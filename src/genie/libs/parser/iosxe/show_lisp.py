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
    * show lisp service {service} summary
    * show lisp {lisp_id} service {service} summary
    * show lisp locator-table {locator_table} service {service} summary
    * show lisp locator-table vrf {vrf} service {service} summary
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
    * show lisp instance-id {instance_id} ethernet map-cache {eid_prefix}
    * show lisp {lisp_id} instance-id {instance_id} ethernet map-cache {eid_prefix}
    * show lisp eid-table vlan {vlan_id} ethernet map-cache {eid_prefix}
    * show lisp locator-table {locator_table} ethernet map-cache {eid_prefix}
    * show lisp {lisp_id} redundancy
    * show lisp redundancy
    * show lisp locator-table {locator_table} redundancy
    * show lisp {lisp_id} instance-id {instance_id} {address_family} eid-watch
    * show lisp instance-id {instance_id} {address_family} eid-watch
    * show lisp locator-table {locator_table} instance-id {instance_id} {address_family} eid-watch
    * show lisp eid-table {eid_table} {address_family} eid-watch
    * show lisp eid-table vlan {vlan_id} ethernet eid-watch
    * show lisp {lisp_id} instance-id {instance_id} dn statistics
    * show lisp remote-locator-set {remote_locator_type}
    * show lisp remote-locator-set name {remote_locator_name}
    * show lisp {lisp_id} remote-locator-set {remote_locator_type}
    * show lisp {lisp_id} remote-locator-set name {remote_locator_name}
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, ListOf, Optional
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

    cli_command = ['show lisp session',
                   'show lisp session {established}']
    exclude = ['time']

    def cli(self, output=None, established=None):
        if output is None:
            if established:
                if established == "established":
                    out = self.device.execute(self.cli_command[1].format(established=established))
                else:
                    raise ValueError("value of established should be 'established'")
            else:
                out = self.device.execute(self.cli_command[0])
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
# Schema for 'show lisp <lisp_id> extranet <extranet_name> instance-id <instance_id>'
# ========================================================================
class ShowLispExtranetSchema(MetaParser):

    ''' Schema for
        * show lisp extranet {extranet_name} instance-id {instance_id}
        * show lisp {lisp_id} extranet {extranet_name} instance-id {instance_id}
    '''
    schema = {
        'lisp_id': {
            int: {
                'home_instance': int,
                'total': int,
                'eid_prefix': {
                    str:{
                        'type': str,
                        'source': str,
                        'iid': int,
                        'eid': str,
                        'mask': int
                        }
                    }
                }
            }
        }


# ========================================================================
# Parser for 'show lisp <lisp_id> extranet <extranet_name> instance-id <instance_id>'
# ========================================================================
class ShowLispExtranet(ShowLispExtranetSchema):

    ''' Parser for
        * show lisp extranet {extranet_name} instance-id {instance_id}
        * show lisp {lisp_id} extranet {extranet_name} instance-id {instance_id}
    '''
    cli_command = ['show lisp extranet {extranet_name} instance-id {instance_id}',
                   'show lisp {lisp_id} extranet {extranet_name} instance-id {instance_id}']

    def cli(self, extranet_name, instance_id, output=None, lisp_id=None):

        if output is None:
            if lisp_id and extranet_name and instance_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, extranet_name=extranet_name, instance_id=instance_id))
            else:
                output = self.device.execute(self.cli_command[0].format(extranet_name=extranet_name, instance_id=instance_id))
        ret_dict = {}

        # Output for router lisp 0
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>(\d+))$")

        # Home Instance ID: 101
        p2 = re.compile(r"^Home\s+Instance\s+ID:\s+(?P<home_instance>(\d+))$")

        # Provider    Dynamic     103        88.88.88.0/24
        p3 = re.compile(r"^(?P<type>Provider|Subscriber)\s+(?P<source>Dynamic)\s+"
                        r"(?P<iid>\d+)\s+(?P<eid>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
                        r"\/(?P<mask>\d{1,2})$")

        # Total entries: 5
        p4 = re.compile(r"^Total\s+entries:\s+(?P<total>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})
                continue

            # Home Instance ID: 101
            m = p2.match(line)
            if m:
                if lisp_id != "all":
                    lisp_id = int(lisp_id) if lisp_id else 0
                    lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                groups = m.groupdict()
                home_instance = int(groups['home_instance'])
                lisp_id_dict.update({'home_instance':home_instance})
                lisp_id_dict.setdefault('total')
                continue

            # Provider    Dynamic     103        88.88.88.0/24
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                type = groups['type']
                source = groups['source']
                iid = int(groups['iid'])
                eid = groups['eid']
                mask = int(groups['mask'])
                eid_prefix = "{}/{}".format(eid,mask)
                eid_dict = lisp_id_dict.setdefault('eid_prefix',{})\
                                       .setdefault(eid_prefix,{})
                eid_dict.update({'type':type,
                                 'source':source,
                                 'iid':iid,
                                 'eid':eid,
                                 'mask':mask})
                continue

            # Total entries: 5
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                total = int(groups['total'])
                lisp_id_dict.update({'total':total})
                continue
        return ret_dict


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
        p4 = re.compile(r'Proxy\-(ITR|ETR) +Router +\((?P<proxy_type>(PITR|PETR))\)'
                        r'*: +(?P<proxy_itr_router>(enabled|disabled))'
                        r'(?: +RLOCs: +(?P<proxy_itr_rloc>'
                        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})))?$')

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
        p24 = re.compile(r'^Publisher\(s\):\s+(?P<publishers>.*)')

        # Subscriber(s):                           *** NOT FOUND ***
        p25 = re.compile(r'^Subscriber\(s\):\s+(?P<subscribers>.*)')

        # ITR Map-Resolver(s):                 10.64.4.4, 10.166.13.13
        p26 = re.compile(r'ITR +Map\-Resolver\(s\) *: +(?P<mr_address>(.*))$')

        #                                      10.84.66.66 *** not reachable ***
        p26_1 = re.compile(r'^(?P<prefix_list>([0-9\.\:]+))(?: +\*.*)?$')

        # ETR Map-Server(s):                   10.64.4.4 (17:49:58), 10.166.13.13 (00:00:35)
        p27 = re.compile(r'ETR +Map\-Server\(s\) *: +(?P<ms_address>(.*))$')

        #                                      10.84.66.66 (never)
        p27_1 = re.compile(r'^(?P<prefix_list>([0-9\.\:]+))(?: +\((?P<uptime>(\S+))\))?$')

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
                for publishers in publishers_list:
                    publishers.append(publishers)

            # Subscriber(s):                           *** NOT FOUND ***
            m = p25.match(line)
            if m:
                group = m.groupdict()
                subscribers = group['subscribers'].split(',')
                subscribers_list = pub_sub_dict.setdefault('subscribers',[])
                for subscribers in subscribers_list:
                    subscribers.append(subscribers)

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
                continue

            #                                  10.84.66.66 (never)
            m = p26_1.match(line)
            if m:
                group = m.groupdict()
                prefix_list = group['prefix_list']
                if etr_mr_dict:
                    etr_mr_dict.update({'prefix_list':prefix_list})
                else:
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
        p5 = re.compile(r'(?P<locator>(\S+)) +(?P<uptime>(\S+))'
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
# Schema for 'show lisp {lisp_id} instance-id <instance_id> <service> dabatase'
# =======================================================================
class ShowLispDatabaseSuperParserSchema(MetaParser):

    '''Schema for "show lisp {lisp_id} instance-id <instance_id> <service> dabatase" '''
    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'eid_table': str,
                        'lsb': str,
                        'entries': {
                            'total': int,
                            'no_route': int,
                            'inactive': int,
                            'eids': {
                                str: {
                                    'eid': str,
                                    'mask': int,
                                    Optional('dynamic_eid'): str,
                                    Optional('locator_set'): str,
                                    Optional('no_route_to_prefix'): bool,
                                    Optional('proxy'): bool,
                                    Optional('sgt'): int,
                                    Optional('domain_id'): str,
                                    Optional('service_insertion'): str,
                                    Optional('auto_discover_rlocs'): bool,
                                    Optional('uptime'): str,
                                    Optional('last_change'): str,
                                    Optional('locators'): {
                                        str: {
                                            'priority': int,
                                            'weight': int,
                                            'source': str,
                                            'location': str,
                                            'state': str
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


class ShowLispDatabaseSuperParser(ShowLispDatabaseSuperParserSchema):
    """Parser for show lisp Database"""

    def cli(self, lisp_id=None, instance_id=None, service=None, locator_table=None, output=None):

        ret_dict = {}

        # LISP ETR IPv4 Mapping Database for EID-table default (IID 1), LSBs: 0x1
        p1 = re.compile(r'^LISP\s+ETR\s+(MAC|IPv6|IPv4)\s+Mapping\s+Database\s+'
                        r'for\s+LISP\s+(?P<lisp_id>\d+)\s+EID-table\s+'
                        r'(?P<eid_table>(vrf\s\w+)|(Vlan\s\d+))\s+'
                        r'\(IID\s(?P<instance_id>\d+)\),\sLSBs:\s(?P<lsb>\S+)$')

        # Entries total 2, no-route 0, inactive 0, do-not-register 1
        p2 = re.compile(r'^Entries\s+total\s+(?P<total>\d+),\s+no-route\s+'
                        r'(?P<no_route>\d),\s+inactive\s+(?P<inactive>\d+),'
                        r'\s+do-not-register\s+\d+$')

        # aabb.cc00.c901/48, dynamic-eid Auto-L2-group-101, inherited from default locator-set RLOC *** NO ROUTE TO EID PREFIX ***
        p3 = re.compile(r'^(?P<eid>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}|'
                        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[a-fA-F\d\:]+)(\/)?'
                        r'(?P<mask>\d{1,3})(,\s)?(route-import)?'
                        r'(dynamic-eid\s+(?P<dynamic_eid>\S+))?'
                        r'(,\sdo\snot\sregister)?(,\sinherited\sfrom\sdefault\s+)?'
                        r'(locator-set\s(?P<locator_set>\S+))?(\s\*\*\*\s'
                        r'(?P<no_route_to_prefix>NO ROUTE TO EID PREFIX)\s\*\*\*)?'
                        r'(,\s(?P<auto_discover_rlocs>auto-discover-rlocs))?'
                        r'(,\s(?P<proxy>proxy))?(,\s(?P<default>default-ETR))?$')

        # Uptime: 1w3d, Last-change: 1w3d
        p4 = re.compile(r'^Uptime:\s+(?P<uptime>\S+),\s+Last-change:\s+(?P<last_change>\S+)$')

        # Domain-ID: local
        p5 = re.compile(r'^Domain-ID:\s+(?P<domain_id>\S+)$')

        # Service-Insertion: N/A (0)
        p6 = re.compile(r'^Service-Insertion:\s+(?P<service_insertion>[\S\s]+)$')

        # SGT: 10
        p7 = re.compile(r'^SGT:\s+(?P<sgt>\d+)$')

        # 11.11.11.11   10/10   cfg-intf   site-self, reachable
        p8 = re.compile(r'^(?P<locators>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                        r'\s+(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<source>\S+)'
                        r'\s+(?P<location>\S+),\s(?P<state>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # LISP ETR IPv4 Mapping Database for EID-table default (IID 1), LSBs: 0x1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id = int(group['lisp_id'])
                eid_table = group['eid_table']
                instance_id = int(group['instance_id'])
                lsb = group['lsb']
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})\
                                       .setdefault('instance_id',{})\
                                       .setdefault(instance_id,{})
                lisp_id_dict.update({'eid_table':eid_table,
                                     'lsb':lsb})
                continue

            # Entries total 2, no-route 0, inactive 0, do-not-register 1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                total = int(group['total'])
                no_route = int(group['no_route'])
                inactive = int(group['inactive'])
                entries_dict = lisp_id_dict.setdefault('entries',{})
                entries_dict.update({'total':total,
                                     'no_route':no_route,
                                     'inactive':inactive})
                continue

            #  aabb.cc00.c901/48, dynamic-eid Auto-L2-group-101, inherited from default locator-set RLOC *** NO ROUTE TO EID PREFIX ***
            m = p3.match(line)
            if m:
                group = m.groupdict()
                eid = group['eid']
                mask = int(group['mask'])
                eids = "{}/{}".format(eid,mask)
                eid_dict = entries_dict.setdefault('eids',{})\
                                       .setdefault(eids,{})
                eid_dict.update({'eid':eid,
                                 'mask':mask})
                if group['dynamic_eid']:
                    dynamic_eid = group['dynamic_eid']
                    eid_dict.update({'dynamic_eid':dynamic_eid})
                if group['locator_set']:
                    locator_set = group['locator_set']
                    eid_dict.update({'locator_set':locator_set})
                if group['no_route_to_prefix']:
                    eid_dict.update({'no_route_to_prefix':True})
                if group['proxy']:
                    eid_dict.update({'proxy':True})
                if group['auto_discover_rlocs']:
                    eid_dict.update({'auto_discover_rlocs':True})
                continue

            # Uptime: 1w3d, Last-change: 1w3d
            m = p4.match(line)
            if m:
                group = m.groupdict()
                uptime = group['uptime']
                last_change = group['last_change']
                eid_dict.update({'uptime':uptime,
                                 'last_change':last_change})
                continue

            # Domain-ID: local
            m = p5.match(line)
            if m:
                group = m.groupdict()
                domain_id = group['domain_id']
                eid_dict.update({'domain_id':domain_id})
                continue

            # Service-Insertion: N/A
            m = p6.match(line)
            if m:
                group = m.groupdict()
                service_insertion = group['service_insertion']
                eid_dict.update({'service_insertion':service_insertion})
                continue

            # SGT: 10
            m = p7.match(line)
            if m:
                group = m.groupdict()
                sgt = group['sgt']
                eid_dict.update({'sgt':sgt})
                continue

            # 11.11.11.11   10/10   cfg-intf   site-self, reachable
            m = p8.match(line)
            if m:
                group = m.groupdict()
                locators = group['locators']
                priority = int(group['priority'])
                weight = int(group['weight'])
                source = group['source']
                location = group['location']
                state = group['state']
                locator_dict = eid_dict.setdefault('locators',{})\
                                       .setdefault(locators,{})
                locator_dict.update({'priority':priority,
                                     'weight':weight,
                                     'source':source,
                                     'location':location,
                                     'state':state})
                continue
        return ret_dict


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
                                                   service=service))
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
                                                   service=service))
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(vrf = vrf,
                                                   service=service))
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


class ShowLispSiteSuperParserSchema(MetaParser):
    """ Schema for show lisp site"""
    schema = {
        'lisp_id': {
            int : {
                'site_name': {
                    str: {
                        'instance_id': {
                            int: {
                                'eid_prefix': {
                                    str: {
                                        'last_registered': str,
                                        'who_last_registered': str,
                                        'up': str
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispSiteSuperParser(ShowLispSiteSuperParserSchema):
    """Parser for show lisp site"""

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, vrf=None, output=None):

        ret_dict = {}

        # Output for router lisp 0
        p1 = re.compile(r'^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)$')

        # Shire          never     no     --                   0        1.1.1.0/24
        p2 = re.compile(r'^((?P<site_name>\S+)\s+)?(?P<last_registered>\S+)\s+'
                        r'(?P<up>yes|no)#?\s+(?P<who_last_registered>\S+)\s+'
                        r'(?P<instance_id>\d+)\s+(?P<eid_prefix>\d{1,3}\.'
                        r'\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3}'
                        r'|any-mac|([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{2})$')

        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id = int(group['lisp_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}) \
                                       .setdefault(lisp_id, {})
                continue

            # Shire          never     no     --                   0        1.1.1.0/24
            m = p2.match(line)
            if m:
                lisp_id = int(lisp_id) if lisp_id else 0
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                group = m.groupdict()
                site_name = group['site_name']
                last_registered = group['last_registered']
                up = group['up']
                who_last_registered = group['who_last_registered']
                instance_id = int(group['instance_id'])
                eid_prefix = group['eid_prefix']
                if site_name:
                    site_dict = lisp_id_dict.setdefault('site_name', {}) \
                                            .setdefault(site_name, {})
                site_info = site_dict.setdefault('instance_id', {}) \
                                     .setdefault(instance_id, {}) \
                                     .setdefault('eid_prefix', {}) \
                                     .setdefault(eid_prefix, {})
                site_info.update({'last_registered':last_registered,
                                  'who_last_registered':who_last_registered,
                                  'up':up})
                continue
        return ret_dict


# ===================
# Parser for:
#  * 'show lisp site'
# ===================
class ShowLispSite(ShowLispSiteSuperParser):

    """ Parser for show lisp site
        * show lisp site
        * show lisp {lisp_id} site
        * show lisp site instance-id {instance_id}
        * show lisp {lisp_id} site instance-id {instance_id}
        * show lisp site eid-table {eid_table}
        * show lisp {lisp_id} site eid-table {eid_table}
        * show lisp site eid-table vrf {vrf}
        * show lisp {lisp_id} site eid-table vrf {vrf}
    """

    cli_command = ['show lisp site',
                   'show lisp {lisp_id} site',
                   'show lisp site instance-id {instance_id}',
                   'show lisp {lisp_id} site instance-id {instance_id}',
                   'show lisp site eid-table {eid_table}',
                   'show lisp {lisp_id} site eid-table {eid_table}',
                   'show lisp site eid-table vrf {vrf}',
                   'show lisp {lisp_id} site eid-table vrf {vrf}']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, vrf=None, output=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[3].\
                                            format(lisp_id=lisp_id,
                                                   instance_id=instance_id))
            elif lisp_id and eid_table:
                output = self.device.execute(self.cli_command[5].\
                                            format(lisp_id=lisp_id,
                                                   eid_table=eid_table))
            elif lisp_id and vrf:
                output = self.device.execute(self.cli_command[7].\
                                            format(lisp_id=lisp_id,
                                                   vrf=vrf))
            elif vrf:
                output = self.device.execute(self.cli_command[6].\
                                            format(vrf=vrf))
            elif eid_table:
                output = self.device.execute(self.cli_command[4].\
                                            format(eid_table=eid_table))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].\
                                            format(instance_id=instance_id))
            elif lisp_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id))
            else:
                output = self.device.execute(self.cli_command[0])
        return super().cli(output=output)


# ==========================================
# Parser for:
#  * 'show lisp instance-id {instance_id} ethernet server'
# ==========================================
class ShowLispInstanceIdEthernetServer(ShowLispSiteSuperParser):

    """ Parser for show lisp site
        * show lisp instance-id {instance_id} ethernet server
        * show lisp {lisp_id} instance-id {instance_id} ethernet server
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server
        * show lisp eid-table vlan {vlan} ethernet server
    """

    cli_command = ['show lisp instance-id {instance_id} ethernet server',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet server',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ethernet server',
                   'show lisp eid-table vlan {vlan} ethernet server']

    def cli(self, lisp_id=None, instance_id=None, locator_table=None, vlan=None, output=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id,
                                                   instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].\
                                            format(locator_table=locator_table,
                                                   instance_id=instance_id))
            elif vlan:
                output = self.device.execute(self.cli_command[3].\
                                            format(vlan=vlan))
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id))
        return super().cli(output=output)


class ShowLispIpv4ServerExtranetPolicy(ShowLispSiteSuperParser):

    """ Parser for show lisp site
        * show lisp instance-id {instance_id} ipv4 server extranet-policy
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server extranet-policy
        * show lisp eid-table {eid_table} ipv4 server extranet-policy
        * show lisp eid-table vrf {vrf} ipv4 server extranet-policy
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server extranet-policy
    """

    cli_command = ['show lisp instance-id {instance_id} ipv4 server extranet-policy',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server extranet-policy',
                   'show lisp eid-table {eid_table} ipv4 server extranet-policy',
                   'show lisp eid-table vrf {vrf} ipv4 server extranet-policy',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server extranet-policy']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, locator_table=None, vrf=None, output=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id,
                                                   instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[4].\
                                            format(locator_table=locator_table,
                                                   instance_id=instance_id))
            elif vrf:
                output = self.device.execute(self.cli_command[3].\
                                            format(vrf=vrf))
            elif eid_table:
                output = self.device.execute(self.cli_command[2].\
                                            format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id))
        return super().cli(output=output)


class ShowLispIpv6ServerExtranetPolicy(ShowLispSiteSuperParser):

    """ Parser for show lisp site
        * show lisp instance-id {instance_id} ipv6 server extranet-policy
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server extranet-policy
        * show lisp eid-table {eid_table} ipv6 server extranet-policy
        * show lisp eid-table vrf {vrf} ipv6 server extranet-policy
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server extranet-policy
    """

    cli_command = ['show lisp instance-id {instance_id} ipv6 server extranet-policy',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server extranet-policy',
                   'show lisp eid-table {eid_table} ipv6 server extranet-policy',
                   'show lisp eid-table vrf {vrf} ipv6 server extranet-policy',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server extranet-policy']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, locator_table=None, vrf=None, output=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id,
                                                   instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[4].\
                                            format(locator_table=locator_table,
                                                   instance_id=instance_id))
            elif vrf:
                output = self.device.execute(self.cli_command[3].\
                                            format(vrf=vrf))
            elif eid_table:
                output = self.device.execute(self.cli_command[2].\
                                            format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id))
        return super().cli(output=output)


class ShowLispInstanceIdIpv4Server(ShowLispSiteSuperParser):

    """ Parser for
        * show lisp instance-id {instance_id} ipv4 server
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server
        * show lisp eid-table vrf {vrf} ipv4 server
        * show lisp eid-table {eid_table} ipv4 server
    """

    cli_command = ['show lisp instance-id {instance_id} ipv4 server',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server',
                   'show lisp eid-table vrf {vrf} ipv4 server',
                   'show lisp eid-table {eid_table} ipv4 server']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, vrf=None, locator_table=None, output=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id,
                                                   instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].\
                                            format(locator_table=locator_table,
                                                   instance_id=instance_id))
            elif vrf:
                output = self.device.execute(self.cli_command[3].\
                                            format(vrf=vrf))
            elif eid_table:
                output = self.device.execute(self.cli_command[4].\
                                            format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id))
        return super().cli(output=output)


class ShowLispInstanceIdIpv6Server(ShowLispSiteSuperParser):

    """ Parser for
        * show lisp instance-id {instance_id} ipv6 server
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server
        * show lisp eid-table vrf {vrf} ipv6 server
        * show lisp eid-table {eid_table} ipv6 server
    """

    cli_command = ['show lisp instance-id {instance_id} ipv6 server',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server',
                   'show lisp eid-table vrf {vrf} ipv6 server',
                   'show lisp eid-table {eid_table} ipv6 server']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, vrf=None, locator_table=None, output=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id,
                                                   instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].\
                                            format(locator_table=locator_table,
                                                   instance_id=instance_id))
            elif vrf:
                output = self.device.execute(self.cli_command[3].\
                                            format(vrf=vrf))
            elif eid_table:
                output = self.device.execute(self.cli_command[4].\
                                            format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id))
        return super().cli(output=output)


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
        #Publication Information for LISP 0 EID-table vrf red (IID 4100)
        p1 = re.compile(r"^Publication\s+Information\s+for\s+LISP\s+"
                        r"(?P<lisp_id>\d+)\s+EID-table\s+vrf\s+red\s+"
                        r"\(IID\s+(?P<instance_id>\d+)\)$")

        #Entries total 2
        p2 = re.compile(r"^Entries\s+total\s+(?P<total_entries>\d+)")

        #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
        p3 = re.compile(r"^\S+\s+\S+\s+(?P<eid_prefix>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}))")

        #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
        p4 = re.compile(r"^(?P<publisher_ip>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))\s+")

        #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
        p5 = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+(?P<last_published>\S+)")

        #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
        p6 = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\S+\s+\d{1,3}\."
                        r"\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,3}\s+(?P<rloc>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

        #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
        p7 = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\S+\s+\S+\s+\S+\s+(?P<encap_iid>\S+)")

        for line in output.splitlines():
            
            #Publication Information for LISP 0 EID-table vrf red (IID 4100)
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                lisp_id_dict.setdefault(lisp_id,{})
                lisp_v4_pub_dict['lisp_id'] = lisp_id_dict
                instance_id_dict.setdefault(instance_id,{})
                lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'] = instance_id_dict
                continue

            #Entries total 2
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                entries = int(groups['total_entries'])
                lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]['total_entries'] = entries
                continue

            #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11
            m=p3.match(line)
            if m:
                groups = m.groupdict()
                publications = groups['eid_prefix']
                publications_dict.setdefault(publications,{})
                lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]['eid_prefix'] = publications_dict
                #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
                m=p4.match(line)
                if m:
                    groups = m.groupdict()
                    publisher_ip = groups['publisher_ip']
                    lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]\
                        ['eid_prefix'][publications]['publisher_ip'] = publisher_ip
                #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
                m=p5.match(line)
                if m:
                    groups = m.groupdict()
                    last_published = groups['last_published']
                    lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]\
                        ['eid_prefix'][publications]['last_published'] = last_published
                #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
                m=p6.match(line)
                if m:
                    groups = m.groupdict()
                    rloc = groups['rloc']
                    lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]\
                        ['eid_prefix'][publications]['rloc'] = rloc
                #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
                m=p7.match(line)
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

        #Publication Information for LISP 0 EID-table vrf red (IID 4100)
        p1 = re.compile(r"^Publication\s+Information\s+for\s+LISP\s+"
                        r"(?P<lisp_id>\d+)\s+EID-table\s+vrf\s+red\s+"
                        r"\(IID\s+(?P<instance_id>\d+)\)$")

        #Entries total 2
        p2 = re.compile(r"^Entries\s+total\s+(?P<total_entries>\d+)")

        #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
        p3 = re.compile(r"^\S+\s+\S+\s+(?P<eid_prefix>[a-fA-F\d\:]+\/\d{1,3})")

        #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
        p4 = re.compile(r"^(?P<publisher_ip>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))\s+")

        #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
        p5 = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+(?P<last_published>\S+)")

        #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
        p6 = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\S+\s+[a-fA-F\d\:]+"
                        r"\/\d{1,3}\s+(?P<rloc>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

        #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
        p7 = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\S+\s+\S+\s+\S+\s+(?P<encap_iid>\S+)")

        for line in output.splitlines():

            #Publication Information for LISP 0 EID-table vrf red (IID 4100)
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                lisp_id_dict.setdefault(lisp_id,{})
                lisp_v6_pub_dict['lisp_id'] = lisp_id_dict
                instance_id_dict.setdefault(instance_id,{})
                lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'] = instance_id_dict
                continue

            #Entries total 2
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                entries = int(groups['total_entries'])
                lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]['total_entries'] = entries
                continue

            #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
            m=p3.match(line)
            if m:
                groups = m.groupdict()
                publications = groups['eid_prefix']
                publications_dict.setdefault(publications,{})
                lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]['eid_prefix'] = publications_dict

                #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
                m=p4.match(line)
                if m:
                    groups = m.groupdict()
                    publisher_ip = groups['publisher_ip']
                    lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]\
                        ['eid_prefix'][publications]['publisher_ip'] = publisher_ip
                #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
                m=p5.match(line)
                if m:
                    groups = m.groupdict()
                    last_published = groups['last_published']
                    lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]\
                        ['eid_prefix'][publications]['last_published'] = last_published
                #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
                m=p6.match(line)
                if m:
                    groups = m.groupdict()
                    rloc = groups['rloc']
                    lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]\
                        ['eid_prefix'][publications]['rloc'] = rloc
                #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
                m=p7.match(line)
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
                            str:  {
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
        p1 = re.compile(r'LISP +IPv(?P<v4_v6>[4-6]) +imported +routes +for(\sLISP\s)?(?P<lisp_id>\d)? +EID-table(\svrf)? +(?P<vrf>.+) +\(+IID +(?P<instance_id>\d+)+\)$')
        
        # Config: 2, Entries: 1 (limit 5000)
        p2 = re.compile(r'Config: +(?P<config>\d+), +Entries: +(?P<entries>\d+) +\(+limit+ (?P<limit>\d+)+\)$')

        # 50.1.1.0/24               00:00:13  static                          installed 
        p3 = re.compile(r'(?P<eid>[\da-fA-F.:]+\/\d+\S+) +(?P<uptime>\S+) +(?P<source>.+\S+) +(?P<rloc>.+\S+)? +(?P<cached>none|installed|replaced|full\S+)+(?P<state>.+)?$')

        for line in output.splitlines():
            line = line.strip()
            # LISP IPv4 imported routes for EID-table vrf blue (IID 102)
            # LISP IPv4 imported routes for LISP 1 EID-table vrf red (IID 105)

            m = p1.match(line)
            if m:
                group = m.groupdict()
                if group['lisp_id'] == None:
                    lisp_id = 0
                else:
                    lisp_id = int(group['lisp_id'])
                instance_id = int(group['instance_id'])
                lisp_id_dict = \
                    parsed_dict.setdefault('lisp_id', {}) \
                               .setdefault(lisp_id, {})
                instance_id_dict = \
                    lisp_id_dict.setdefault('instance_id', {})\
                                .setdefault(instance_id, {})
    
                instance_id_dict.update({'eid_table': group['vrf']})
                continue


            # Config: 2, Entries: 1 (limit 5000)
            m = p2.match(line)
            if m:
               group = m.groupdict()
               instance_id_dict.update({'config': int(group['config'])})
               instance_id_dict.update({'entries': int(group['entries'])})
               instance_id_dict.update({'limit': int(group['limit'])})
               continue

            # 50.1.1.0/24               00:00:13  static                          installed
            m = p3.match(line)
            if m:
               group = m.groupdict()
               eid_dict = \
                   instance_id_dict.setdefault('eids',{})\
                                   .setdefault(group['eid'],{})
             
               eid_dict.update({'uptime': group['uptime']})  
               eid_dict.update({'source': group['source']})
               eid_dict.update({'cache_db': group['cached']})

               if group['rloc'] != None:
                   eid_dict.update({'rloc_set': group['rloc']})         
               
               if group['state'] != None:
                   eid_dict.update({'state': group['state']})

        return parsed_dict

class ShowLispIpv4RouteImportMapCache(ShowLispRouteImportMapCacheSuperParser,ShowLispRouteImportMapCacheSchema):
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
             elif eid_table and eid_prefix:
                 output = self.device.execute(self.cli_command[11].\
                                             format(eid_table=eid_table, eid_prefix=eid_prefix))
             elif eid_table:
                 output = self.device.execute(self.cli_command[9].\
                                             format(eid_table=eid_table))
             elif locator_table and instance_id and eid_prefix:
                 output = self.device.execute(self.cli_command[14].\
                                             format(locator_table=locator_table, instance_id=instance_id, eid_prefix=eid_prefix))
             elif locator_table and instance_id and eid:
                 output = self.device.execute(self.cli_command[13].\
                                             format(locator_table=locator_table, instance_id=instance_id, eid=eid))
             else:
                 output = self.device.execute(self.cli_command[12].\
                                             format(locator_table=locator_table, instance_id=instance_id))
          else:
              output = output
          return super().cli(output=output)

class ShowLispIpv6RouteImportMapCache(ShowLispRouteImportMapCacheSuperParser,ShowLispRouteImportMapCacheSchema):
      '''route Import map-cache cli variations'''
      cli_command = [
        'show lisp instance-id {instance_id} ipv6 route-import map-cache',
        'show lisp instance-id {instance_id} ipv6 route-import map-cache {eid}',
        'show lisp instance-id {instance_id} ipv6 route-import map-cache {eid_prefix}',
        'show lisp {lisp_id} instance-id {instance_id} ipv6 route-import map-cache',
        'show lisp {lisp_id} instance-id {instance_id} ipv6 route-import map-cache {eid}',
        'show lisp {lisp_id} instance-id {instance_id} ipv6 route-import map-cache {eid_prefix}',
        'show lisp eid-table vrf {vrf} ipv6 route-import map-cache',
        'show lisp eid-table vrf {vrf} ipv6 route-import map-cache {eid}',
        'show lisp eid-table vrf {vrf} ipv6 route-import map-cache {eid_prefix}',
        'show lisp eid-table {eid_table} ipv6 route-import map-cache',
        'show lisp eid-table {eid_table} ipv6 route-import map-cache {eid}',
        'show lisp eid-table {eid_table} ipv6 route-import map-cache {eid_prefix}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 route-import map-cache',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 route-import map-cache {eid}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 route-import map-cache {eid_prefix}'
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
             elif eid_table and eid_prefix:
                 output = self.device.execute(self.cli_command[11].\
                                             format(eid_table=eid_table, eid_prefix=eid_prefix))
             elif eid_table:
                 output = self.device.execute(self.cli_command[9].\
                                             format(eid_table=eid_table))
             elif locator_table and instance_id and eid_prefix:
                 output = self.device.execute(self.cli_command[14].\
                                             format(locator_table=locator_table, instance_id=instance_id, eid_prefix=eid_prefix))
             elif locator_table and instance_id and eid:
                 output = self.device.execute(self.cli_command[13].\
                                             format(locator_table=locator_table, instance_id=instance_id, eid=eid))
             else:
                 output = self.device.execute(self.cli_command[12].\
                                             format(locator_table=locator_table, instance_id=instance_id))
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
                        Optional('eid_prefix'): {
                            str: {
                            'producer': str,
                            'created': str
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
        show lisp instance-id {instance_id} ipv6 away
        show lisp instance-id {instance_id} ipv6 away {eid}
        show lisp instance-id {instance_id} ipv6 away {eid_prefix}
        show lisp {lisp_id} instance-id {instance_id} ipv6 away
        show lisp {lisp_id} instance-id {instance_id} ipv6 away {eid}
        show lisp {lisp_id} instance-id {instance_id} ipv6 away {eid_prefix}
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away {eid}
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away {eid_prefix}
        show lisp eid-table {eid_table} ipv6 away
        show lisp eid-table {eid_table} ipv6 away {eid}
        show lisp eid-table {eid_table} ipv6 away {eid_prefix}
        show lisp eid-table vrf {eid_table} ipv6 away
        show lisp eid-table vrf {eid_table} ipv6 away {eid}
        show lisp eid-table vrf {eid_table} ipv6 away {eid_prefix}
    '''
    def cli(self, output=None):
        parsed_dict = {}
        # LISP Away Table for router lisp 0 (blue) IID 102
        p1 = re.compile(r'^LISP +Away +Table +for +router +lisp (?P<lisp_id>\d+) +\((?P<vrf>.+)\) +IID +(?P<instance_id>\d+)$')
        # Entries: 1
        p2 = re.compile(r'^Entries: +(?P<entries>\d+)$')
        # 10.1.0.0/16                             dyn-eid                        4d20h
        # 192.168.1.0/24                          local EID                      00:23:50
        p3 = re.compile(r'^(?P<eid_prefix>[\da-fA-F.:]+\S+) +(?P<producer>\w+\s\w+\,\s\w+\s\w+|\w+\s\w+|\w+\-\w+) +(?P<created>\S+)$')
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

class ShowLispIpv6Away(ShowLispEidAwaySuperParser, ShowLispEidAwaySchema):
    ''' Show Command Ipv6 Away
        show lisp instance-id {instance_id} ipv6 away
        show lisp instance-id {instance_id} ipv6 away {eid}
        show lisp instance-id {instance_id} ipv6 away {eid_prefix}
        show lisp {lisp_id} instance-id {instance_id} ipv6 away
        show lisp {lisp_id} instance-id {instance_id} ipv6 away {eid}
        show lisp {lisp_id} instance-id {instance_id} ipv6 away {eid_prefix}
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away {eid}
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away {eid_prefix}
        show lisp eid-table {eid_table} ipv6 away
        show lisp eid-table {eid_table} ipv6 away {eid}
        show lisp eid-table {eid_table} ipv6 away {eid_prefix}
        show lisp eid-table vrf {eid_table} ipv6 away
        show lisp eid-table vrf {eid_table} ipv6 away {eid}
        show lisp eid-table vrf {eid_table} ipv6 away {eid_prefix}
    '''
    
    cli_command = [
        'show lisp instance-id {instance_id} ipv6 away',
        'show lisp instance-id {instance_id} ipv6 away {eid}',
        'show lisp instance-id {instance_id} ipv6 away {eid_prefix}',
        'show lisp {lisp_id} instance-id {instance_id} ipv6 away',
        'show lisp {lisp_id} instance-id {instance_id} ipv6 away {eid}',
        'show lisp {lisp_id} instance-id {instance_id} ipv6 away {eid_prefix}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away {eid}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away {eid_prefix}',
        'show lisp eid-table {eid_table} ipv6 away',
        'show lisp eid-table {eid_table} ipv6 away {eid}',
        'show lisp eid-table {eid_table} ipv6 away {eid_prefix}',
        'show lisp eid-table vrf {vrf} ipv6 away', 
        'show lisp eid-table vrf {vrf} ipv6 away {eid}',
        'show lisp eid-table vrf {vrf} ipv6 away {eid_prefix}'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, locator_table=None,
            eid_table=None, eid=None, eid_prefix=None):
        if output is None:
            if lisp_id and instance_id and eid:
                output = self.device.execute(self.cli_command[4].\
                                                format(lisp_id=lisp_id, \
                                                   instance_id=instance_id, eid=eid))
            elif lisp_id and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[5].\
                                                format(lisp_id=lisp_id, \
                                                   instance_id=instance_id, \
                                                   eid_prefix=eid_prefix))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[3].\
                                                format(lisp_id=lisp_id, \
                                                   instance_id=instance_id))
            elif instance_id and eid:
                output = self.device.execute(self.cli_command[1].\
                                                format(instance_id=instance_id, \
                                                   eid= eid))
            elif instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[2].\
                                                format(instance_id=instance_id,\
                                                   eid_prefix=eid_prefix))
            elif instance_id:
                output = self.device.execute(self.cli_command[0].\
                                                format(instance_id=instance_id))
            elif locator_table and instance_id and eid:
                output = self.device.execute(self.cli_command[7].\
                                                format(locator_table=locator_table, \
                                                   instance_id=instance_id, \
                                                   eid=eid)) 
            elif locator_table and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[8].\
                                                format(locator_table=locator_table, \
                                                   instance_id=instance_id, \
                                                   eid_prefix=eid_prefix))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[6].\
                                                format(locator_table=locator_table, \
                                                   instance_id=instance_id))
            elif eid_table and eid:
                output = self.device.execute(self.cli_command[10].\
                                                format(eid_table=eid_table, eid=eid))
            elif eid_table and eid_prefix:
                output = self.device.execute(self.cli_command[11].\
                                                format(eid_table=eid_table, \
                                                   eid_prefix=eid_prefix))
            elif eid_table:
                output = self.device.execute(self.cli_command[9].\
                                                format(eid_table=eid_table))
            elif vrf and eid:
                output = self.device.execute(self.cli_command[13].\
                                                format(vrf=vrf, eid=eid))
            elif vrf and eid_prefix:
                output = self.device.execute(self.cli_command[14].\
                                                format(vrf=vrf, \
                                                   eid_prefix=eid_prefix))
            else:
                output = self.device.execute(self.cli_command[12].\
                                                format(vrf=vrf))

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

        #Publication Information for LISP 0 EID-table vrf red (IID 4100)
        p1 = re.compile(r"^Publication\s+Information\s+for\s+LISP\s+"
                        r"(?P<lisp_id>\d+)\s+EID-table\s+vrf\s+\S+\s+"
                        r"\(IID\s+(?P<instance_id>\d+)\)$")

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
        #Exported to:          local-eid, map-cache
        p6 = re.compile(r"^Exported\s+to:\s+(?P<exported_to>[\s\S]+)$")

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
            #Publication Information for LISP 0 EID-table vrf red (IID 4100)
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
                        Optional('srvc_ins_type'): str,
                        Optional('srvc_ins_id'): int,
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



class ShowLispEthernetMapCachePrefixSchema(MetaParser):

    ''' Schema for 
      * show lisp instance-id {instance_id} ethernet map-cache {eid_prefix}
      * show lisp {lisp_id} instance-id {instance_id} ethernet map-cache {eid_prefix}
      * show lisp eid-table vlan {vlan_id} ethernet map-cache {eid_prefix}
      * show lisp locator-table {locator_table} ethernet map-cache {eid_prefix}
    '''

    Schema = {
        "lisp_id": {
            int: {
                "instance_id": {
                    int: {
                        "eid_table": str,
                        "entries": int,
                        "eid_prefix": {
                            "str": {
                                "uptime": str,
                                "expiry_time": str,
                                "via": str,
                                "map_reply_state": str,
                                "prefix_location": str,
                                "source_type": str,
                                "last_modified": str,
                                "source_ip": str,
                                "prefix_state": str,
                                "encap": str,
                                "rloc_set": {
                                    "str": {
                                        "uptime": str,
                                        "rloc_state": str,
                                        "priority": int,
                                        "weight": int,
                                        "encap_iid": str,
                                        "last_state_change": {
                                            "time": str, 
                                            "count": int
                                        },
                                        "last_route_reach_change": {
                                            "time": str,
                                            "count": int,
                                        },
                                        "last_pri_weight_change": {
                                            "priority": str,
                                            "weight": str,
                                        },
                                        "rloc_probe_sent": {
                                            "time": str, 
                                            "rtt": int,
                                            "rtt_unit": str,
                                        },
                                    }
                                },
                            }
                        },
                    }
                }
            }
        }
    }


class ShowLispEthernetMapCachePrefix(ShowLispEthernetMapCachePrefixSchema):
    ''' Parser for 
        * show lisp instance-id {instance_id} ethernet map-cache {eid_prefix}
        * show lisp {lisp_id} instance-id {instance_id} ethernet map-cache {eid_prefix}
        * show lisp eid-table vlan {vlan_id} ethernet map-cache {eid_prefix}
        * show lisp locator-table {locator_table} ethernet map-cache {eid_prefix}
    '''

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ethernet map-cache {eid_prefix}',
        'show lisp instance-id {instance_id} ethernet map-cache {eid_prefix}',
        'show lisp eid-table vlan {vlan_id} ethernet map-cache {eid_prefix}',
        'show lisp locator-table {locator_table} ethernet map-cache {eid_prefix}'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, eid_prefix=None, vlan_id=None, 
            locator_table=None):

        if output is None:
            if lisp_id and instance_id and eid_prefix:
                cmd = self.cli_command[0].format(lisp_id=lisp_id, instance_id=instance_id,\
                                                 eid_prefix=eid_prefix)
            elif instance_id and eid_prefix:
                cmd = self.cli_command[1].format(instance_id=instance_id, eid_prefix=eid_prefix)
            elif vlan_id and eid_prefix:
                cmd = self.cli_command[2].format(vlan_id=vlan_id, eid_prefix=eid_prefix)
            else:
                cmd = self.cli_command[3].format(locator_table=locator_table, eid_prefix=eid_prefix)
        
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

        # LISP MAC Mapping Cache for EID-table Vlan 210 (IID 8188), 1 entries
        p2 = re.compile(r'^LISP\sMAC\sMapping\sCache\sfor\sEID-table\s(?P<eid_table>.*)\s\(IID\s(?P<instance_id>\d+)\),\s(?P<entries>\d+)\sentries$')
    
        # 0017.0100.0001/48, uptime: 01:09:06, expires: 22:50:53, via map-reply, complete, local-to-site
        p3 = re.compile(r'^(?P<eid_prefix>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})|([a-fA-F\d\:]+\/\d{1,3})|(([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{1,2})),\suptime:\s(?P<uptime>\S+),\sexpires:\s(?P<expiry_time>\S+),\s+via\s(?P<via>\S+),\s(?P<map_reply_state>\S+),\s(?P<prefix_location>\S+)$')

        # Sources: map-reply
        p4 = re.compile(r'^Sources:\s(?P<source_type>\S+)$')

        # State: complete, last modified: 01:09:06, map-source: 1.1.1.10
        p5 = re.compile(r'^State:\s(?P<state>\S+),\slast\smodified:\s(?P<last_modified>\S+)\smap-source:\s(?P<source_ip>.+)$')

        # Active, Packets out: 139(0 bytes), counters are not accurate (~ 00:00:01 ago)
        p6 = re.compile(r'^(?P<prefix_state>\S+),\sPackets out:\s(?P<packets_out>\d+).+$')

        # Encapsulating dynamic-EID traffic
        p7 = re.compile(r'^Encapsulating\s(?P<encap>.+)$')

        # 1.1.1.10  01:09:06  up      10/10        -
        p8 = re.compile(r'^(?P<rloc_set>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<uptime>\S+)\s+(?P<rloc_state>\S+)\s+(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<encap_iid>\S+)$')

        # Last up-down state change:         01:09:06, state change count: 1
        p9 = re.compile(r'^Last\sup-down\sstate\schange:\s+(?P<time>\S+),\s+state change count:\s+(?P<count>\d+)$')

        # Last route reachability change:    01:09:06, state change count: 1
        p10 = re.compile(r'^Last\sroute\sreachability\schange:\s+(?P<time>\S+),\s+state change count:\s+(?P<count>\d+)$')

        # Last priority / weight change:     never/never
        p11 = re.compile(r'^Last\spriority\s\/\sweight\schange:\s+(?P<priority>\S+)\/(?P<weight>\S+)$')

        # Last RLOC-probe sent:            01:09:06 (rtt 1ms)
        p12 = re.compile(r'^Last\sRLOC-probe\ssent:\s+(?P<time>\S+)\s\(rtt (?P<rtt>\d+)(?P<rtt_unit>\S+)\)$')

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

            # LISP MAC Mapping Cache for EID-table Vlan 210 (IID 8188), 1 entries
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group['instance_id']:
                    instance_id = int(group['instance_id'])
                lisp_id_dict = \
                    ret_dict.setdefault('lisp_id', {})\
                        .setdefault(lisp_id, {})\
                        .setdefault('instance_id', {})\
                        .setdefault(instance_id, {})
                lisp_id_dict.update({
                    'eid_table': group['eid_table'],
                    'entries': int(group['entries'])
                })
                continue
            
            # 0017.0100.0001/48, uptime: 01:09:06, expires: 22:50:53, via map-reply, complete, local-to-site
            m = p3.match(line)
            if m:
                group = m.groupdict()
                eid_prefix = group.pop('eid_prefix')
                eid_prefix_dict = lisp_id_dict.setdefault('eid_prefix', {})\
                                              .setdefault(eid_prefix, {})
                eid_prefix_dict.update(
                    {k:v for k, v in group.items() if v is not None}
                )
                continue

            # Sources: map-reply
            m = p4.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict.update({'source_type': group['source_type']})
                continue
            
            # State: complete, last modified: 01:09:06, map-source: 1.1.1.10
            m = p5.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict.update({
                    'last_modified': group['last_modified'],
                    'source_ip': group['source_ip']
                })
                continue
            
            # Active, Packets out: 139(0 bytes), counters are not accurate (~ 00:00:01 ago)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict.update({'prefix_state': group['prefix_state']})
                continue

            # Encapsulating dynamic-EID traffic
            m = p7.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict.update({'encap': group['encap']})
                continue
            
            # 1.1.1.10  01:09:06  up      10/10        -
            m = p8.match(line)
            if m:
                group = m.groupdict()
                rloc_set = group.pop('rloc_set')
                rloc_set_dict = eid_prefix_dict.setdefault('rloc_set', {})\
                                               .setdefault(rloc_set, {})
                rloc_set_dict.update({
                    'uptime': group['uptime'],
                    'rloc_state': group['rloc_state'],
                    'priority': int(group['priority']),
                    'weight': int(group['weight']),
                    'encap_iid': group['encap_iid']
                })
                continue
            
            # Last up-down state change:         01:09:06, state change count: 1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                last_state_change_dict = rloc_set_dict.setdefault('last_state_change', {})
                last_state_change_dict.update({
                    'time': group['time'],
                    'count': int(group['count'])
                })
                continue

            # Last route reachability change:    01:09:06, state change count: 1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                last_route_reach_change_dict = rloc_set_dict.setdefault('last_route_reach_change', {})
                last_route_reach_change_dict.update({
                    'time': group['time'],
                    'count': int(group['count'])
                })
                continue
            
            # Last priority / weight change:     never/never
            m = p11.match(line)
            if m:
                group = m.groupdict()
                last_pri_weight_change_dict = rloc_set_dict.setdefault('last_pri_weight_change', {})
                last_pri_weight_change_dict.update({
                    'priority': group['priority'],
                    'weight': group['weight']
                })
                continue
            
            # Last RLOC-probe sent:            01:09:06 (rtt 1ms)
            m = p12.match(line)
            if m:
                group = m.groupdict()
                rloc_probe_sent_dict = rloc_set_dict.setdefault('rloc_probe_sent', {})
                rloc_probe_sent_dict.update({
                    'time': group['time'],
                    'rtt': int(group['rtt']),
                    'rtt_unit': group['rtt_unit']
                })
                continue

        return ret_dict


class ShowLispSessionCapabilityRLOCSchema(MetaParser):

    ''' Schema for
        * show lisp vrf {vrf} session capability {rloc}
    '''
    schema = {
        'vrf': {
            str: {
                'peer_address': str,
                'peer_port': int,
                'local_address': str,
                'local_port': int,
                'capability_exchange_complete': str,
                'capability_sent_bitmap': str,
                'capability_sent': ListOf(str),
                'capability_received_bitmap': str,
                'capability_received': ListOf(str),
                'rx_count': int,
                'err_count': int
                }
            }
        }


class ShowLispSessionCapabilityRLOC(ShowLispSessionCapabilityRLOCSchema):
    """Parser for show lisp vrf {vrf} session capability {rloc}"""
    cli_command = ['show lisp vrf {vrf} session capability {rloc}']

    def cli(self, vrf=None, rloc=None, output=None):
        if output is None:
            if vrf and rloc:
                output = self.device.execute(self.cli_command[0].format(vrf=vrf,rloc=rloc))
        ret_dict = {}

        # Output for router lisp vrf red
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+vrf\s+(?P<vrf>\S+)$")

        # Peer address:                 66.66.66.66:4342
        p2 = re.compile(r"^Peer\s+address:\s+(?P<peer_address>\d{1,3}\.\d{1,3}"
                        r"\.\d{1,3}\.\d{1,3}:(?P<peer_port>\d+))$")

        # Local address:                66.66.66.66:50383
        p3 = re.compile(r"^Local\s+address:\s+(?P<local_address>\d{1,3}\.\d{1,3}"
                        r"\.\d{1,3}\.\d{1,3}:(?P<local_port>\d+))$")

        # Capability Exchange Complete: Yes
        p4 = re.compile(r"^Capability\s+Exchange\s+Complete:\s+"
                        r"(?P<capability_exchange_complete>\S+)$")

        # Capability Sent:              0x000001FF
        p5 = re.compile(r"^Capability\s+Sent:\s+(?P<capability_sent_bitmap>\S+)$")

        # Publish-Subscribe Instance-ID
        p6 = re.compile(r"^(?P<capability_sent>Publish-Subscribe\s+Instance-ID)$")

        # Domain-Info
        p7 = re.compile(r"^(?P<Domain>Domain-Info)$")

        # Route-Tag
        p8 = re.compile(r"^(?P<route>Route-Tag)$")

        # SGT
        p9 = re.compile(r"^(?P<sgt>SGT)$")

        # Default-originate
        p10 = re.compile(r"^(?P<default>Default-originate)$")

        # Service-registration
        p11 = re.compile(r"^(?P<service>Service-registration)$")

        # Extranet-policy-propagation
        p12 = re.compile(r"^(?P<extranet>Extranet-policy-propagation)$")

        # Default-ETR Route-metric
        p13 = re.compile(r"^(?P<default_etr>Default-ETR Route-metric)$")

        # Unknown vendor type skip
        p14 = re.compile(r"^(?P<unknown>Unknown\s+vendor\s+type\s+skip)$")

        # Capability Received:              0x000001FF
        p15 = re.compile(r"^Capability\s+Received:\s+(?P<capability_received_bitmap>\S+)$")

        # Publish-Subscribe Instance-ID
        p16 = re.compile(r"^(?P<capability_received>Publish-Subscribe\s+Instance-ID)$")

        # Domain-Info
        p17 = re.compile(r"^(?P<Domain_received>Domain-Info)$")

        # Route-Tag
        p18 = re.compile(r"^(?P<route_received>Route-Tag)$")

        # SGT
        p19 = re.compile(r"^(?P<sgt_received>SGT)$")

        # Default-originate
        p20 = re.compile(r"^(?P<default_received>Default-originate)$")

        # Service-registration
        p21 = re.compile(r"^(?P<service_received>Service-registration)$")

        # Extranet-policy-propagation
        p22 = re.compile(r"^(?P<extranet_received>Extranet-policy-propagation)$")

        # Default-ETR Route-metric
        p23 = re.compile(r"^(?P<default_etr_received>Default-ETR Route-metric)$")

        # Unknown vendor type skip
        p24 = re.compile(r"^(?P<unknown_received>Unknown\s+vendor\s+type\s+skip)$")

        # Receive count:                1
        p25 = re.compile("^Receive\s+count:\s+(?P<rx_count>\d+)$")

        # Error count:                  0
        p26 = re.compile("^Error\s+count:\s+(?P<err_count>\d+)$")

        count1 = 0
        count2 = 0
        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp vrf red
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                vrf = groups['vrf']
                vrf_dict = ret_dict.setdefault('vrf',{})\
                                   .setdefault(vrf,{})
                continue

            if not m and "vrf" not in ret_dict and vrf != "*":
                vrf = vrf
                vrf_dict = ret_dict.setdefault('vrf',{})\
                                   .setdefault(vrf,{})
                continue

            # Peer address:                 66.66.66.66:4342
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                peer_address = groups['peer_address']
                peer_port = int(groups['peer_port'])
                vrf_dict.update({'peer_address':peer_address})
                vrf_dict.update({'peer_port':peer_port})
                continue

            # Local address:                66.66.66.66:50383
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                local_address = groups['local_address']
                local_port = int(groups['local_port'])
                vrf_dict.update({'local_address':local_address})
                vrf_dict.update({'local_port':local_port})
                continue

            # Capability Exchange Complete: Yes
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                capability_exchange_complete = groups['capability_exchange_complete']
                vrf_dict.update({'capability_exchange_complete':capability_exchange_complete})
                continue

            # Capability Sent:              0x000001FF
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                capability_sent_bitmap = groups['capability_sent_bitmap']
                vrf_dict.update({'capability_sent_bitmap':capability_sent_bitmap})
                continue

            # Publish-Subscribe Instance-ID
            m = p6.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                capability_sent = groups['capability_sent']
                capability_sent_list = vrf_dict.setdefault('capability_sent', [])
                capability_sent_list.append(capability_sent)
                continue

            # Domain-Info
            m = p7.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                Domain = groups['Domain']
                capability_sent_list.append(Domain)
                continue

            # Route-Tag
            m = p8.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                route = groups['route']
                capability_sent_list.append(route)
                continue

            # SGT
            m = p9.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                sgt = groups['sgt']
                capability_sent_list.append(sgt)
                continue

            # Default-originate
            m = p10.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                default = groups['default']
                capability_sent_list.append(default)
                continue

            # Service-registration
            m = p11.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                service = groups['service']
                capability_sent_list.append(service)
                continue

            # Extranet-policy-propagation
            m = p12.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                extranet = groups['extranet']
                capability_sent_list.append(extranet)
                continue

            # Default-ETR Route-metric
            m = p13.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                default_etr = groups['default_etr']
                capability_sent_list.append(default_etr)
                continue

            # Unknown vendor type skip
            m = p14.match(line)
            if m and count1 <= count2:
                groups = m.groupdict()
                unknown = groups['unknown']
                capability_sent_list.append(unknown)
                count1 += 1
                continue

            # Capability Received:              0x000001FF
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                capability_received_bitmap = groups['capability_received_bitmap']
                vrf_dict.update({'capability_received_bitmap':capability_received_bitmap})
                continue

            # Publish-Subscribe Instance-ID
            m = p16.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                capability_received = groups['capability_received']
                capability_received_list = vrf_dict.setdefault('capability_received', [])
                capability_received_list.append(capability_received)
                continue

            # Domain-Info
            m = p17.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                Domain_received = groups['Domain_received']
                capability_received_list.append(Domain_received)
                continue

            # Route-Tag
            m = p18.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                route_received = groups['route_received']
                capability_received_list.append(route_received)
                continue

            # SGT
            m = p19.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                sgt_received = groups['sgt_received']
                capability_received_list.append(sgt_received)
                continue

            # Default-originate
            m = p20.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                default_received = groups['default_received']
                capability_received_list.append(default_received)
                continue

            # Service-registration
            m = p21.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                service_received = groups['service_received']
                capability_received_list.append(service_received)
                continue

            # Extranet-policy-propagation
            m = p22.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                extranet_received = groups['extranet_received']
                capability_received_list.append(extranet_received)
                continue

            # Default-ETR Route-metric
            m = p23.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                default_etr_received = groups['default_etr_received']
                capability_received_list.append(default_etr_received)
                continue

            # Unknown vendor type skip
            m = p24.match(line)
            if m and count1 >= count2:
                groups = m.groupdict()
                unknown_received = groups['unknown_received']
                capability_received_list.append(unknown_received)
                count2 += 1
                continue

            # Receive count:                1
            m = p25.match(line)
            if m:
                groups = m.groupdict()
                rx_count = int(groups['rx_count'])
                vrf_dict.update({'rx_count':rx_count})
                continue

            # Error count:                  0
            m = p26.match(line)
            if m:
                groups = m.groupdict()
                err_count = int(groups['err_count'])
                vrf_dict.update({'err_count':err_count})
                continue
        return ret_dict


# ==========================================
# Parser for: show lisp {lisp_id} redundancy
# ==========================================
class ShowLispRedundancySchema(MetaParser):
    schema = {
        'lisp_id': {
            int: { # LISP ID
                'rp': str,
                'sso': str,
                'checkpoint_connection': str,
                'peer_redundancy_state': str,
                'number_of_bulk_sync_started': int,
                'last_bulk_sync_started': str,
                'last_bulk_sync_finished': str,
                'last_sync_lost': str,
                'queued_checkpoint_requests': int,
                'unack_checkpoint_requests': int,
                'max_checkpoint_requests': int,
            }
        }
    }


class ShowLispRedundancy(ShowLispRedundancySchema):
    cli_command = ['show lisp {lisp_id} redundancy',
                   'show lisp redundancy',
                   'show lisp locator-table {locator_table} redundancy']

    def cli(self, lisp_id=None, locator_table=None, output=None):
        if output is None:
            if lisp_id:
                cmd = self.cli_command[0].format(lisp_id=lisp_id)
            elif locator_table:
                cmd = self.cli_command[2].format(locator_table=locator_table)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        lisp_dict = {}

        #Redundancy for LISP 0
        p1 = re.compile(r"^Redundancy\s+for\s+LISP\s+(?P<lisp_id>\d+)$")

        #  Active RP
        #  Standby RP
        p2 = re.compile(r"^(?P<rp>Active|Standby)\s+RP$")

        #  SSO enabled
        #  SSO disabled
        p3 = re.compile(r"^SSO\s+(?P<sso>enabled|disabled)$")

        #  Checkpoint connection open
        #  Checkpoint connection closed
        p4 = re.compile(r"^Checkpoint\s+connection\s+(?P<checkpoint_connection>open|closed)$")

        #  Peer redundancy state: synchronized
        #  Peer redundancy state: unsynchronized
        p5 = re.compile(r"^Peer\s+redundancy\s+state:\s+(?P<peer_redundancy_state>synchronized|unsynchronized)$")

        #  Number of Bulk Syncs started: 1
        p6 = re.compile(r"^Number\s+of\s+Bulk\s+Syncs\s+started:\s+(?P<number_of_bulk_sync_started>\d+)$")

        #  Last Bulk Sync started: never
        #  Last Bulk Sync started: Jan 23 15:55:26.712 PST
        p7 = re.compile(r"^Last\s+Bulk\s+Sync\s+started:\s+(?P<last_bulk_sync_started>[\w:\s+\.]+)$")

        #  Last Bulk Sync finished: never
        #  Last Bulk Sync finished: Jan 23 15:55:26.712 PST
        p8 = re.compile(r"^Last\s+Bulk\s+Sync\s+finished:\s+(?P<last_bulk_sync_finished>[\w:\s+\.]+)$")

        #  Last time synchronization was lost: never
        #  Last time synchronization was lost: Jan 23 15:55:26.712 PST
        p9 = re.compile(r"^Last\s+time\s+synchronization\s+was\s+lost:\s+(?P<last_sync_lost>[\w\s+\d:\.]+)$")

        #  Queued/max checkpoint requests: 0/17
        p10 = re.compile(r"^Queued\/max\s+checkpoint\s+requests:\s+(?P<queued_checkpoint_requests>\d+)\/(?P<max_checkpoint_requests>\d+)$")

        #  Unacknowledged/max checkpoint requests: 0/17
        p11 = re.compile(r"^Unacknowledged\/max\s+checkpoint\s+requests:\s+(?P<unack_checkpoint_requests>\d+)\/\d+$")

        for line in output.splitlines():
            line = line.strip()

            #Redundancy for LISP 0
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])

                lisp_id_dict = lisp_dict.setdefault('lisp_id', {}) \
                                        .setdefault(lisp_id, {})
                continue

            #  Active RP
            #  Standby RP
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['rp'] = groups['rp']
                continue

            #  SSO enabled
            #  SSO disabled
            m=p3.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['sso'] = groups['sso']
                continue

            #  Checkpoint connection open
            #  Checkpoint connection closed
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['checkpoint_connection'] = groups['checkpoint_connection']
                continue

            #  Peer redundancy state: synchronized
            #  Peer redundancy state: unsynchronized
            m=p5.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['peer_redundancy_state'] = groups['peer_redundancy_state']
                continue

            #  Number of Bulk Syncs started: 1
            m=p6.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['number_of_bulk_sync_started'] = int(groups['number_of_bulk_sync_started'])
                continue

            #  Last Bulk Sync started: never
            #  Last Bulk Sync started: Jan 23 15:55:26.712 PST
            m=p7.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['last_bulk_sync_started'] = groups['last_bulk_sync_started']
                continue

            #  Last Bulk Sync finished: never
            #  Last Bulk Sync finished: Jan 23 15:55:26.712 PST
            m=p8.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['last_bulk_sync_finished'] = groups['last_bulk_sync_finished']
                continue

            #  Last time synchronization was lost: never
            #  Last time synchronization was lost: Jan 23 15:55:26.712 PST
            m=p9.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['last_sync_lost'] = groups['last_sync_lost']
                continue

            #  Queued/max checkpoint requests: 0/17
            m=p10.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['queued_checkpoint_requests'] = int(groups['queued_checkpoint_requests'])
                lisp_id_dict['max_checkpoint_requests'] = int(groups['max_checkpoint_requests'])
                continue

            #  Unacknowledged/max checkpoint requests: 0/17
            m=p11.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['unack_checkpoint_requests'] = int(groups['unack_checkpoint_requests'])
                continue

        return lisp_dict


class ShowLispEthernetMapCacheSchema(MetaParser):

    ''' Schema for
        * 'show lisp instance-id <instance_id> ethernet map-cache'
        * 'show lisp <lisp_id> instance-id <instance_id> ethernet map-cache'
        * 'show lisp eid-table vlan <vlan> ethernet map-cache'
        * 'show lisp locator-table <vrf> ethernet map-cache'''
    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'eid_table': str,
                        'entries': int,
                        'eid_prefix': {
                            str: {
                                'uptime': str,
                                'expiry_time': str,
                                'via': str,
                                'map_reply_state': str,
                                'site': str,
                                'locators': {
                                    str: {
                                        'uptime': str,
                                        'rloc_state': str,
                                        'priority': int,
                                        'weight': int,
                                        'encap_iid': str
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispEthernetMapCache(ShowLispEthernetMapCacheSchema):
    """Parser for
    * 'show lisp instance-id <instance_id> ethernet map-cache'
    * 'show lisp <lisp_id> instance-id <instance_id> ethernet map-cache'
    * 'show lisp eid-table vlan <vlan> ethernet map-cache'
    * 'show lisp locator-table <vrf> ethernet map-cache'"""
    cli_command = ['show lisp locator-table {vrf} instance-id {instance_id} ethernet map-cache',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet map-cache',
                   'show lisp instance-id {instance_id} ethernet map-cache'
                   #'show lisp eid-table vlan {vlan} ethernet map-cache',
                   ]

    def cli(self, lisp_id=None, instance_id=None, vlan=None, vrf=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id,instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            elif vrf:
                output = self.device.execute(self.cli_command[0].format(vrf=vrf,instance_id=instance_id))
            #else:
            #    output = self.device.execute(self.cli_command[3].format(vlan=vlan))
        ret_dict = {}

        #Output for router lisp 0 instance-id 8188
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)"
                        r"\s+instance-id\s+(?P<instance_id>\d+)$")

        #LISP MAC Mapping Cache for EID-table Vlan 210 (IID 8188), 1 entries
        # LISP MAC Mapping Cache for LISP 0 EID-table Vlan 101 (IID 1023), 2 entries
        p2 = re.compile(r"^LISP\s+MAC\s+Mapping\s+Cache\s+for(\s+LISP\s+\d+)?\s+EID-table\s+"
                        r"(?P<eid_table>Vlan\s+\d+)\s+\(IID\s+\d+\),\s+(?P<entries>\d+)\s+entries$")

        #0017.0100.0001/48, uptime: 18:33:39, expires: 05:26:20, via map-reply, complete, local-to-site
        # aabb.cc00.cb00/48, uptime: 00:00:03, expires: never, via pub-sub, complete, local-to-site
        p3 = re.compile(r"^(?P<eid_prefix>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{1,2}),"
                        r"\s+uptime:\s+(?P<uptime>\d{1,2}:\d{1,2}:\d{1,2}),\s+expires:\s+"
                        r"(?P<expiry_time>\d{1,2}:\d{1,2}:\d{1,2}|\S+),\s+via\s+(?P<via>\S+),\s+"
                        r"(?P<map_reply_state>\S+),\s+(?P<site>\S+)$")

        #  1.1.1.10  18:33:39  up      10/10        -
        p4 = re.compile(r"^(?P<locators>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
                        r"(?P<uptime>\d{1,2}:\d{1,2}:\d{1,2})\s+(?P<rloc_state>\S+)"
                        r"\s+(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<encap_iid>\S+)$")
        for line in output.splitlines():
            line = line.strip()
            #Output for router lisp 0 instance-id 8188
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})
                instance_id_dict = ret_dict.setdefault('instance_id',{})\
                                           .setdefault(instance_id,{})
                continue

            #LISP MAC Mapping Cache for EID-table Vlan 210 (IID 8188), 1 entries
            m = p2.match(line)
            if m:
                if "lisp_id" and "instance_id" not in ret_dict:
                    if lisp_id and instance_id:
                        lisp_id = int(lisp_id)
                        lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                               .setdefault(lisp_id,{})
                        instance_id = int(instance_id)
                        instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                                       .setdefault(instance_id,{})
                    elif not lisp_id and instance_id:
                        lisp_id = 0
                        lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                               .setdefault(lisp_id,{})
                        instance_id = int(instance_id)
                        instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                                       .setdefault(instance_id,{})
                groups = m.groupdict()
                eid_table = groups['eid_table']
                entries = int(groups['entries'])
                instance_id_dict.update({'eid_table':eid_table,'entries':entries})

            #0017.0100.0001/48, uptime: 18:33:39, expires: 05:26:20, via map-reply, complete, local-to-site
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                eid_prefix = groups['eid_prefix']
                uptime = groups['uptime']
                expiry_time = groups['expiry_time']
                via = groups['via']
                map_reply_state = groups['map_reply_state']
                site = groups['site']
                eid_prefix_dict = instance_id_dict.setdefault('eid_prefix',{})\
                                                  .setdefault(eid_prefix,{})
                eid_prefix_dict.update({
                    'uptime':uptime,
                    'expiry_time':expiry_time,
                    'via':via,
                    'map_reply_state':map_reply_state,
                    'site':site
                })

            #  1.1.1.10  18:33:39  up      10/10        -
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                locators = groups['locators']
                uptime = groups['uptime']
                rloc_state = groups['rloc_state']
                priority = int(groups['priority'])
                weight = int(groups['weight'])
                encap_iid = groups['encap_iid']
                rloc_set_dict = eid_prefix_dict.setdefault('locators',{})\
                                               .setdefault(locators,{})
                rloc_set_dict.update({
                    'uptime':uptime,
                    'rloc_state':rloc_state,
                    'priority':priority,
                    'weight':weight,
                    'encap_iid':encap_iid
                })
        return ret_dict


class ShowLispEthernetDatabaseSchema(MetaParser):

    ''' Schema for
        * show lisp instance-id <instance_id> ethernet database 
        * show lisp <lisp_id> instance-id <instance_id> ethernet database 
        * show lisp eid-table vlan <vlan> ethernet database
        * show lisp locator-table <locator_table> instance_id <instance_id> ethernet database
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'eid_table': str,
                        'lsb': str,
                        'entries': int,
                        'no_route': int,
                        'inactive': int,
                        'do_not_reg': int,
                        'eid_prefix': {
                            str: {
                                Optional('dyn_eid_name') : str,
                                Optional('do_not_reg_flag'): bool,
                                'loc_set': str,
                                'uptime': str,
                                'last_change_time': str,
                                'domain_id': str,
                                Optional('serv_ins_type'): str,
                                Optional('serv_ins_id'): int,
                                Optional('locators'): {
                                    str: {
                                        'priority': int,
                                        'weight': int,
                                        'src': str,
                                        'state': str
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispEthernetDatabase(ShowLispEthernetDatabaseSchema):
    ''' Parser for
        * show lisp instance-id <instance_id> ethernet database 
        * show lisp <lisp_id> instance-id <instance_id> ethernet database 
        * show lisp eid-table vlan <vlan> ethernet database
        * show lisp locator-table <locator_table> instance_id <instance_id> ethernet database
    '''
    cli_command = ['show lisp instance-id {instance_id} ethernet database',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet database',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ethernet database'
                   # this will be uncommented after command's output is enhanced for instance-id
                   #'show lisp eid-table vlan <vlan> ethernet database'
                   ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vlan=None, vrf=None, locator_table=None):
        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].format(locator_table=locator_table, instance_id=instance_id))
            else:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id))
        ret_dict = {}

        #LISP ETR MAC Mapping Database for LISP 0 EID-table Vlan 101 (IID 101), LSBs: 0x1
        p1 = re.compile(r"^LISP\s+ETR\s+MAC\s+Mapping\s+Database\s+for\s+LISP\s+"
                        r"(?P<lisp_id>\d+)\s+EID-table\s+(?P<eid_table>Vlan\s+\d+)"
                        r"\s+\(IID\s+(?P<instance_id>\d+)\),\s+LSBs:\s+(?P<lsb>\S+)$")

        #Entries total 3, no-route 0, inactive 0, do-not-register 1
        p2 = re.compile(r"^Entries\s+total\s+(?P<entries>\d+),\s+no-route\s+(?P<no_route>\d+),"
                        r"\s+inactive\s+(?P<inactive>\d+),\s+do-not-register (?P<do_not_reg>\d+)$")

        #0000.0c9f.f98b/48, dynamic-eid Auto-L2-group-8188, do not register, inherited from default locator-set rloc_71d5dfee-bf02-4e45-9e5e-079ef3c09407
        p3 = re.compile(r"^(?P<eid_prefix>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d+),\s+dynamic-eid\s+"
                        r"(?P<dyn_eid_name>\S+),(?P<do_not_reg_flag>.*)\s+inherited\s+from\s+default"
                        r"\s+locator-set\s+(?P<loc_set>\S+)$")

        #Uptime: 1d21h, Last-change: 1d21h
        p4 = re.compile(r"^Uptime:\s+(?P<uptime>\S+),\s+Last-change:\s+(?P<last_change_time>\S+)$")

        #Domain-ID: unset
        p5 = re.compile(r"^Domain-ID:\s+(?P<domain_id>\S+)$")

        #Service-Insertion: N/A (0)
        p6 = re.compile(r"^Service-Insertion:\s+(?P<serv_ins_type>\S+)"
                        r"\s+\((?P<serv_ins_id>\d+)\)$")

        #1.1.1.10   10/10   cfg-intf   site-self, reachable
        p7 = re.compile(r"^(?P<locators>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
                        r"(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<src>\S+)\s+"
                        r"(?P<state>\S+\W+\S+)")

        for line in output.splitlines():
            line = line.strip()

            # LISP ETR MAC Mapping Database for LISP 0 EID-table Vlan 101 (IID 101), LSBs: 0x1
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})
                instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                               .setdefault(instance_id,{})
                eid_table = groups['eid_table']
                lsb = groups['lsb']
                instance_id_dict.update({'eid_table':eid_table,'lsb':lsb})

            #Entries total 3, no-route 0, inactive 0, do-not-register 1
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict.update({
                    'entries':int(groups['entries']),
                    'no_route':int(groups['no_route']),
                    'inactive':int(groups['inactive']),
                    'do_not_reg':int(groups['do_not_reg'])
                    })

            #0000.0c9f.f98b/48, dynamic-eid Auto-L2-group-8188, do not register, inherited from default locator-set rloc_71d5dfee-bf02-4e45-9e5e-079ef3c09407
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                eid_prefix = groups['eid_prefix']
                dyn_eid_name = groups['dyn_eid_name']
                do_not_reg = groups['do_not_reg_flag']
                do_not_reg_flag = bool(re.search("do not register",do_not_reg))
                loc_set = groups['loc_set']
                eid_prefix_dict = instance_id_dict.setdefault('eid_prefix',{})\
                                                  .setdefault(eid_prefix,{})
                eid_prefix_dict.update({
                    'dyn_eid_name':dyn_eid_name,
                    'do_not_reg_flag':do_not_reg_flag,
                    'loc_set':loc_set
                    })

            #Uptime: 1d21h, Last-change: 1d21h
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                uptime = groups['uptime']
                last_change_time = groups['last_change_time']
                eid_prefix_dict.update({
                    'uptime':uptime,
                    'last_change_time':last_change_time
                })

            #Domain-ID: unset
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                domain_id = groups['domain_id']
                eid_prefix_dict.update({'domain_id':domain_id})

            #Service-Insertion: N/A (0)
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                serv_ins_type = groups['serv_ins_type']
                serv_ins_id = int(groups['serv_ins_id'])
                eid_prefix_dict.update({'serv_ins_type':serv_ins_type,
                                        'serv_ins_id':serv_ins_id})

            #1.1.1.10   10/10   cfg-intf   site-self, reachable
            m = p7.match(line)
            if m:	
                groups = m.groupdict()
                locators = groups['locators']
                priority = int(groups['priority'])
                weight = int(groups['weight'])
                src = groups['src']
                state = groups['state']
                rloc_set_dict = eid_prefix_dict.setdefault('locators',{})\
                                           .setdefault(locators,{})
                rloc_set_dict.update({
                    'priority':priority,
                    'weight':weight,
                    'src':src,
                    'state':state
                    })
        return ret_dict


# ==========================================
# Parser for: show lisp {lisp_id} instance-id
# {instance_id} {address_family} eid-watch
# ==========================================
class ShowLispEidWatchSchema(MetaParser):
    schema = {
        'lisp_id': {
            int: { # lisp id
                Optional('instance_id'): {
                    Optional(int): { # instance id
                        'client_name': str,
                        'process_id': int,
                        'connection_to_control_process': str,
                        'ipc_endpoint': int,
                        'client_notifications': str,
                        'address_family': str,
                        'eid_table': str,
                        'entry_count': int,
                        'prefix': str,
                        'watched_entries': ListOf(str)
                    }
                }
            }
        }
    }


class ShowLispEidWatch(ShowLispEidWatchSchema):
    cli_command = ['show lisp {lisp_id} instance-id {instance_id} {address_family} eid-watch',
                   'show lisp instance-id {instance_id} {address_family} eid-watch',
                   'show lisp locator-table {locator_table} instance-id {instance_id} {address_family} eid-watch',
                   'show lisp eid-table {eid_table} {address_family} eid-watch',
                   'show lisp eid-table vlan {vlan_id} ethernet eid-watch']

    def cli(self, lisp_id=None, instance_id=None, address_family=None, locator_table=None, eid_table=None, vlan_id=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                cmd = self.cli_command[0].format(lisp_id=lisp_id, instance_id=instance_id, address_family=address_family)
            elif locator_table and instance_id:
                cmd = self.cli_command[2].format(locator_table=locator_table, instance_id=instance_id, address_family=address_family)
            elif eid_table:
                cmd = self.cli_command[4].format(eid_table=eid_table, address_family=address_family)
            elif vlan_id:
                cmd = self.cli_command[6].format(vlan_id=vlan_id)
            else:
                cmd = self.cli_command[1].format(instance_id=instance_id, address_family=address_family)
            output = self.device.execute(cmd)

        lisp_dict = {}

        #LISP EID watch information for router 0
        p1 = re.compile(r"^LISP\sEID\swatch\sinformation\sfor\srouter\s+(?P<lisp_id>\d+)$")

        #Client : Test 0
        p2 = re.compile(r"^Client\s+:\s+(?P<client_name>.+)$")

        #Process ID : 87
        p3 = re.compile(r"^Process\sID\s+:\s+(?P<process_id>\d+)$")

        #Connection to LISP control process : ENABLED
        p4 = re.compile(r"^Connection\sto\sLISP\scontrol\sprocess\s+:\s+(?P<connection_to_control_process>.+)$")

        #IPC end point : 1
        p5 = re.compile(r"^IPC\send\spoint\s+:\s+(?P<ipc_endpoint>\d+)$")

        #Client notifications : Delivered
        p6 = re.compile(r"^Client\snotifications\s+:\s+(?P<client_notifications>.+)$")

        #LISP IPv4 EID Watches for Table (RLOC mapping in vrf default IPv4) IID (101), 1 watch entries
        #LISP invalid EID Watches for Table (AR mapping in Vlan 100) IID (103), 1 watch entries
        p7 = re.compile(r"^LISP\s+(?P<address_family>[A-Za-z0-9]+)\sEID\sWatches\sfor\sTable\s+\((RLOC|AR)\smapping\sin\s+(?P<eid_table>(vrf\s+\w+)|(Vlan\s+\d+))(\s+)?(IPv4|IPv6)?\)\sIID\s+\((?P<instance_id>\d+)\),\s+(?P<entry_count>\d+)\swatch\sentries$")

        #  Watch entries for prefix 0.0.0.0/0
        #  Watch entries for prefix ::/0
        #  Watch entries for prefix 0000.0000.0000/0
        p8 = re.compile(r"^Watch\sentries\sfor\sprefix\s+(?P<prefix>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})|([a-fA-F\d\:]+\/\d{1,3})|(([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{1,2}))$")

        #   1.1.1.1
        #   E80::AEDE:48FF:FE00:1111
        #   f100.a551.0501
        p9 = re.compile(r"^(?P<watched_entry>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|(([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})|([a-fA-F\d\:]+))")

        for line in output.splitlines():
            line = line.strip()
           #LISP EID watch information for router 0
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                if groups['lisp_id']:
                    lisp_id = int(groups['lisp_id'])
                else:
                    lisp_id = 0

                instance_id_container = lisp_dict.setdefault('lisp_id', {}) \
                                                 .setdefault(lisp_id, {})
                instance_id_dict = instance_id_container.setdefault('instance_id', {})
                
                # At this point we don't know instance_id yet
                dummy_instance_id_dict = instance_id_dict.setdefault('dummy_instance_id', {})
                continue

            #Client : Test 0
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                dummy_instance_id_dict['client_name'] = groups['client_name']
                continue

            #Process ID : 87
            m=p3.match(line)
            if m:
                groups = m.groupdict()
                dummy_instance_id_dict['process_id'] = int(groups['process_id'])
                continue

            #Connection to LISP control process : ENABLED
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                dummy_instance_id_dict['connection_to_control_process'] = groups['connection_to_control_process']
                continue

            #IPC end point : 1
            m=p5.match(line)
            if m:
                groups = m.groupdict()
                dummy_instance_id_dict['ipc_endpoint'] = int(groups['ipc_endpoint'])
                continue

            #Client notifications : Delivered
            m=p6.match(line)
            if m:
                groups = m.groupdict()
                dummy_instance_id_dict['client_notifications'] = groups['client_notifications']
                continue

            #LISP IPv4 EID Watches for Table (RLOC mapping in vrf default IPv4) IID (101), 1 watch entries
            #LISP invalid EID Watches for Table (AR mapping in Vlan 100) IID (103), 1 watch entries
            m=p7.match(line)
            if m:
                groups = m.groupdict()
                instance_id = int(groups['instance_id'])

                instance_id_dict[instance_id] = instance_id_dict.pop('dummy_instance_id')
                instance_id_dict[instance_id]['address_family'] = groups['address_family']
                instance_id_dict[instance_id]['eid_table'] = groups['eid_table']
                instance_id_dict[instance_id]['entry_count'] = int(groups['entry_count'])
                continue

            #  Watch entries for prefix 0.0.0.0/0
            #  Watch entries for prefix ::/0
            #  Watch entries for prefix 0000.0000.0000/0
            m=p8.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict[instance_id]['prefix'] = groups['prefix']
                continue

            #   1.1.1.1
            #   E80::AEDE:48FF:FE00:1111
            #   f100.a551.0501
            m=p9.match(line)
            if m:
                groups = m.groupdict()
                watched_entries = instance_id_dict[instance_id].setdefault('watched_entries', [])
                watched_entries.append(groups['watched_entry'])
                continue

        # Post processing in case the output does not have instance id
        if lisp_dict == {}:
            return {}

        lisp_ids_to_delete = []
        for lisp_id, lisp_id_dict in lisp_dict['lisp_id'].items():
            for instance_id, instance_id_dict in lisp_id_dict['instance_id'].items():
                if instance_id == 'dummy_instance_id':
                    lisp_ids_to_delete.append(lisp_id)
                    break

        for id in lisp_ids_to_delete:
            del lisp_dict['lisp_id'][id]['instance_id']['dummy_instance_id']

        return lisp_dict


class ShowLispInstanceIdForwardingStateSchema(MetaParser):

    ''' Schema for
        * show ip lisp instance-id {instance_id} forwarding state
        * show ipv6 lisp instance-id {instance_id} forwarding state
        * show lisp instance-id {instance_id} {service} forwarding state
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'lisp_virtual_intf': str,
                        'user': str,
                        'eid_vrf': {
                            str: {
                                'address_family': { # IPv4|IPv6|L2
                                    str: {
                                        Optional('configured_roles'): ListOf(str),
                                        Optional('eid_table'): str,
                                        Optional('alt_table'): str,
                                        Optional('locator_status_bit'): str,
                                        Optional('nonce'): str,
                                        Optional('ttl_propagation'): str,
                                        Optional('table_supression'): str,
                                        Optional('sgt_policy_fwd'): str,
                                        Optional('l2_domain_id'): int,
                                        Optional('ipv4_unnum_if'): str,
                                        Optional('ipv6_unnum_if'): str
                                        }
                                    },
                                'rloc_transport': {
                                    'vrf': str,
                                    'ipv4_rloc_table': str,
                                    'ipv6_rloc_table': str,
                                    'ipv4_path_mtu_discovery': {
                                        'min': int,
                                        'max': int
                                        },
                                    'ipv6_path_mtu_discovery': {
                                        'min': int,
                                        'max': int
                                        },
                                    'ipv4_rloc_fltr_handle': str,
                                    'ipv6_rloc_fltr_handle': str
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispInstanceIdForwardingState(ShowLispInstanceIdForwardingStateSchema):
    ''' Parser for
        * show ip lisp instance-id {instance_id} forwarding state
        * show ipv6 lisp instance-id {instance_id} forwarding state
        * show lisp instance-id {instance_id} {service} forwarding state

    '''
    cli_command = ['show ip lisp instance-id {instance_id} forwarding state',
                   'show ipv6 lisp instance-id {instance_id} forwarding state',
                   'show lisp instance-id {instance_id} {service} forwarding state']

    def cli(self, instance_id, output=None, service=None):
        if output is None:
            if instance_id and service:
                output = self.device.execute(self.cli_command[2].format(instance_id = instance_id,service = service))
            if instance_id:
                if "ipv6" in self.cli_command:
                    output = self.device.execute(self.cli_command[1].format(instance_id = instance_id))
                else:
                    output = self.device.execute(self.cli_command[0].format(instance_id = instance_id))
        ret_dict = {}

        # EID VRF                      red (0x2)
        p1 = re.compile(r"^EID\s+VRF\s+(?P<eid_vrf>\S+\s+\S+)$")

        # IPv4
        p2 = re.compile(r"^(?P<address_family>IPv4|IPv6|L2)$")

        # Configured roles         ETR|PITR
        p3 = re.compile(r"^Configured\s+roles\s+(?P<configured_roles>\S+)$")

        # EID table                IPv4:red
        p4 = re.compile(r"^EID\s+table\s+(?P<eid_table>\S+)$")

        # ALT table                <null>
        p5 = re.compile(r"^ALT\s+table\s+(?P<alt_table>\S+)$")

        # Locator status bits      Disabled
        p6 = re.compile(r"^Locator\s+status\s+bits\s+(?P<locator_status_bit>Disabled|Enabled)$")

        # Nonce                    N/A
        p7 = re.compile(r"^Nonce\s+(?P<nonce>\S+)$")

        # TTL Propagation          Enabled
        p8 = re.compile(r"^TTL\s+Propagation\s+(?P<ttl_propagation>Disabled|Enabled)$")

        # Table Suppression        Disabled
        p9 = re.compile(r"^Table\s+Suppression\s+(?P<table_supression>Disabled|Enabled)$")

        # SGT Policy Fwd           Disabled
        p10 = re.compile(r"^SGT\s+Policy\s+Fwd\s+(?P<sgt_policy_fwd>Disabled|Enabled)$")

        # L2 Domain ID             0
        p11 = re.compile(r"^L2\s+Domain\s+ID\s+(?P<l2_domain_id>\d+)$")

        # IPv4 Unnum I/F           N/A
        p12 = re.compile(r"^IPv4\s+Unnum\s+I\/F\s+(?P<ipv4_unnum_if>\S+)$")

        # IPv6 Unnum I/F           N/A
        p13 = re.compile(r"^IPv6\s+Unnum\s+I\/F\s+(?P<ipv6_unnum_if>\S+)$")

        # RLOC transport VRF         Default
        p14  = re.compile(r"^RLOC\s+transport\s+VRF\s+(?P<vrf>\S+)")

        # IPv4 RLOC table          IPv4:Default
        p15 = re.compile(r"^IPv4\s+RLOC\s+table\s+(?P<ipv4_rloc_table>\S+)")

        # IPv6 RLOC table          IPv6:Default
        p16 = re.compile(r"^IPv6\s+RLOC\s+table\s+(?P<ipv6_rloc_table>\S+)")

        # IPv4 path MTU discovery  min  576 max 65535
        # IPv6 path MTU discovery  min  1280 max 65535
        p17 = re.compile(r"^IPv(?P<ip_version>\d)\s+path\s+MTU\s+discovery\s+"
                         r"min\s+(?P<min>\d+)\s+max\s+(?P<max>\d+)$")

        # IPv4 RLOC fltr handle    0x0
        # IPv6 RLOC fltr handle    0x0
        p18 = re.compile(r"^IPv(?P<ip_version>\d)\s+RLOC\s+fltr\s+handle\s+"
                         r"(?P<rloc_fltr_handle>\S+)$")

        # LISP router ID             0
        p19 = re.compile(r"^LISP\s+router\s+ID\s+(?P<lisp_id>\d+)$")

        # LISP virtual interface     LISP0.4100
        p20 = re.compile(r"^LISP\s+virtual\s+interface\s+"
                         r"(?P<lisp_virtual_intf>\S+)$")

        # User                       LISP
        p21 = re.compile(r"^User\s+(?P<user>\S+)$")

        for line in output.splitlines():
            line = line.strip()

            # EID VRF                      red (0x2)
            m = p1.match(line)
            if m:
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(None,{})
                instance_id = int(instance_id)
                instance_id_dict = lisp_id_dict.setdefault('instance_id', {}).setdefault(instance_id, {})
                groups = m.groupdict()
                eid_vrf = groups['eid_vrf']
                instance_id_dict.setdefault('lisp_virtual_intf')
                instance_id_dict.setdefault('user')
                eid_dict = instance_id_dict.setdefault('eid_vrf', {}).setdefault(eid_vrf, {})
                continue

            # IPv4
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                address_family = groups['address_family']
                af_dict = eid_dict.setdefault('address_family', {}).setdefault(address_family, {})
                continue

            # Configured roles         ETR|PITR
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                configured_role = groups['configured_roles']
                configured_roles = configured_role.split("|")
                af_dict.update({'configured_roles':configured_roles})
                continue

            # EID table                IPv4:red
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                eid_table = groups['eid_table']
                af_dict.update({'eid_table':eid_table})
                continue

            # ALT table                <null>
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                alt_table = groups['alt_table']
                af_dict.update({'alt_table':alt_table})
                continue

            # Locator status bits      Disabled
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                locator_status_bit = groups['locator_status_bit']
                af_dict.update({'locator_status_bit':locator_status_bit})
                continue

            # Nonce                    N/A
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                nonce = groups['nonce']
                af_dict.update({'nonce':nonce})
                continue

            # TTL Propagation          Enabled
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                ttl_propagation = groups['ttl_propagation']
                af_dict.update({'ttl_propagation':ttl_propagation})
                continue

            # Table Suppression        Disabled
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                table_supression = groups['table_supression']
                af_dict.update({'table_supression':table_supression})
                continue

            # SGT Policy Fwd           Disabled
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                sgt_policy_fwd = groups['sgt_policy_fwd']
                af_dict.update({'sgt_policy_fwd':sgt_policy_fwd})
                continue

            # L2 Domain ID             0
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                l2_domain_id = int(groups['l2_domain_id'])
                af_dict.update({'l2_domain_id':l2_domain_id})
                continue

            # IPv4 Unnum I/F           N/A
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                ipv4_unnum_if = groups['ipv4_unnum_if']
                af_dict.update({'ipv4_unnum_if':ipv4_unnum_if})
                continue

            # IPv6 Unnum I/F           N/A
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                ipv6_unnum_if = groups['ipv6_unnum_if']
                af_dict.update({'ipv6_unnum_if':ipv6_unnum_if})
                continue

            # RLOC transport VRF         Default
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                vrf = groups['vrf']
                rloc_dict = eid_dict.setdefault('rloc_transport', {})
                rloc_dict.update({'vrf':vrf})
                continue

            # IPv4 RLOC table          IPv4:Default
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                ipv4_rloc_table = groups['ipv4_rloc_table']
                rloc_dict.update({'ipv4_rloc_table':ipv4_rloc_table})
                continue

            # IPv6 RLOC table          IPv6:Default
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                ipv6_rloc_table = groups['ipv6_rloc_table']
                rloc_dict.update({'ipv6_rloc_table':ipv6_rloc_table})
                continue

            # IPv4 path MTU discovery  min  576 max 65535
            # IPv6 path MTU discovery  min  1280 max 65535
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                ip_version = int(groups['ip_version'])
                min = int(groups['min'])
                max = int(groups['max'])
                if ip_version == 4:
                    v4_mtu_dict = rloc_dict.setdefault('ipv4_path_mtu_discovery',{})
                    v4_mtu_dict.update({'min':min,'max':max})
                else:
                    v6_mtu_dict = rloc_dict.setdefault('ipv6_path_mtu_discovery',{})
                    v6_mtu_dict.update({'min':min,'max':max})
                continue

            # IPv4 RLOC fltr handle    0x0
            # IPv6 RLOC fltr handle    0x0
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                rloc_fltr_handle = groups['rloc_fltr_handle']
                ip_version = groups['ip_version']
                rloc_dict.update({f'ipv{ip_version}_rloc_fltr_handle': rloc_fltr_handle})
                continue

            # LISP router ID             0
            m = p19.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                ret_dict['lisp_id'][lisp_id] = ret_dict['lisp_id'].pop(None)
                continue

            # LISP virtual interface     LISP0.4100
            m = p20.match(line)
            if m:
                groups = m.groupdict()
                lisp_virtual_intf = groups['lisp_virtual_intf']
                instance_id_dict.update({'lisp_virtual_intf':lisp_virtual_intf})
                continue

            # User                       LISP
            m = p21.match(line)
            if m:
                groups = m.groupdict()
                user = groups['user']
                instance_id_dict.update({'user':user})
                continue
        return ret_dict


class ShowLispIAFServerSchema(MetaParser):

    ''' Schema for
        * show lisp instance-id {instance_id} {address_family} server summary
        * show lisp {lisp_id} instance-id {instance_id} {address_family} server summary
        * show lisp locator-table {locator_table} instance-id {instance_id} {address_family} server summary
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'site': {
                            str: {
                                'configured': int,
                                'registered': int,
                                'incons': int
                                }
                            },
                        'site_reg_limit': int,
                        'site_reg_count': int,
                        'configured_sites': int,
                        'registered_sites': int,
                        'sites_inconsistent_registrations': int,
                        'af': {
                            str: { # IPv4|IPv6|MAC
                                'configured_eid_prefixes': int,
                                'registered_eid_prefixes': int,
                                'instance_service_site_reg_limit': int,
                                'registration_history_size': int,
                                'registration_history_limit': int
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispIAFServer(ShowLispIAFServerSchema):
    ''' Parser for
        * show lisp instance-id {instance_id} {address_family} server summary
        * show lisp {lisp_id} instance-id {instance_id} {address_family} server summary
        * show lisp locator-table {locator_table} instance-id {instance_id} {address_family} server summary
    '''
    cli_command = ['show lisp instance-id {instance_id} {address_family} server summary',
                   'show lisp {lisp_id} instance-id {instance_id} {address_family} server summary',
                   'show lisp locator-table {locator_table} instance-id {instance_id} {address_family} server summary'
                   ]

    def cli(self, output=None, lisp_id=None, instance_id=None, address_family=None, locator_table=None):
        if output is None:
            if lisp_id and instance_id and address_family:
                output = self.device.execute(self.cli_command[1].format(
                        lisp_id=lisp_id,
                        instance_id=instance_id,
                        address_family=address_family))
            elif locator_table and instance_id and address_family:
                output = self.device.execute(self.cli_command[2].format(
                        locator_table=locator_table,
                        instance_id=instance_id,
                        address_family=address_family))
            else:
                output = self.device.execute(self.cli_command[0].format(
                        instance_id=instance_id,
                        address_family=address_family))
        ret_dict = {}

        # Output for router lisp 0 instance-id 4100
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)"
                        r"\s+instance-id\s+(?P<instance_id>\d+)$")

        # Shire                         1          0      0
        p2 = re.compile(r"^(?P<site>\S+)\s+(?P<configured>\d+)\s+"
                        r"(?P<registered>\d+)\s+(?P<incons>\d+)$")

        # Site-registration limit for router lisp 0:              0
        p3 = re.compile(r"^Site-registration\s+limit\s+for\s+"
                        r"router\s+lisp\s+\d+:\s+(?P<site_reg_limit>\d+)")

        # Site-registration count for router lisp 0:              6
        p4 = re.compile(r"^Site-registration\s+count\s+for\s+router\s+"
                        r"lisp\s+\d+:\s+(?P<site_reg_count>\d+)")

        # Number of configured sites:                             1
        p5 = re.compile(r"^Number\s+of\s+configured\s+sites:\s+(?P<configured_sites>\d+)")

        # Number of registered sites:                             0
        p6 = re.compile(r"^Number\s+of\s+registered\s+sites:\s+(?P<registered_sites>\d+)")

        # Sites with inconsistent registrations:                  0
        p7 = re.compile(r"^Sites\s+with\s+inconsistent\s+registrations:\s+"
                        r"(?P<sites_inconsistent_registrations>\d+)")

        # IPv4|IPv6|MAC
        p8 = re.compile(r"^(?P<af>IPv4|IPv6|MAC)$")

        # Number of configured EID prefixes:                    1
        p9 = re.compile(r"^Number\s+of\s+configured\s+EID\s+prefixes:\s+"
                        r"(?P<configured_eid_prefixes>\d+)$")

        # Number of registered EID prefixes:                    0
        p10 = re.compile(r"^Number\s+of\s+registered\s+EID\s+prefixes:\s+"
                         r"(?P<registered_eid_prefixes>\d+)$")

        # Instance-Service site-registration limit:             0
        p11 = re.compile(r"^Instance-Service\s+site-registration\s+limit:\s+"
                         r"(?P<instance_service_site_reg_limit>\d+)$")

        # Registration-history size/limit:                      0/1000
        p12 = re.compile(r"^Registration-history\s+size\/limit:\s+"
                         r"(?P<registration_history_size>\d+)\/(?P<registration_history_limit>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0 instance-id 4100
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})
                instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                               .setdefault(instance_id,{})
                continue

            # Shire                         1          0      0
            m = p2.match(line)
            if m:
                lisp_id = int(lisp_id) if lisp_id else 0
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                instance_id = int(instance_id)
                instance_id_dict = lisp_id_dict.setdefault('instance_id', {}).setdefault(instance_id, {})
                groups = m.groupdict()
                site = groups['site']
                configured = int(groups['configured'])
                registered = int(groups['registered'])
                incons = int(groups['incons'])
                site_dict = instance_id_dict.setdefault('site',{})\
                                            .setdefault(site,{})
                site_dict.update({'configured':configured,'registered':registered,
                                  'incons':incons})

            # Site-registration limit for router lisp 0:              0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                site_reg_limit = int(groups['site_reg_limit'])
                instance_id_dict.update({'site_reg_limit':site_reg_limit})

            # Site-registration count for router lisp 0:              6
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                site_reg_count = int(groups['site_reg_count'])
                instance_id_dict.update({'site_reg_count':site_reg_count})

            # Number of configured sites:                             1
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                configured_sites = int(groups['configured_sites'])
                instance_id_dict.update({'configured_sites':configured_sites})

            # Number of registered sites:                             0
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                registered_sites = int(groups['registered_sites'])
                instance_id_dict.update({'registered_sites':registered_sites})

            # Sites with inconsistent registrations:                  0
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                sites_inconsistent_registrations = int(groups['sites_inconsistent_registrations'])
                instance_id_dict.update({'sites_inconsistent_registrations':sites_inconsistent_registrations})

            # IPv4|IPv6|MAC
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                af = groups['af']
                af_dict = instance_id_dict.setdefault('af',{})\
                                          .setdefault(af,{})

            # Number of configured EID prefixes:                    1
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                configured_eid_prefixes = int(groups['configured_eid_prefixes'])
                af_dict.update({'configured_eid_prefixes':configured_eid_prefixes})

            # Number of registered EID prefixes:                    0
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                registered_eid_prefixes = int(groups['registered_eid_prefixes'])
                af_dict.update({'registered_eid_prefixes':registered_eid_prefixes})

            # Instance-Service site-registration limit:             0
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                instance_service_site_reg_limit = int(groups['instance_service_site_reg_limit'])
                af_dict.update({'instance_service_site_reg_limit':instance_service_site_reg_limit})

            # Registration-history size/limit:                      0/1000
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                registration_history_size = int(groups['registration_history_size'])
                registration_history_limit = int(groups['registration_history_limit'])
                af_dict.update({'registration_history_size':registration_history_size,
                                'registration_history_limit':registration_history_limit})
        return ret_dict


class ShowLispInstanceIdForwardingEidRemoteSchema(MetaParser):

    ''' Schema for
        * show lisp instance-id {instance_id} ipv4 forwarding eid remote
        * show lisp instance-id {instance_id} ipv6 forwarding eid remote
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'prefix': {
                            str: { # ipv4 prefix
                                'fwd_action': str,
                                'locator_status_bits': str,
                                'encap_iid': str,
                                'packets': int,
                                'bytes': int
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispInstanceIdIpv4ForwardingEID(ShowLispInstanceIdForwardingEidRemoteSchema):

    ''' Parser for
        * show lisp instance-id {instance_id} ipv4 forwarding eid remote
    '''
    cli_command = 'show lisp instance-id {instance_id} ipv4 forwarding eid remote'

    def cli(self, instance_id, output=None):
        if output is None:
            if instance_id:
                output = self.device.execute(self.cli_command.format(instance_id=instance_id))
        ret_dict = {}

        # 0.0.0.0/0              signal      0x00000000            N/A
        p1 = re.compile(r"^(?P<prefix>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})\s+"
                        r"(?P<fwd_action>\S+)\s+(?P<locator_status_bits>\S+)\s+(?P<encap_iid>\S+)$")

        #   packets/bytes       0/0
        p2 = re.compile(r"^packets\/bytes\s+(?P<packets>\d+)\/(?P<bytes>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # 0.0.0.0/0              signal      0x00000000            N/A
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = 0
                instance_id = int(instance_id)
                prefix = groups['prefix']
                fwd_action = groups['fwd_action']
                locator_status_bits = groups['locator_status_bits']
                encap_iid = groups['encap_iid']
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                instance_id_dict = lisp_id_dict.setdefault('instance_id', {}).setdefault(instance_id, {})
                prefix_dict = instance_id_dict.setdefault('prefix',{}).setdefault(prefix,{})
                prefix_dict.update({'fwd_action':fwd_action,
                                    'locator_status_bits':locator_status_bits,
                                    'encap_iid':encap_iid})

            #   packets/bytes       0/0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                packets = int(groups['packets'])
                bytes = int(groups['bytes'])
                prefix_dict.update({'packets':packets,
                                    'bytes':bytes})
        return ret_dict


class ShowLispInstanceIdIpv6ForwardingEID(ShowLispInstanceIdForwardingEidRemoteSchema):

    ''' Parser for
        * show lisp instance-id {instance_id} ipv6 forwarding eid remote
    '''
    cli_command = 'show lisp instance-id {instance_id} ipv6 forwarding eid remote'

    def cli(self, instance_id, output=None):
        if output is None:
            if instance_id:
                output = self.device.execute(self.cli_command.format(instance_id=instance_id))
        ret_dict = {}

        # ::/0           signal      0x00000000            N/A
        p1 = re.compile(r"^(?P<prefix>[a-fA-F\d\:]+\/\d{1,3})\s+(?P<fwd_action>\S+)"
                        r"\s+(?P<locator_status_bits>\S+)\s+(?P<encap_iid>\S+)$")

        #   packets/bytes       0/0
        p2 = re.compile(r"^packets\/bytes\s+(?P<packets>\d+)\/(?P<bytes>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # 0.0.0.0/0              signal      0x00000000            N/A
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = 0
                instance_id = int(instance_id)
                prefix = groups['prefix']
                fwd_action = groups['fwd_action']
                locator_status_bits = groups['locator_status_bits']
                encap_iid = groups['encap_iid']
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                instance_id_dict = lisp_id_dict.setdefault('instance_id', {}).setdefault(instance_id, {})
                prefix_dict = instance_id_dict.setdefault('prefix',{}).setdefault(prefix,{})
                prefix_dict.update({'fwd_action':fwd_action,
                                    'locator_status_bits':locator_status_bits,
                                    'encap_iid':encap_iid})

            #   packets/bytes       0/0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                packets = int(groups['packets'])
                bytes = int(groups['bytes'])
                prefix_dict.update({'packets':packets,
                                    'bytes':bytes})
        return ret_dict


class ShowLispInstanceIdDNStatisticsSchema(MetaParser):

    ''' Schema for
        * show lisp {lisp_id} instance-id 16777214 dn statistics
        * show lisp {lisp_id} instance-id {instance_id} dn statistics
        * show lisp instance-id 16777214 dn statistics
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: { # Value other than 16777214 is not accepted
                        'iaf_count': int,
                        'loca_eid_map_count': int,
                        'etr_ems_link_count': int,
                        'udp_map_register': {
                            'sent': int,
                            'received': int
                            },
                        'tcp_map_register': {
                            'sent': int,
                            'received': int
                            },
                        'udp_map_notify': {
                            'sent': int,
                            'received': int
                            },
                        'tcp_map_notify': {
                            'sent': int,
                            'received': int
                            }
                        }
                    }
                }
            }
        }


class ShowLispInstanceIdDNStatistics(ShowLispInstanceIdDNStatisticsSchema):

    ''' Parser for
        * show lisp instance-id 16777214 dn statistics
        * show lisp {lisp_id} instance-id 16777214 dn statistics
        * show lisp {lisp_id} instance-id {instance_id} dn statistics
    '''
    cli_command = ['show lisp instance-id 16777214 dn statistics',
                   'show lisp {lisp_id} instance-id {instance_id} dn statistics']

    def cli(self, output=None, lisp_id=None, instance_id=None):
        if output is None:
            if lisp_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id,
                    instance_id=instance_id if instance_id else '16777214'))
            else:
                output = self.device.execute(self.cli_command[0])
        ret_dict = {}

        # Output for router lisp 0
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)$")

        # LISP EID Statistics for instance ID 16777214
        p2 = re.compile(r"^LISP\s+EID\s+Statistics\s+for\s+instance\s+ID\s+(?P<instance_id>\d+)$")

        # Active DN IAF count:                              1 
        p3 = re.compile(r"^Active\s+DN\s+IAF\s+count:\s+(?P<iaf_count>\d+)$")

        # Active DN local eid map count:                    1
        p4 = re.compile(r"^Active\s+DN\s+local\s+eid\s+map\s+"
                        r"count:\s+(?P<loca_eid_map_count>\d+)$")

        # Active DN etr ems registration link count:        2
        p5 = re.compile(r"^Active\s+DN\s+etr\s+ems\s+registration\s+"
                        r"link\s+count:\s+(?P<etr_ems_link_count>\d+)$")

        # UDP Map-Register (send/recv):                     1/0
        p6 = re.compile(r"^UDP\s+Map-Register\s+\(send\/recv\):\s+"
                        r"(?P<sent>\d)\/(?P<received>\d)")

        # TCP Map-Register (send/recv):                     1/0
        p7 = re.compile(r"^TCP\s+Map-Register\s+\(send\/recv\):\s+"
                        r"(?P<sent>\d)\/(?P<received>\d)")

        # UDP Map-Notify (send/recv):                       0/2
        p8 = re.compile(r"^UDP\s+Map-Notify\s+\(send\/recv\):\s+"
                        r"(?P<sent>\d)\/(?P<received>\d)")

        # TCP Map-Notify (send/recv):                       0/5
        p9 = re.compile(r"^TCP\s+Map-Notify\s+\(send\/recv\):\s+"
                        r"(?P<sent>\d)\/(?P<received>\d)")
        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                continue

            # LISP EID Statistics for instance ID 16777214
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                instance_id = int(groups['instance_id'])
                lisp_id = int(lisp_id) if lisp_id else 0
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                instance_id_dict = lisp_id_dict.setdefault('instance_id', {}).setdefault(instance_id, {})
                continue

            # Active DN IAF count:                              1
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                iaf_count = int(groups['iaf_count'])
                instance_id_dict.update({'iaf_count':iaf_count})
                continue

            #  Active DN local eid map count:                    1
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                loca_eid_map_count = int(groups['loca_eid_map_count'])
                instance_id_dict.update({'loca_eid_map_count':loca_eid_map_count})
                continue

            # Active DN etr ems registration link count:        2
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                etr_ems_link_count = int(groups['etr_ems_link_count'])
                instance_id_dict.update({'etr_ems_link_count':etr_ems_link_count})
                continue

            # UDP Map-Register (send/recv):                     1/0
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                sent = int(groups['sent'])
                received = int(groups['received'])
                udp_map_dict = instance_id_dict.setdefault('udp_map_register', {})
                udp_map_dict.update({'sent':sent,
                                     'received':received})
                continue

            # TCP Map-Register (send/recv):                     1/0
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                sent = int(groups['sent'])
                received = int(groups['received'])
                tcp_map_dict = instance_id_dict.setdefault('tcp_map_register', {})
                tcp_map_dict.update({'sent':sent,
                                     'received':received})
                continue

            # UDP Map-Notify (send/recv):                       0/2
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                sent = int(groups['sent'])
                received = int(groups['received'])
                udp_map_dict = instance_id_dict.setdefault('udp_map_notify', {})
                udp_map_dict.update({'sent':sent,
                                     'received':received})
                continue

            # TCP Map-Notify (send/recv):                       0/5
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                sent = int(groups['sent'])
                received = int(groups['received'])
                tcp_map_dict = instance_id_dict.setdefault('tcp_map_notify', {})
                tcp_map_dict.update({'sent':sent,
                                     'received':received})
                continue
        return ret_dict


class ShowLispSessionRLOCSchema(MetaParser):

    ''' Schema for
        * show lisp session {rloc}
        * show lisp {lisp_id} session {rloc}
        * show lisp locator-table {locator_table} session {rloc}
        * show lisp vrf {vrf} session {rloc}
    '''

    schema = {
        'lisp_id': {
            int: {
                'peer_addr': str,
                'peer_port': int,
                'local_address': str,
                Optional('local_port'): int,
                Optional('session_type'): str,
                Optional('session_state'): str,
                Optional('session_state_time'): str,
                Optional('session_rtt'): int,
                Optional('session_rtt_time'): str,
                'messages_in': int,
                'messages_out': int,
                'bytes_in': int,
                'bytes_out': int,
                'fatal_errors': int,
                'rcvd_unsupported': int,
                'rcvd_invalid_vrf': int,
                'rcvd_override':int,
                'rcvd_malformed':int,
                'sent_defferred': int,
                'ssd_redundancy': str,
                'auth_type': str,
                Optional('keychain_name'): str,
                'users': {
                    'count': int,
                    'type': {
                        str: {
                            'id': {
                                str: {
                                    'in': int,
                                    'out': int,
                                    'state': str
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispSessionRLOC(ShowLispSessionRLOCSchema):

    ''' Parser for
        * show lisp session {rloc}
        * show lisp {lisp_id} session {rloc}
        * show lisp locator-table {locator_table} session {rloc}
        * show lisp vrf {vrf} session {rloc}
    '''
    cli_command = ['show lisp session {rloc}',
                   'show lisp {lisp_id} session {rloc}',
                   'show lisp locator-table {locator_table} session {rloc}',
                   'show lisp vrf {vrf} session {rloc}']

    def cli(self, output=None, lisp_id=None, rloc=None, locator_table=None, vrf=None):
        if output is None:
            if lisp_id and rloc:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id,rloc=rloc))
            elif locator_table and rloc:
                output = self.device.execute(self.cli_command[2].format(locator_table=locator_table,rloc=rloc))
            elif vrf and rloc:
                output = self.device.execute(self.cli_command[3].format(vrf=vrf,rloc=rloc))
            else:
                output = self.device.execute(self.cli_command[0].format(rloc=rloc))
        ret_dict = {}

        # Output for router lisp 0
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)$")

        # Peer address:     44.44.44.44:4342
        p2 = re.compile(r"^Peer\s+address:\s+(?P<peer_addr>\d{1,3}\.\d{1,3}\."
                        r"\d{1,3}\.\d{1,3}):(?P<peer_port>\d+)$")

        # Local address:    11.11.11.11:61669
        p3 = re.compile(r"^Local\s+address:\s+(?P<local_address>\d{1,3}\.\d{1,3}\."
                        r"\d{1,3}\.\d{1,3}):(?P<local_port>\d+)$")

        # Session Type:     Active
        p4 = re.compile(r"^Session\s+Type:\s+(?P<session_type>\S+)$")

        # Session State:    Up (4d23h)
        p5 = re.compile(r"^Session\s+State:\s+(?P<session_state>\S+)\s+"
                        r"(?P<session_state_time>\S+)$")

        # Session RTT:      0 ms  (4d23h)
        p6 = re.compile(r"^Session\s+RTT:\s+(?P<session_rtt>\S+)\s+"
                        r"ms\s+(?P<session_rtt_time>\S+)$")

        # Messages in/out:  32/15
        p7 = re.compile(r"^Messages in\/out:\s+(?P<messages_in>\d+)"
                        r"\/(?P<messages_out>\d+)$")

        # Bytes in/out:     1606/1076
        p8 = re.compile(r"^Bytes in\/out:\s+(?P<bytes_in>\d+)"
                        r"\/(?P<bytes_out>\d+)$")

        # Fatal errors:     0
        p9 = re.compile(r"^Fatal\s+errors:\s+(?P<fatal_errors>\d+)$")

        # Rcvd unsupported: 0
        p10 = re.compile(r"^Rcvd\s+unsupported:\s+(?P<rcvd_unsupported>\d+)$")

        # Rcvd invalid VRF: 0
        p11 = re.compile(r"^Rcvd\s+invalid\s+VRF:\s+(?P<rcvd_invalid_vrf>\d+)$")

        # Rcvd override:    0
        p12 = re.compile(r"^Rcvd\s+override:\s+(?P<rcvd_override>\d+)$")

        # Rcvd malformed:   0
        p13 = re.compile(r"^Rcvd\s+malformed:\s+(?P<rcvd_malformed>\d+)$")

        # Sent deferred:    1
        p14 = re.compile(r"^Sent\s+deferred:\s+(?P<sent_defferred>\d+)$")

        # SSO redundancy:   N/A
        p15 = re.compile(r"^SSO\s+redundancy:\s+(?P<ssd_redundancy>\S+)$")

        #Auth Type:        TCP-Auth-Option, keychain:  kc1
        p16 = re.compile(r"^Auth\s+Type:\s+(?P<auth_type>\S+)"
                         r"(,\s+keychain:\s+(?P<keychain_name>\S+))?$")

        # Users:            14
        p17 = re.compile(r"^Users:\s+(?P<count>\S+)$")

        # Pubsub subscriber         lisp 0 IID 101 AFI MAC                   2/0      Off
        p18 = re.compile(r"^(?P<type>[a-zA-Z]+(?:[\s.]+[a-zA-Z]+)*)\s+"
                         r"(?P<id>[a-zA-Z]+(?:[\s.]+[\da-zA-Z]+)*)\s+"
                         r"(?P<in>\d+)\/(?P<out>\d+)\s+(?P<state>\S+)$")

        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                continue

            # Peer address:     44.44.44.44:4342
            m = p2.match(line)
            if m:
                if lisp_id != "all":
                    lisp_id = int(lisp_id) if lisp_id else 0
                    lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                groups = m.groupdict()
                peer_addr = groups['peer_addr']
                peer_port = int(groups['peer_port'])
                lisp_id_dict.update({'peer_addr':peer_addr,
                                     'peer_port':peer_port})
                continue

            # Local address:    11.11.11.11:61669
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                local_address = groups['local_address']
                local_port = int(groups['local_port'])
                lisp_id_dict.update({'local_address':local_address,
                                     'local_port':local_port})
                continue

            # Session Type:     Active
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                session_type = groups['session_type']
                lisp_id_dict.update({'session_type':session_type})
                continue

            # Session State:    Up (4d23h)
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                session_state = groups['session_state']
                session_state_time = groups['session_state_time']
                lisp_id_dict.update({'session_state':session_state,
                                     'session_state_time':session_state_time})
                continue

            # Session RTT:      0 ms  (4d23h)
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                session_rtt = int(groups['session_rtt'])
                session_rtt_time = groups['session_rtt_time']
                lisp_id_dict.update({'session_rtt':session_rtt,
                                     'session_rtt_time':session_rtt_time})
                continue

            # Messages in/out:  32/15
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                messages_in = int(groups['messages_in'])
                messages_out = int(groups['messages_out'])
                lisp_id_dict.update({'messages_in':messages_in,
                                     'messages_out':messages_out})
                continue

            # Bytes in/out:     1606/1076
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                bytes_in = int(groups['bytes_in'])
                bytes_out = int(groups['bytes_out'])
                lisp_id_dict.update({'bytes_in':bytes_in,
                                     'bytes_out':bytes_out})
                continue

            # Fatal errors:     0
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                fatal_errors = int(groups['fatal_errors'])
                lisp_id_dict.update({'fatal_errors':fatal_errors})
                continue

            # Rcvd unsupported: 0
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                rcvd_unsupported = int(groups['rcvd_unsupported'])
                lisp_id_dict.update({'rcvd_unsupported':rcvd_unsupported})
                continue

            # Rcvd invalid VRF: 0
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                rcvd_invalid_vrf = int(groups['rcvd_invalid_vrf'])
                lisp_id_dict.update({'rcvd_invalid_vrf':rcvd_invalid_vrf})
                continue

            # Rcvd override:    0
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                rcvd_override = int(groups['rcvd_override'])
                lisp_id_dict.update({'rcvd_override':rcvd_override})
                continue

            # Rcvd malformed:   0
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                rcvd_malformed = int(groups['rcvd_malformed'])
                lisp_id_dict.update({'rcvd_malformed':rcvd_malformed})
                continue

            # Sent deferred:    1
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                sent_defferred = int(groups['sent_defferred'])
                lisp_id_dict.update({'sent_defferred':sent_defferred})
                continue

            # SSO redundancy:   N/A
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                ssd_redundancy = groups['ssd_redundancy']
                lisp_id_dict.update({'ssd_redundancy':ssd_redundancy})
                continue

            #Auth Type:        TCP-Auth-Option, keychain:  kc1
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                auth_type = groups['auth_type']
                keychain_name = groups['keychain_name']
                if keychain_name:
                    lisp_id_dict.update({'auth_type':auth_type,
                                     'keychain_name':keychain_name})
                else:
                    lisp_id_dict.update({'auth_type':auth_type})
                continue

            # Users:            14
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                count = int(groups['count'])
                count_dict = lisp_id_dict.setdefault('users',{})
                count_dict.update({'count':count})
                continue

            # Pubsub subscriber         lisp 0 IID 101 AFI MAC                   2/0      Off
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                type = groups['type']
                id = groups['id']
                user_in = int(groups['in'])
                out = int(groups['out'])
                state = groups['state']
                type_dict = count_dict.setdefault('type',{}).setdefault(type,{})
                id_dict = type_dict.setdefault('id',{}).setdefault(id,{})
                id_dict.update({'in':user_in,
                                'out':out,
                                'state':state})
                continue
        return ret_dict


class ShowLispIpMapCachePrefixSchema(MetaParser):

    ''' Schema for
        * show lisp instance-id {instance_id} ipv4 map-cache {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 map-cache {prefix}
        * show lisp eid-table vrf {eid_table} ipv4 map-cache {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 map-cache {prefix}
        * show lisp instance-id {instance_id} ipv6 map-cache {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 map-cache {prefix}
        * show lisp eid-table vrf {eid_table} ipv6 map-cache {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 map-cache {prefix}
    '''
    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'eid_table': str,
                        'entries': int,
                        'eid_prefix': str, #194.168.1.72/32
                        'eid': str, # 194.168.1.72
                        'mask': int,
                        'uptime': str,
                        'expires': str,
                        'via': str,
                        Optional('site'): str, # (remote-to-site|local-to-site)
                        Optional('received_mapping'): str,
                        Optional('sgt'): int,
                        'sources': str,
                        'state': str,
                        'last_modified': str,
                        'map_source': str,
                        Optional('activity'): str, # (Idle|Active|Exempt)
                        Optional('packets_out'): int,
                        Optional('packets_out_bytes'): int,
                        Optional('action'): str,
                        'locators': {
                            Any(): {
                                'uptime': str,
                                'state': str,
                                'priority': int,
                                'weight': int,
                                'encap_iid': str,
                                Optional('domain_id'): str,
                                Optional('multihome_id'): str,
                                Optional('metric'): str,
                                Optional('state_change_time'): str,
                                Optional('state_change_count'): int,
                                Optional('route_reachability_change_time'): str,
                                Optional('route_reachability_change_count'): int,
                                Optional('priority_change'): str,
                                Optional('weight_change'): str,
                                Optional('reject_reason'): str,
                                Optional('rloc_probe_sent'): str,
                                Optional('rloc_probe_in'): str,
                                Optional('itr_rloc'): str
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispIpMapCachePrefixSuperParser(ShowLispIpMapCachePrefixSchema):

    ''' Parser for
        * show lisp instance-id {instance_id} ipv4 map-cache {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 map-cache {prefix}
        * show lisp eid-table vrf {eid_table} ipv4 map-cache {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 map-cache {prefix}
        * show lisp instance-id {instance_id} ipv6 map-cache {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 map-cache {prefix}
        * show lisp eid-table vrf {eid_table} ipv6 map-cache {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 map-cache {prefix}
    '''

    def cli(self, prefix, output=None, lisp_id=None, instance_id=None, eid_table=None, locator_table=None):

        ret_dict = {}

        # LISP IPv4 Mapping Cache for LISP 0 EID-table vrf red (IID 100), 3 entries
        # LISP IPv6 Mapping Cache for LISP 0 EID-table vrf red (IID 100), 3 entries
        p1 = re.compile(r"^LISP\s+(IPv4|IPv6)\s+Mapping\s+Cache\s+for\s+LISP\s+"
                        r"(?P<lisp_id>\d+)\s+EID-table\s+vrf\s+(?P<eid_table>\S+)\s+"
                        r"\(IID\s+(?P<instance_id>\d+)\),\s+(?P<entries>\d+)\s+entries$")

        # 191.168.1.11/32, uptime: 02:26:35, expires: 21:33:24, via map-reply, self, complete, remote-to-site
        # 2001:194:168:1::72/128, uptime: 00:44:35, expires: 23:15:25, via map-reply, complete
        p2 = re.compile(r"^(?P<eid>[a-fA-F\d\:\.]+)\/(?P<mask>\d{1,3}),\s+uptime:\s+"
                        r"(?P<uptime>(\d{2}:?){3}|\dw\dd),\s+expires:\s+(?P<expires>(\d{2}:?){3}|never),"
                        r"\s+via\s+(?P<via>[-\w]+)(,\s+self)?(,\s+complete)?(,\s+unknown-eid-forward)?(,\s+"
                        r"(?P<site>remote-to-site|local-to-site))?(,\s+\S+)?$")

        # Received mapping for 191.168.0.0/16
        p3 = re.compile(r"^Received\s+mapping\s+for\s+"
                        r"(?P<received_mapping>[a-fA-F\d\:\.]+\/\d{1,3})$")

        # SGT: 100
        p4 = re.compile(r"^SGT:\s+(?P<sgt>\d+)$")

        # Sources: map-reply
        # Sources: map-reply, static-send-map-request
        p5 = re.compile(r"^Sources:\s+(?P<sources>[\S\s]+)$")

        # State: complete, last modified: 02:26:35, map-source: 10.10.10.101
        # State: unknown-eid-forward, last modified: 00:00:00, map-source: local
        p6 = re.compile(r"^State:\s+(?P<state>\S+),\s+last\s+modified:\s+"
                        r"(?P<last_modified>\d{1,2}:\d{2}:\d{2}),\s+map-source:\s+"
                        r"(?P<map_source>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\S+)$")

        # Exempt, Packets out: 146(14600 bytes) (~ 01:37:41 ago)
        p7 = re.compile(r"^(?P<activity>Idle|Active|Exempt),\s+Packets\s+"
                        r"out:\s+(?P<packets_out>\d+)\((?P<packets_out_bytes>\d+)"
                        r"\s+bytes\)\s+\(\W+\d{1,2}:\d{2}:\d{2}\s+ago\)$")

        # Negative cache entry, action: send-map-request
        p8 = re.compile(r"^Negative\s+cache\s+entry,\s+action:\s+(?P<action>\S+)$")

        # 101.101.101.101  02:26:35  up           1/100       -             1/2           -
        # 45.45.45.45  00:00:04  up, self    10/50   111                 3/3      0
        p9 = re.compile(r"^(?P<locators>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
                        r"(?P<uptime>\d{1,2}:\d{2}:\d{2})\s+(?P<state>\S+)(,\s+self)?\s+"
                        r"(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<encap_iid>\S+)|\s+"
                        r"(?P<domain_id>\d+)\/(?P<multihome_id>\d+)\s+(?P<metric>\S+)$")

        # Last up-down state change:         02:26:35, state change count: 1
        p10 = re.compile(r"^Last\s+up-down\s+state\s+change:\s+"
                         r"(?P<state_change_time>\d{1,2}:\d{2}:\d{2}|\dw\dd),"
                         r"\s+state\s+change\s+count:\s+(?P<state_change_count>\d+)$")

        # Last route reachability change:    02:26:35, state change count: 1
        p11 = re.compile(r"^Last\s+route\s+reachability\s+change:\s+"
                         r"(?P<route_reachability_change_time>\d{1,2}:\d{2}:\d{2}|\dw\dd),\s+"
                         r"state\s+change\s+count:\s+(?P<route_reachability_change_count>\d+)$")

        # Last priority / weight change:     never/never
        p12 = re.compile(r"^Last\s+priority\s+\/\s+weight\s+change:\s+"
                         r"(?P<priority_change>\S+)\/(?P<weight_change>\S+)$")

        # RLOC route rejection reason:       reachability (minimum mask length check failed)
        p13 = re.compile(r"^RLOC\s+route\s+rejection\s+reason:\s+"
                         r"(?P<reject_reason>[\(\)\w\s-]+)$")

        # Last RLOC-probe sent:            00:24:49 (rtt 1ms)
        p14 = re.compile(r"^Last\s+RLOC-probe\s+sent:\s+"
                         r"(?P<rloc_probe_sent>\d{2}:\d{2}:\d{2}\s+\(rtt\s+\d+ms\))$")

        # Next RLOC-probe in:              00:47:14
        p15 = re.compile(r"^Next\s+RLOC-probe\s+in:\s+"
                         r"(?P<rloc_probe_sent>\d{2}:\d{2}:\d{2})$")

        # Latched to ITR-RLOC:             104.104.104.104
        p16 = re.compile(r"^Latched\s+to\s+ITR-RLOC:\s+"
                         r"(?P<itr_rloc>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$")

        for line in output.splitlines():
            line = line.strip()

            # LISP IPv4 Mapping Cache for LISP 0 EID-table vrf red (IID 100), 3 entries
            # LISP IPv6 Mapping Cache for LISP 0 EID-table vrf red (IID 100), 3 entries
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                eid_table = groups['eid_table']
                entries = int(groups['entries'])
                instance_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {}).setdefault('instance_id',{}).setdefault(instance_id,{})
                instance_id_dict.update({'eid_table':eid_table,'entries':entries})
                continue

            # 191.168.1.11/32, uptime: 02:26:35, expires: 21:33:24, via map-reply, self, complete, remote-to-site
            # 2001:194:168:1::72/128, uptime: 00:44:35, expires: 23:15:25, via map-reply, complete
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                eid = groups['eid']
                mask = int(groups['mask'])
                uptime = groups['uptime']
                expires = groups['expires']
                via = groups['via']
                site = groups['site']
                eid_prefix = "{}/{}".format(eid,mask)
                instance_id_dict.update({'eid_prefix':eid_prefix,
                                         'eid':eid,
                                         'mask':mask,
                                         'uptime':uptime,
                                         'expires':expires,
                                         'via':via})
                if site:
                    instance_id_dict.update({'site':site})
                continue

            # Received mapping for 191.168.0.0/16
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                received_mapping = groups['received_mapping']
                instance_id_dict.update({'received_mapping':received_mapping})
                continue

            # SGT: 100
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                sgt = int(groups['sgt'])
                instance_id_dict.update({'sgt':sgt})
                continue

            # Sources: map-reply
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                sources = groups['sources']
                instance_id_dict.update({'sources':sources})
                continue

            # State: complete, last modified: 02:26:35, map-source: 10.10.10.101
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                state = groups['state']
                last_modified = groups['last_modified']
                map_source = groups['map_source']
                instance_id_dict.update({'state':state,
                                         'last_modified':last_modified,
                                         'map_source':map_source})
                continue

            # Exempt, Packets out: 146(14600 bytes) (~ 01:37:41 ago)
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                activity = groups['activity']
                packets_out = int(groups['packets_out'])
                packets_out_bytes = int(groups['packets_out_bytes'])
                instance_id_dict.update({'activity':activity,
                                         'packets_out':packets_out,
                                         'packets_out_bytes':packets_out_bytes})
                continue

            # Negative cache entry, action: send-map-request
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                action = groups['action']
                instance_id_dict.update({'action':action})
                continue

            # 101.101.101.101  02:26:35  up           1/100       -             1/2           -
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                locators = groups['locators']
                uptime = groups['uptime']
                state = groups['state']
                priority = int(groups['priority'])
                weight = int(groups['weight'])
                encap_iid = groups['encap_iid']
                domain_id = groups['domain_id']
                multihome_id = groups['multihome_id']
                metric = groups['metric']
                locators_dict = instance_id_dict.setdefault('locators',{}).setdefault(locators,{})
                locators_dict.update({'uptime':uptime,
                                      'state':state,
                                      'priority':priority,
                                      'weight':weight,
                                      'encap_iid':encap_iid})
                if domain_id and multihome_id and metric:
                    locators_dict.update({'domain_id':domain_id,
                                          'multihome_id':multihome_id,
                                          'metric':metric})
                continue

            # Last up-down state change:         02:26:35, state change count: 1
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                state_change_time = groups['state_change_time']
                state_change_count = int(groups['state_change_count'])
                locators_dict.update({'state_change_time':state_change_time,
                                      'state_change_count':state_change_count})
                continue

            # Last route reachability change:    02:26:35, state change count: 1
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                route_reachability_change_time = groups['route_reachability_change_time']
                route_reachability_change_count = int(groups['route_reachability_change_count'])
                locators_dict.update({'route_reachability_change_time':route_reachability_change_time,
                                      'route_reachability_change_count':route_reachability_change_count})
                continue

            # Last priority / weight change:     never/never
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                priority_change = groups['priority_change']
                weight_change = groups['weight_change']
                locators_dict.update({'priority_change':priority_change,
                                      'weight_change':weight_change})
                continue

            # RLOC route rejection reason:       reachability (minimum mask length check failed)
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                reject_reason = groups['reject_reason']
                locators_dict.update({'reject_reason':reject_reason})
                continue

            # Last RLOC-probe sent:            00:24:49 (rtt 1ms)
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                rloc_probe_sent = groups['rloc_probe_sent']
                locators_dict.update({'rloc_probe_sent':rloc_probe_sent})
                continue

            # Next RLOC-probe in:              00:47:14
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                rloc_probe_in = groups['rloc_probe_in']
                locators_dict.update({'rloc_probe_in':rloc_probe_in})
                continue

            # Latched to ITR-RLOC:             104.104.104.104
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                itr_rloc = groups['itr_rloc']
                locators_dict.update({'itr_rloc':itr_rloc})
                continue
        return ret_dict


class ShowLispIpv4MapCachePrefix(ShowLispIpMapCachePrefixSuperParser):

    ''' Parser for
        * show lisp instance-id {instance_id} ipv4 map-cache {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 map-cache {prefix}
        * show lisp eid-table vrf {eid_table} ipv4 map-cache {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 map-cache {prefix}
    '''
    cli_command = ['show lisp instance-id {instance_id} ipv4 map-cache {prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 map-cache {prefix}',
                   'show lisp eid-table vrf {eid_table} ipv4 map-cache {prefix}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 map-cache {prefix}']

    def cli(self, prefix, output=None, lisp_id=None, instance_id=None, eid_table=None, locator_table=None):
        if output is None:
            if locator_table and instance_id and prefix:
                output = self.device.execute(self.cli_command[3].format(locator_table=locator_table,instance_id=instance_id,prefix=prefix))
            elif lisp_id and instance_id and prefix:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id,instance_id=instance_id,prefix=prefix))
            elif instance_id and prefix:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id,prefix=prefix))
            else:
                output = self.device.execute(self.cli_command[2].format(eid_table=eid_table,prefix=prefix))
        return super().cli(prefix, output=output, lisp_id=lisp_id, instance_id=instance_id, eid_table=eid_table, locator_table=locator_table)


class ShowLispIpv6MapCachePrefix(ShowLispIpMapCachePrefixSuperParser):

    ''' Parser for
        * show lisp instance-id {instance_id} ipv6 map-cache {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 map-cache {prefix}
        * show lisp eid-table vrf {eid_table} ipv6 map-cache {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 map-cache {prefix}
    '''
    cli_command = ['show lisp instance-id {instance_id} ipv6 map-cache {prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 map-cache {prefix}',
                   'show lisp eid-table vrf {eid_table} ipv6 map-cache {prefix}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 map-cache {prefix}']

    def cli(self, prefix, output=None, lisp_id=None, instance_id=None, eid_table=None, locator_table=None):
        if output is None:
            if locator_table and instance_id and prefix:
                output = self.device.execute(self.cli_command[3].format(locator_table=locator_table,instance_id=instance_id,prefix=prefix))
            elif lisp_id and instance_id and prefix:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id,instance_id=instance_id,prefix=prefix))
            elif instance_id and prefix:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id,prefix=prefix))
            else:
                output = self.device.execute(self.cli_command[2].format(eid_table=eid_table,prefix=prefix))
        return super().cli(prefix, output=output, lisp_id=lisp_id, instance_id=instance_id, eid_table=eid_table, locator_table=locator_table)


class ShowLispPlatformStatisticsSchema(MetaParser):

    ''' Schema for
        * show lisp platform statistics
    '''
    schema = {
        'fib': {
            'notifications': {
                'received': int,
                'processed': int
                },
            'invalid': {
                'received': int,
                'processed': int
                },
            'data_packet': {
                'received': int,
                'processed': int
                },
            'l2_data_packet': {
                'received': int,
                'processed': int
                },
            'status_report': {
                'received': int,
                'processed': int
                },
            'dyn_eid_detected': {
                'received': int,
                'processed': int
                },
            'dyn_eid_decap_statle': {
                'received': int,
                'processed': int
                },
            'l2_dyn_eid_decap_statle': {
                'received': int,
                'processed': int
                },
            'dyn_eid_adjacency': {
                'received': int,
                'processed': int
                },
            'delete_map_cache': {
                'received': int,
                'processed': int
                }
            },
        'l2_rib': {
            'remote_update_requests': int,
            'local_update_requests': int,
            'delete_requests': int,
            'update_test': int,
            'delete_test': int,
            'message_sent': int,
            'message_received': int,
            'unknown_message_received': int,
            'send_errors': int,
            'flow_control': int
            },
        'cef': {
            'dropped_notifications': int,
            'total_notifications': int,
            'dropped_control_packets': int,
            'high_priority_queue': int,
            'normal_priority_queue': int
            },
        'deffered': {
            'ddt_referral': {
                'deferred': int,
                'dropped': int
                },
            'ddt_request': {
                'deferred': int,
                'dropped': int
                },
            'ddt_query': {
                'deferred': int,
                'dropped': int
                },
            'map_request': {
                'deferred': int,
                'dropped': int
                },
            'map_register': {
                'deferred': int,
                'dropped': int
                },
            'map_reply': {
                'deferred': int,
                'dropped': int
                },
            'mr_negative_map_reply': {
                'deferred': int,
                'dropped': int
                },
            'mr_map_request_fwd': {
                'deferred': int,
                'dropped': int
                },
            'ms_map_request_fwd': {
                'deferred': int,
                'dropped': int
                },
            'ms_proxy_map_reply': {
                'deferred': int,
                'dropped': int
                },
            'xtr_mcast_map_notify': {
                'deferred': int,
                'dropped': int
                },
            'ms_info_reply': {
                'deferred': int,
                'dropped': int
                },
            'ms_map_notify': {
                'deferred': int,
                'dropped': int
                },
            'rtr_map_register_fwd': {
                'deferred': int,
                'dropped': int
                },
            'rtr_map_notify_fwd': {
                'deferred': int,
                'dropped': int
                },
            'etr_info_request': {
                'deferred': int,
                'dropped': int
                },
            },
        'errors': {
            'invalid_ip_version_drops': int
            },
        'udp_control_packets': {
            'ipv4': {
                'received_total_packets': int,
                'received_invalid_vrf': int,
                'received_invalid_ip_header': int,
                'received_invalid_protocol': int,
                'received_invalid_size': int,
                'received_invalid_port': int,
                'received_invalid_checksum': int,
                'received_unsupported_lisp': int,
                'received_not_lisp_control': int,
                'received_unknown_lisp_control': int,
                'sent_total': int,
                'sent_flow_controlled': int,
                },
            'ipv6': {
                'received_total_packets': int,
                'received_invalid_vrf': int,
                'received_invalid_ip_header': int,
                'received_invalid_protocol': int,
                'received_invalid_size': int,
                'received_invalid_port': int,
                'received_invalid_checksum': int,
                'received_unsupported_lisp': int,
                'received_not_lisp_control': int,
                'received_unknown_lisp_control': int,
                'sent_total': int,
                'sent_flow_controlled': int,
                }
            }
        }


class ShowLispPlatformStatistics(ShowLispPlatformStatisticsSchema):

    ''' Parser for
        * show lisp platform statistics
    '''
    cli_command = 'show lisp platform statistics'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)
        ret_dict = {}

        #  FIB notications received/processed:                    35669/35669
        p1 = re.compile(r"^FIB\s+notications\s+received\/processed:\s+"
                        r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # Invalid received/processed:                          0/0
        p2 = re.compile(r"^Invalid\s+received\/processed:\s+"
                        r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # Data packet signal received/processed:               35669/35669
        p3 = re.compile(r"^Data\s+packet\s+signal\s+received\/processed:\s+"
                        r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # L2 data packet signal received/processed:            0/0
        p4 = re.compile(r"^L2\s+data\s+packet\s+signal\s+received\/processed:\s+"
                        r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # Status report received/processed:                    0/0
        p5 = re.compile(r"^Status\s+report\s+received\/processed:\s+"
                        r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # Dyn-EID detected received/processed:                 0/0
        p6 = re.compile(r"^Dyn-EID\s+detected\s+received\/processed:\s+"
                        r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # Dyn-EID decap stale detected received/processed:     0/0
        p7 = re.compile(r"^Dyn-EID\s+decap\s+stale\s+detected\s+received\/processed:\s+"
                        r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # L2 dyn-EID decap stale detected received/processed:  0/0
        p8 = re.compile(r"^L2\s+dyn-EID\s+decap\s+stale\s+detected\s+"
                        r"received\/processed:\s+(?P<received>\d+)\/(?P<processed>\d+)$")

        # Dyn-EID adjacency discover received/processed:       0/0
        p9 = re.compile(r"^Dyn-EID\s+adjacency\s+discover\s+received\/"
                        r"processed:\s+(?P<received>\d+)\/(?P<processed>\d+)$")

        # delete map-cache received/processed:                 0/0
        p10 = re.compile(r"^delete\s+map-cache\s+received\/processed:\s+"
                         r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # Remote update requests:                              0
        p11 = re.compile(r"^Remote\s+update\s+requests:\s+(?P<remote_update_requests>\d+)$")

        # Local update requests:                               5
        p12 = re.compile(r"^Local\s+update\s+requests:\s+(?P<local_update_requests>\d+)$")

        # Delete requests:                                     1
        p13 = re.compile(r"^Delete\s+requests:\s+(?P<delete_requests>\d+)$")

        # Update test:                                         0
        p14 = re.compile(r"^Update\s+test:\s+(?P<update_test>\d+)$")

        # Delete test:                                         0
        p15 = re.compile(r"^Delete\s+test:\s+(?P<delete_test>\d+)$")

        # Message sent:                                        6
        p16 = re.compile(r"^Message\s+sent:\s+(?P<message_sent>\d+)$")

        # Message received:                                    6
        p17 = re.compile(r"^Message\s+received:\s+(?P<message_received>\d+)$")

        # Unknown message received:                            0
        p18 = re.compile(r"^Unknown\s+message\s+received:\s+(?P<unknown_message_received>\d+)$")

        # Send Error:                                          0
        p19 = re.compile(r"^Send\s+Error:\s+(?P<send_errors>\d+)$")

        # Number of times blocked (flow control):              0
        p20 = re.compile(r"^Number\s+of\s+times\s+blocked\s+"
                         r"\(flow\s+control\):\s+(?P<flow_control>\d+)$")

        # Dropped notications from CEF:                          0
        p21 = re.compile(r"^Dropped\s+notications\s+"
                         r"from\s+CEF:\s+(?P<dropped_notifications>\d+)$")

        # Total notications from CEF:                            35669
        p22 = re.compile(r"^Total\s+notications\s+from\s+CEF:\s+(?P<total_notifications>\d+)$")

        # Dropped control packets in input queue:                0
        p23 = re.compile(r"^Dropped\s+control\s+packets\s+in\s+"
                         r"input\s+queue:\s+(?P<dropped_control_packets>\d+)$")

        # High priority input queue:                           0
        p24 = re.compile(r"^High\s+priority\s+input\s+queue:\s+(?P<high_priority_queue>\d+)$")

        # Normal priority input queue:                         0
        p25 = re.compile(r"^Normal\s+priority\s+input\s+queue:\s+(?P<normal_priority_queue>\d+)$")

        # DDT referral deferred/dropped:                       0/0
        p26 = re.compile(r"^DDT\s+referral\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # DDT request deferred/dropped:                        0/0
        p27 = re.compile(r"^DDT\s+request\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # DDT query deferred/dropped:                          0/0
        p28 = re.compile(r"^DDT\s+query\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # Map-Request deferred/dropped:                        0/0
        p29 = re.compile(r"^Map-Request\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # Map-Register deferred/dropped:                       0/0
        p30 = re.compile(r"^Map-Register\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # Map-Reply deferred/dropped:                          0/0
        p31 = re.compile(r"^Map-Reply\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # MR negative Map-Reply deferred/dropped:              0/0
        p32 = re.compile(r"^MR\s+negative\s+Map-Reply\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # MR Map-Request fwd deferred/dropped:                 0/0
        p33 = re.compile(r"^MR\s+Map-Request\s+fwd\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # MS Map-Request fwd deferred/dropped:                 0/0
        p34 = re.compile(r"^MS\s+Map-Request\s+fwd\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # MS proxy Map-Reply deferred/dropped:                 0/0
        p35 = re.compile(r"^MS\s+proxy\s+Map-Reply\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # xTR mcast Map-Notify deferred/dropped:               0/0
        p36 = re.compile(r"^xTR\s+mcast\s+Map-Notify\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # MS Info-Reply deferred/dropped:                      0/0
        p37 = re.compile(r"^MS\s+Info-Reply\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # MS Map-Notify deferred/dropped:                      0/0
        p38 = re.compile(r"^MS\s+Map-Notify\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # RTR Map-Register fwd deferred/dropped:               0/0
        p39 = re.compile(r"^RTR\s+Map-Register\s+fwd\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # RTR Map-Notify fwd deferred/dropped:                 0/0
        p40 = re.compile(r"^RTR\s+Map-Notify\s+fwd\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # ETR Info-Request deferred/dropped:                   0/0
        p41 = re.compile(r"^ETR\s+Info-Request\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # Invalid IP version drops:                              0
        p42 = re.compile(r"^Invalid\s+IP\s+version\s+drops:"
                         r"\s+(?P<invalid_ip_version_drops>\d+)$")

        # IPv4 UDP control packets:
        # IPv6 UDP control packets:
        p43 = re.compile(r"^IP(?P<ip_version>v4|v6)\s+UDP\s+control\s+packets:$")

        # Rcvd total packets:                                    0
        p44 = re.compile(r"^Rcvd\s+total\s+packets:\s+(?P<received_total_packets>\d+)$")

        # Rcvd invalid vrf:                                      0
        p45 = re.compile(r"^Rcvd\s+invalid\s+vrf:\s+(?P<received_invalid_vrf>\d+)$")

        # Rcvd invalid IP header:                                0
        p46 = re.compile(r"^Rcvd\s+invalid\s+IP\s+header:\s+(?P<received_invalid_ip_header>\d+)$")

        # Rcvd invalid protocol:                                 0
        p47 = re.compile(r"^Rcvd\s+invalid\s+protocol:\s+(?P<received_invalid_protocol>\d+)$")

        # Rcvd invalid size:                                     0
        p48 = re.compile(r"^Rcvd\s+invalid\s+size:\s+(?P<received_invalid_size>\d+)$")

        # Rcvd invalid port:                                     0
        p49 = re.compile(r"^Rcvd\s+invalid\s+port:\s+(?P<received_invalid_port>\d+)$")

        # Rcvd invalid checksum:                                 0
        p50 = re.compile(r"^Rcvd\s+invalid\s+checksum:\s+(?P<received_invalid_checksum>\d+)$")

        # Rcvd unsupported LISP:                                 0
        p51 = re.compile(r"^Rcvd\s+unsupported\s+LISP:\s+(?P<received_unsupported_lisp>\d+)$")

        # Rcvd not LISP control:                                 0
        p52 = re.compile(r"^Rcvd\s+not\s+LISP\s+control:\s+(?P<received_not_lisp_control>\d+)$")

        # Rcvd unknown LISP control:                             0
        p53 = re.compile(r"^Rcvd\s+unknown\s+LISP\s+control:\s+(?P<received_unknown_lisp_control>\d+)$")

        # Sent total packets:                                    0
        p54 = re.compile(r"^Sent\s+total\s+packets:\s+(?P<sent_total>\d+)$")

        # Sent flow controlled:                                  0
        p55 = re.compile(r"^Sent\s+flow\s+controlled:\s+(?P<sent_flow_controlled>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # FIB notications received/processed:                    35669/35669
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                fib_dict = ret_dict.setdefault('fib', {})
                notification_dict = fib_dict.setdefault('notifications', {})
                notification_dict.update({'received':received,
                                          'processed':processed})
                continue

            # Invalid received/processed:                          0/0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                invalid_dict = fib_dict.setdefault('invalid', {})
                invalid_dict.update({'received':received,
                                     'processed':processed})
                continue

            # Data packet signal received/processed:               35669/35669
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                data_dict = fib_dict.setdefault('data_packet', {})
                data_dict.update({'received':received,
                                  'processed':processed})
                continue

            # L2 data packet signal received/processed:            0/0
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                l2_data_dict = fib_dict.setdefault('l2_data_packet', {})
                l2_data_dict.update({'received':received,
                                     'processed':processed})
                continue

            # Status report received/processed:                    0/0
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                status_dict = fib_dict.setdefault('status_report', {})
                status_dict.update({'received':received,
                                    'processed':processed})
                continue

            # Dyn-EID detected received/processed:                 0/0
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                dyn_dict = fib_dict.setdefault('dyn_eid_detected', {})
                dyn_dict.update({'received':received,
                                 'processed':processed})
                continue

            # Dyn-EID decap stale detected received/processed:     0/0
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                dyn_decap_dict = fib_dict.setdefault('dyn_eid_decap_statle', {})
                dyn_decap_dict.update({'received':received,
                                       'processed':processed})
                continue

            # L2 dyn-EID decap stale detected received/processed:  0/0
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                l2_dyn_decap_dict = fib_dict.setdefault('l2_dyn_eid_decap_statle', {})
                l2_dyn_decap_dict.update({'received':received,
                                          'processed':processed})
                continue

            # Dyn-EID adjacency discover received/processed:       0/0
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                dyn_adjacency_dict = fib_dict.setdefault('dyn_eid_adjacency', {})
                dyn_adjacency_dict.update({'received':received,
                                           'processed':processed})
                continue

            # delete map-cache received/processed:                 0/0
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                delete_dict = fib_dict.setdefault('delete_map_cache', {})
                delete_dict.update({'received':received,
                                    'processed':processed})
                continue

            # Remote update requests:                              0
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                remote_update_requests = int(groups['remote_update_requests'])
                l2_dict = ret_dict.setdefault('l2_rib', {})
                l2_dict.update({'remote_update_requests':remote_update_requests})
                continue

            # Local update requests:                               5
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                local_update_requests = int(groups['local_update_requests'])
                l2_dict.update({'local_update_requests':local_update_requests})
                continue

            # Delete requests:                                     1
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                delete_requests = int(groups['delete_requests'])
                l2_dict.update({'delete_requests':delete_requests})
                continue

            # Update test:                                         0
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                update_test = int(groups['update_test'])
                l2_dict.update({'update_test':update_test})
                continue

            # Delete test:                                         0
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                delete_test = int(groups['delete_test'])
                l2_dict.update({'delete_test':delete_test})
                continue

            # Message sent:                                        6
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                message_sent = int(groups['message_sent'])
                l2_dict.update({'message_sent':message_sent})
                continue

            # Message received:                                    6
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                message_received = int(groups['message_received'])
                l2_dict.update({'message_received':message_received})
                continue

            # Unknown message received:                            0
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                unknown_message_received = int(groups['unknown_message_received'])
                l2_dict.update({'unknown_message_received':unknown_message_received})
                continue

            # Send Error:                                          0
            m = p19.match(line)
            if m:
                groups = m.groupdict()
                send_errors = int(groups['send_errors'])
                l2_dict.update({'send_errors':send_errors})
                continue

            # Number of times blocked (flow control):              0
            m = p20.match(line)
            if m:
                groups = m.groupdict()
                flow_control = int(groups['flow_control'])
                l2_dict.update({'flow_control':flow_control})
                continue

            # Dropped notications from CEF:                          0
            m = p21.match(line)
            if m:
                groups = m.groupdict()
                dropped_notifications = int(groups['dropped_notifications'])
                cef_dict = ret_dict.setdefault('cef', {})
                cef_dict.update({'dropped_notifications':dropped_notifications})
                continue

            # Total notications from CEF:                            35669
            m = p22.match(line)
            if m:
                groups = m.groupdict()
                total_notifications = int(groups['total_notifications'])
                cef_dict.update({'total_notifications':total_notifications})
                continue

            # Dropped control packets in input queue:                0
            m = p23.match(line)
            if m:
                groups = m.groupdict()
                dropped_control_packets = int(groups['dropped_control_packets'])
                cef_dict.update({'dropped_control_packets':dropped_control_packets})
                continue

            # High priority input queue:                           0
            m = p24.match(line)
            if m:
                groups = m.groupdict()
                high_priority_queue = int(groups['high_priority_queue'])
                cef_dict.update({'high_priority_queue':high_priority_queue})
                continue

            # Normal priority input queue:                         0
            m = p25.match(line)
            if m:
                groups = m.groupdict()
                normal_priority_queue = int(groups['normal_priority_queue'])
                cef_dict.update({'normal_priority_queue':normal_priority_queue})
                continue

            # DDT referral deferred/dropped:                       0/0
            m = p26.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                deferred_dict = ret_dict.setdefault('deffered', {})
                ddt_referral_dict = deferred_dict.setdefault('ddt_referral', {})
                ddt_referral_dict.update({'deferred':deferred,
                                          'dropped':dropped})
                continue

            # DDT request deferred/dropped:                        0/0
            m = p27.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                ddt_request_dict = deferred_dict.setdefault('ddt_request', {})
                ddt_request_dict.update({'deferred':deferred,
                                         'dropped':dropped})
                continue

            # DDT query deferred/dropped:                          0/0
            m = p28.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                ddt_query_dict = deferred_dict.setdefault('ddt_query', {})
                ddt_query_dict.update({'deferred':deferred,
                                       'dropped':dropped})
                continue

            # Map-Request deferred/dropped:                        0/0
            m = p29.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                map_request_dict = deferred_dict.setdefault('map_request', {})
                map_request_dict.update({'deferred':deferred,
                                         'dropped':dropped})
                continue

            # Map-Register deferred/dropped:                       0/0
            m = p30.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                map_register_dict = deferred_dict.setdefault('map_register', {})
                map_register_dict.update({'deferred':deferred,
                                          'dropped':dropped})
                continue

            # Map-Reply deferred/dropped:                          0/0
            m = p31.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                map_reply_dict = deferred_dict.setdefault('map_reply', {})
                map_reply_dict.update({'deferred':deferred,
                                       'dropped':dropped})
                continue

            # MR negative Map-Reply deferred/dropped:              0/0
            m = p32.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                mr_negative_dict = deferred_dict.setdefault('mr_negative_map_reply', {})
                mr_negative_dict.update({'deferred':deferred,
                                         'dropped':dropped})
                continue

            # MR Map-Request fwd deferred/dropped:                 0/0
            m = p33.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                mr_map_request_dict = deferred_dict.setdefault('mr_map_request_fwd', {})
                mr_map_request_dict.update({'deferred':deferred,
                                            'dropped':dropped})
                continue

            # MS Map-Request fwd deferred/dropped:                 0/0
            m = p34.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                ms_map_request_dict = deferred_dict.setdefault('ms_map_request_fwd', {})
                ms_map_request_dict.update({'deferred':deferred,
                                            'dropped':dropped})
                continue

            # MS proxy Map-Reply deferred/dropped:                 0/0
            m = p35.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                ms_proxy_map_dict = deferred_dict.setdefault('ms_proxy_map_reply', {})
                ms_proxy_map_dict.update({'deferred':deferred,
                                          'dropped':dropped})
                continue

            # xTR mcast Map-Notify deferred/dropped:               0/0
            m = p36.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                xtr_mcast_map_dict = deferred_dict.setdefault('xtr_mcast_map_notify', {})
                xtr_mcast_map_dict.update({'deferred':deferred,
                                           'dropped':dropped})
                continue

            # MS Info-Reply deferred/dropped:                      0/0
            m = p37.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                ms_info_dict = deferred_dict.setdefault('ms_info_reply', {})
                ms_info_dict.update({'deferred':deferred,
                                     'dropped':dropped})
                continue

            # MS Map-Notify deferred/dropped:                      0/0
            m = p38.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                ms_map_dict = deferred_dict.setdefault('ms_map_notify', {})
                ms_map_dict.update({'deferred':deferred,
                                    'dropped':dropped})
                continue

            # RTR Map-Register fwd deferred/dropped:               0/0
            m = p39.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                rtr_map_dict = deferred_dict.setdefault('rtr_map_register_fwd', {})
                rtr_map_dict.update({'deferred':deferred,
                                     'dropped':dropped})
                continue

            # RTR Map-Notify fwd deferred/dropped:                 0/0
            m = p40.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                rtr_map_notify_dict = deferred_dict.setdefault('rtr_map_notify_fwd', {})
                rtr_map_notify_dict.update({'deferred':deferred,
                                            'dropped':dropped})
                continue

            # ETR Info-Request deferred/dropped:                   0/0
            m = p41.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                etr_info_request_dict = deferred_dict.setdefault('etr_info_request', {})
                etr_info_request_dict.update({'deferred':deferred,
                                              'dropped':dropped})
                continue

            # Invalid IP version drops:                              0
            m = p42.match(line)
            if m:
                groups = m.groupdict()
                invalid_ip_version_drops = int(groups['invalid_ip_version_drops'])
                invalid_dict = ret_dict.setdefault('errors', {})
                invalid_dict.update({'invalid_ip_version_drops':invalid_ip_version_drops})
                continue

            # IPv4 UDP control packets:
            # IPv6 UDP control packets:
            m = p43.match(line)
            if m:
                groups = m.groupdict()
                ip_version = groups['ip_version']
                ip_dict = ret_dict.setdefault('udp_control_packets', {}).setdefault(f'ip{ip_version}', {})

            # Rcvd total packets:                                    0
            m = p44.match(line)
            if m:
                groups = m.groupdict()
                received_total_packets = int(groups['received_total_packets'])
                ip_dict['received_total_packets'] = received_total_packets
                continue

            # Rcvd invalid vrf:                                      0
            m = p45.match(line)
            if m:
                groups = m.groupdict()
                received_invalid_vrf = int(groups['received_invalid_vrf'])
                ip_dict['received_invalid_vrf'] = received_invalid_vrf
                continue

            # Rcvd invalid IP header:                                0
            m = p46.match(line)
            if m:
                groups = m.groupdict()
                received_invalid_ip_header = int(groups['received_invalid_ip_header'])
                ip_dict['received_invalid_ip_header'] = received_invalid_ip_header
                continue

            # Rcvd invalid protocol:                                 0
            m = p47.match(line)
            if m:
                groups = m.groupdict()
                received_invalid_protocol = int(groups['received_invalid_protocol'])
                ip_dict['received_invalid_protocol'] = received_invalid_protocol
                continue

            # Rcvd invalid size:                                     0
            m = p48.match(line)
            if m:
                groups = m.groupdict()
                received_invalid_size = int(groups['received_invalid_size'])
                ip_dict['received_invalid_size'] = received_invalid_size
                continue

            # Rcvd invalid port:                                     0
            m = p49.match(line)
            if m:
                groups = m.groupdict()
                received_invalid_port = int(groups['received_invalid_port'])
                ip_dict['received_invalid_port'] = received_invalid_port
                continue

            # Rcvd invalid checksum:                                 0
            m = p50.match(line)
            if m:
                groups = m.groupdict()
                received_invalid_checksum = int(groups['received_invalid_checksum'])
                ip_dict['received_invalid_checksum'] = received_invalid_checksum
                continue

            # Rcvd unsupported LISP:                                 0
            m = p51.match(line)
            if m:
                groups = m.groupdict()
                received_unsupported_lisp = int(groups['received_unsupported_lisp'])
                ip_dict['received_unsupported_lisp'] = received_unsupported_lisp
                continue

            # Rcvd not LISP control:                                 0
            m = p52.match(line)
            if m:
                groups = m.groupdict()
                received_not_lisp_control = int(groups['received_not_lisp_control'])
                ip_dict['received_not_lisp_control'] = received_not_lisp_control
                continue

            # Rcvd unknown LISP control:                             0
            m = p53.match(line)
            if m:
                groups = m.groupdict()
                received_unknown_lisp_control = int(groups['received_unknown_lisp_control'])
                ip_dict['received_unknown_lisp_control'] = received_unknown_lisp_control
                continue

            # Sent total packets:                                    0
            m = p54.match(line)
            if m:
                groups = m.groupdict()
                sent_total = int(groups['sent_total'])
                ip_dict['sent_total'] = sent_total
                continue

            # Sent flow controlled:                                  0
            m = p55.match(line)
            if m:
                groups = m.groupdict()
                sent_flow_controlled = int(groups['sent_flow_controlled'])
                ip_dict['sent_flow_controlled'] = sent_flow_controlled
                continue
        return ret_dict


class ShowLispExtranetSummarySchema(MetaParser):

    ''' Schema for "show lisp extranet summary" '''

    schema = {
          'lisp_id': {
              int: {
                    'total_extranets': int,
                    'max_allowed_ipv4_prefix' : int,
                    'total_ipv4_prefix':int,
                    'max_allowed_ipv6_prefix' : int,
                    'total_ipv6_prefix':int, 
                    'extranet_name': {
                        str: {
                            'provider_iid': int,
                            'provider_ipv4_prefix_count': int,
                            'provider_ipv6_prefix_count': int,
                            'provider_total_prefix_count': int,
                            'subscriber_inst_count': int,
                            'subscriber_ipv4_prefix_count': int,
                            'subscriber_ipv6_prefix_count': int,
                            'subscriber_total_prefix_count': int,
                            'total_ipv4_prefix_count': int,
                            'total_ipv6_prefix_count': int,
                            'total_prefix_count': int,
                            },
                        },
                    },
                },
             }

# ==============================
# Parser for 'show lisp extranet summary'
# ==============================
class ShowLispExtranetSummary(ShowLispExtranetSummarySchema):

    ''' Parser for "show lisp extranet summary" '''

    cli_command = ["show lisp extranet summary",
                   "show lisp {lisp_id} extranet summary"]

    def cli(self, lisp_id=None, output=None):
        if not output:
            if lisp_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id))
            else:
                output = self.device.execute(self.cli_command[0])
        
        parsed_dict = {}

        # Total extranets: 1
        p1 = re.compile(r"^Total\sextranets:\s+(?P<total_ext>\d+)")

        # Max allowed Extranet IPV4 EID prefixes: 4294967295
        p2 = re.compile(r"^Max\sallowed\sExtranet\sIPV4\sEID\sprefixes:\s+(?P<MAX_ALLOWED_IPV4_PREFIX>\d+)")

        # Total Extranet IPV4 EID prefixes      : 4
        p3 = re.compile(r"^Total\sExtranet\sIPV4\sEID\sprefixes\s+:\s+(?P<TOTAL_IPV4_PREFIX>\d+)")

        # Max allowed Extranet IPV6 EID prefixes: 4294967295
        p4 = re.compile(r"^Max\sallowed\sExtranet\sIPV6\sEID\sprefixes:\s+(?P<MAX_ALLOWED_IPV6_PREFIX>\d+)")

        # Total Extranet IPV6 EID prefixes      : 0
        p5 = re.compile(r"^Total\sExtranet\sIPV6\sEID\sprefixes\s+:\s+(?P<TOTAL_IPV6_PREFIX>\d+)")

        # Extranet name: ext1
        p6 = re.compile(r"^\s*Extranet\sname:\s+(?P<EXTRANET_NAME>\S+)")

        # Provider Instance ID : 111
        p7 = re.compile(r"^Provider\sInstance ID\s+:\s+(?P<PROVIDER_IID>\d+)")

        # Total Provider IPV4 EID prefixes : 0
        p8 = re.compile(r"^Total\sProvider\sIPV4\sEID\sprefixes\s+:\s+(?P<PROVIDER_IPV4_PREFIX_COUNT>\d+)")

        # Total Provider IPV6 EID prefixes : 0
        p9 = re.compile(r"^Total\sProvider\sIPV6\sEID\sprefixes\s+:\s+(?P<PROVIDER_IPV6_PREFIX_COUNT>\d+)")

        # Total Provider EID prefixes : 0
        p10 = re.compile(r"^Total\sProvider\sEID\sprefixes\s+:\s+(?P<PROVIDER_TOTAL_PREFIX_COUNT>\d+)")

        # Total Subscriber Instances : 1
        p11 = re.compile(r"^Total\sSubscriber\sInstances\s+:\s+(?P<SUBSCRIBER_INST_COUNT>\d+)")

        # Total Subscriber IPV4 EID prefixes  : 4
        p12 = re.compile(r"^Total\sSubscriber\sIPV4\sEID\sprefixes\s+:\s+(?P<SUBSCRIBER_IPV4_PREFIX_COUNT>\d+)")

        # Total Subscriber IPV6 EID prefixes  : 0
        p13 = re.compile(r"^Total\sSubscriber\sIPV6\sEID\sprefixes\s+:\s+(?P<SUBSCRIBER_IPV6_PREFIX_COUNT>\d+)")

        # Total Subscriber EID prefixes : 4
        p14 = re.compile(r"^Total\sSubscriber\sEID\sprefixes\s+:\s+(?P<SUBSCRIBER_TOTAL_PREFIX_COUNT>\d+)")

        # Total IPV4 EID prefixes  : 4
        p15 = re.compile(r"^Total\sIPV4\sEID\sprefixes\s+:\s+(?P<TOTAL_IPV4_PREFIX_COUNT>\d+)")

        # Total IPV6 EID prefixes  : 0
        p16 = re.compile(r"^Total\sIPV6\sEID\sprefixes\s+:\s+(?P<TOTAL_IPV6_PREFIX_COUNT>\d+)")

        # Total EID prefixes  : 4
        p17 = re.compile(r"^Total\sEID\sprefixes\s+:\s+(?P<TOTAL_PREFIX_COUNT>\d+)")

        for line in output.splitlines():
            line = line.strip()

            if not lisp_id:
                lisp_id = 0
            else:
                lisp_id = int(lisp_id)
            
            lisp_id_dict = parsed_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
            
            # Total extranets: 1
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                total_ext = int(groups['total_ext'])
                lisp_id_dict.update({'total_extranets': total_ext})
                continue

            # Max allowed Extranet IPV4 EID prefixes: 4294967295
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                max_allowed_ipv4_prefix = int(groups['MAX_ALLOWED_IPV4_PREFIX'])
                lisp_id_dict.update({'max_allowed_ipv4_prefix': max_allowed_ipv4_prefix})
                continue

            # Total Extranet IPV4 EID prefixes      : 4
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                total_ipv4_prefix = int(groups['TOTAL_IPV4_PREFIX'])
                lisp_id_dict.update({'total_ipv4_prefix': total_ipv4_prefix})
                continue

            # Max allowed Extranet IPV6 EID prefixes: 4294967295
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                max_allowed_ipv6_prefix = int(groups['MAX_ALLOWED_IPV6_PREFIX'])
                lisp_id_dict.update({'max_allowed_ipv6_prefix': max_allowed_ipv6_prefix})
                continue
            
            # Total Extranet IPV6 EID prefixes      : 0
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                total_ipv6_prefix = int(groups['TOTAL_IPV6_PREFIX'])
                lisp_id_dict.update({'total_ipv6_prefix': total_ipv6_prefix})
                continue
            
            # Extranet name: ext1
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                ext_name = groups['EXTRANET_NAME']
                ext_dict = lisp_id_dict.setdefault('extranet_name', {}).setdefault(ext_name, {})
                continue
            
            # Provider Instance ID: 111
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                prov_iid = int(groups['PROVIDER_IID'])
                ext_dict.update({'provider_iid': prov_iid})

            # Total Provider IPV4 EID prefixes : 0
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                provider_ipv4_prefix_count = int(groups['PROVIDER_IPV4_PREFIX_COUNT'])
                ext_dict.update({'provider_ipv4_prefix_count': provider_ipv4_prefix_count})
            
            # Total Provider IPV6 EID prefixes : 0
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                provider_ipv6_prefix_count = int(groups['PROVIDER_IPV6_PREFIX_COUNT'])
                ext_dict.update({'provider_ipv6_prefix_count': provider_ipv6_prefix_count})

            # Total Provider EID prefixes : 0
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                provider_total_prefix_count = int(groups['PROVIDER_TOTAL_PREFIX_COUNT'])
                ext_dict.update({'provider_total_prefix_count': provider_total_prefix_count})

            # Total Subscriber Instances : 1    
            m = p11.match(line)   
            if m:
                groups = m.groupdict()
                subscriber_inst_count = int(groups['SUBSCRIBER_INST_COUNT'])
                ext_dict.update({'subscriber_inst_count': subscriber_inst_count})  
            
            # Total Subscriber IPV4 EID prefixes  : 4
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                subscriber_ipv4_prefix_count = int(groups['SUBSCRIBER_IPV4_PREFIX_COUNT'])
                ext_dict.update({'subscriber_ipv4_prefix_count': subscriber_ipv4_prefix_count})   
            
            # Total Subscriber IPV6 EID prefixes  : 0
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                subscriber_ipv6_prefix_count = int(groups['SUBSCRIBER_IPV6_PREFIX_COUNT'])
                ext_dict.update({'subscriber_ipv6_prefix_count': subscriber_ipv6_prefix_count}) 
            
            # Total Subscriber EID prefixes  : 4
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                subscriber_total_prefix_count = int(groups['SUBSCRIBER_TOTAL_PREFIX_COUNT'])
                ext_dict.update({'subscriber_total_prefix_count': subscriber_total_prefix_count}) 

            # Total IPV4 EID prefixes : 4
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                total_ipv4_prefix_count = int(groups['TOTAL_IPV4_PREFIX_COUNT'])
                ext_dict.update({'total_ipv4_prefix_count': total_ipv4_prefix_count}) 

            # Total IPV6 EID prefixes  : 0
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                total_ipv6_prefix_count = int(groups['TOTAL_IPV6_PREFIX_COUNT'])
                ext_dict.update({'total_ipv6_prefix_count': total_ipv6_prefix_count})

            # Total EID prefixes : 4
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                total_prefix_count = int(groups['TOTAL_PREFIX_COUNT'])
                ext_dict.update({'total_prefix_count': total_prefix_count})

        return parsed_dict


class ShowLispSiteDetailSuperParserSchema(MetaParser):

    ''' Schema for
        *  show lisp site detail
        *  show lisp site name {site_name}
        *  show lisp site {eid}
        *  show lisp site {eid} instance-id {instance_id}
        *  show lisp site {eid} eid-table {eid_table}
        *  show lisp site {eid} eid-table vrf {vrf}
        *  show lisp {lisp_id} site detail
        *  show lisp {lisp_id} site name {site_name}
        *  show lisp {lisp_id} site {eid}
        *  show lisp {lisp_id} site {eid} instance-id {instance_id}
        *  show lisp {lisp_id} site {eid} eid-table {eid_table}
        *  show lisp {lisp_id} site {eid} eid-table vrf {vrf}
        *  show lisp locator-table {locator_table} site detail
        *  show lisp locator-table {locator_table} site name {site_name}
        *  show lisp locator-table {locator_table} site {eid}
        *  show lisp locator-table {locator_table} site {eid} instance-id {instance_id}
        *  show lisp locator-table {locator_table} site {eid} eid-table {eid_table}
        *  show lisp locator-table {locator_table} site {eid} eid-table vrf {vrf}
    '''
    schema = {
        'lisp_id': {
            int: {
                'site_name': {
                    str: {
                        'instance_id': {
                            int: {
                                'eid_prefix': {
                                    str: {
                                        'first_registered': str,
                                        'last_registered': str,
                                        Optional('routing_table_tag'): int,
                                        'origin': str,
                                        'merge_active': str,
                                        'proxy_reply': str,
                                        Optional('skip_publication'): str,
                                        Optional('force_withdraw'): str,
                                        'ttl': str,
                                        'state': str,
                                        Optional('extranet_iid'): str,
                                        'registration_erros': {
                                            'authentication_failures': int,
                                            'allowed_locators_mismatch': int
                                            },
                                        'etr': {
                                            str: {
                                                'port': int,
                                                'last_registered': str,
                                                'proxy_reply': bool,
                                                'map_notify': bool,
                                                'ttl': str,
                                                'nonce': str,
                                                'state': str,
                                                'xtr_id': str,
                                                Optional('domain_id'): str,
                                                Optional('multihoming_id'): str,
                                                'locators': {
                                                    str: {
                                                        'local': str,
                                                        'state': str, 
                                                        'priority': int,
                                                        'weight': int,
                                                        'scope': str
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
            }
        }


class ShowLispSiteDetailSuperParser(ShowLispSiteDetailSuperParserSchema):

    def cli(self, output=None, lisp_id=None, eid=None, instance_id=None, eid_table=None,
            vrf=None, locator_table=None, site_name=None, prefix=None):
        ret_dict = {}

        # Output for router lisp 0
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)$")

        # Site name: Shire
        p2 = re.compile(r"^Site\s+name:\s+(?P<site_name>\S+)$")

        # EID-prefix: 1.1.1.0/24 instance-id 0
        # EID-prefix: 2001:192:168:1::1/64 instance-id 0
        # EID-prefix: aabb.cc00.c901/48 instance-id 101
        p3 = re.compile(r"^EID-prefix:\s+(?P<eid_prefix>\d{1,3}\.\d{1,3}\."
                        r"\d{1,3}\.\d{1,3}\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3}"
                        r"|([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{1,3})\s+"
                        r"instance-id\s+(?P<instance_id>\d+)$")

        # First registered:     never
        p4 = re.compile(r"^First\s+registered:\s+"
                        r"(?P<first_registered>\d{1,2}:\d{2}:\d{2}|\dw\dd|never)$")

        # Last registered:      00:45:46
        p5 = re.compile(r"^Last\s+registered:\s+"
                        r"(?P<last_registered>\d{1,2}:\d{2}:\d{2}|\dw\dd|never)$")

        # Routing table tag:    0
        p6 = re.compile(r"^Routing\s+table\s+tag:\s+(?P<routing_table_tag>\d+)$")

        # Origin:               Dynamic, more specific of 192.168.1.0/24
        p7 = re.compile(r"^Origin:\s+(?P<origin>[\d:\.\/\w\s,\W]+)$")

        # Merge active:         No
        p8 = re.compile(r"^Merge\s+active:\s+(?P<merge_active>Yes|No)$")

        # Proxy reply:          No
        p9 = re.compile(r"^Proxy\s+reply:\s+(?P<proxy_reply>Yes|No)$")

        # Skip Publication:     No
        p10 = re.compile(r"^Skip\s+Publication:\s+(?P<skip_publication>Yes|No)$")

        # Force Withdraw:       No
        p11 = re.compile(r"^Force\s+Withdraw:\s+(?P<force_withdraw>Yes|No)$")

        # TTL:                  00:00:00
        p12 = re.compile(r"^TTL:\s+(?P<ttl>\S+)$")

        # State:                unknown
        p13 = re.compile(r"^State:\s+(?P<state>\S+)$")

        # Extranet IID:         Unspecified
        p14 = re.compile(r"^Extranet\s+IID:\s+(?P<extranet_iid>\S+)$")

        # Authentication failures:   0
        p15 = re.compile(r"^Authentication\s+failures:\s+(?P<authentication_failures>\d+)$")

        # Allowed locators mismatch: 0
        p16 = re.compile(r"^Allowed\s+locators\s+mismatch:\s+(?P<allowed_locators_mismatch>\d+)$")

        # ETR 11.11.11.11:33079, last registered 00:45:46, proxy-reply, map-notify
        p17 = re.compile(r"^ETR\s+(?P<etr>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(?P<port>\d+),"
                         r"\s+last\s+registered\s+(?P<last_registered>\d{1,2}:\d{2}:\d{2}|\dw\dd),"
                         r"\s+(?P<proxy_reply>proxy-reply),\s+(?P<map_notify>map-notify)$")

        # TTL 1d00h, no merge, hash-function sha1, nonce 0x4536735E-0xE5D90458
        p18 = re.compile(r"^TTL\s+(?P<ttl>\S+),\s+no\s+merge,\s+hash-function\s+sha1,"
                         r"\s+nonce\s+(?P<nonce>\S+)$")

        # state complete, no security-capability
        p19 = re.compile(r"^state\s+(?P<state>\S+),\s+no\s+security-capability$")

        # xTR-ID 0xE52CBAD5-0x38D3485F-0x97DC3A75-0xC27B2130
        p20 = re.compile(r"^xTR-ID\s+(?P<xtr_id>\S+)$")

        # Domain-ID local
        p21 = re.compile(r"^Domain-ID\s+(?P<domain_id>local)$")

        # Multihoming-ID unspecified
        p22 = re.compile(r"^Multihoming-ID\s+(?P<multihoming_id>\S+)$")

        # 22.22.22.22  yes    up          10/10   IPv4 none
        p23 = re.compile(r"^(?P<locators>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
                         r"(?P<local>yes|no)\s+(?P<state>\S+)\s+(?P<priority>\d+)"
                         r"\/(?P<weight>\d+)\s+(?P<scope>IPv4)\snone$")

        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})
                continue

            # Site name: Shire
            m = p2.match(line)
            if m:
                if lisp_id != "all":
                    lisp_id = int(lisp_id) if lisp_id else 0
                    lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                groups = m.groupdict()
                site_name = groups['site_name']
                site_dict = lisp_id_dict.setdefault('site_name',{})\
                                        .setdefault(site_name,{})
                continue

            # EID-prefix: 1.1.1.0/24 instance-id 0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                eid_prefix = groups['eid_prefix']
                instance_id = int(groups['instance_id'])
                instance_dict = site_dict.setdefault('instance_id',{})\
                                         .setdefault(instance_id,{})\
                                         .setdefault('eid_prefix',{})\
                                         .setdefault(eid_prefix,{})
                continue

            # First registered:     00:45:45
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                first_registered = groups['first_registered']
                instance_dict.update({'first_registered':first_registered})
                continue

            # Last registered:      00:45:42
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                last_registered = groups['last_registered']
                instance_dict.update({'last_registered':last_registered})
                continue

            # Routing table tag:    0
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                routing_table_tag = int(groups['routing_table_tag'])
                instance_dict.update({'routing_table_tag':routing_table_tag})
                continue

            # Origin:               Dynamic, more specific of 194.168.1.0/24
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                origin = groups['origin']
                instance_dict.update({'origin':origin})
                continue

            # Merge active:         No
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                merge_active = groups['merge_active']
                instance_dict.update({'merge_active':merge_active})
                continue

            # Proxy reply:          Yes
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                proxy_reply = groups['proxy_reply']
                instance_dict.update({'proxy_reply':proxy_reply})
                continue

            # Skip Publication:     No
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                skip_publication = groups['skip_publication']
                instance_dict.update({'skip_publication':skip_publication})
                continue

            # Force Withdraw:       No
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                force_withdraw = groups['force_withdraw']
                instance_dict.update({'force_withdraw':force_withdraw})
                continue

            # TTL:                  1d00h
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                ttl = groups['ttl']
                instance_dict.update({'ttl':ttl})
                continue

            # State:                complete
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                state = groups['state']
                instance_dict.update({'state':state})
                continue

            # Extranet IID:         Unspecified
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                extranet_iid = groups['extranet_iid']
                instance_dict.update({'extranet_iid':extranet_iid})
                continue

            # Authentication failures:   0
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                authentication_failures = int(groups['authentication_failures'])
                registered_dict = instance_dict.setdefault('registration_erros',{})
                registered_dict.update({'authentication_failures':authentication_failures})
                continue

            # Allowed locators mismatch: 0
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                allowed_locators_mismatch = int(groups['allowed_locators_mismatch'])
                registered_dict.update({'allowed_locators_mismatch':allowed_locators_mismatch})
                continue

            # ETR 22.22.22.22:27643, last registered 00:45:42, proxy-reply, map-notify
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                etr = groups['etr']
                port = int(groups['port'])
                last_registered = groups['last_registered']
                proxy_reply = groups['proxy_reply']
                map_notify = groups['map_notify']
                proxy_reply_bool = bool(re.search("proxy-reply",proxy_reply))
                map_notify_bool = bool(re.search("map-notify",map_notify))
                etr_dict = instance_dict.setdefault('etr',{})\
                                        .setdefault(etr,{})
                etr_dict.update({'port':port,
                                 'last_registered':last_registered,
                                 'proxy_reply':proxy_reply_bool,
                                 'map_notify':map_notify_bool})
                continue

            # TTL 1d00h, no merge, hash-function sha1, nonce 0xC7E970BF-0x125C7F7B
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                ttl = groups['ttl']
                nonce = groups['nonce']
                etr_dict.update({'ttl':ttl,
                                 'nonce':nonce})
                continue

            # state complete, no security-capability
            m = p19.match(line)
            if m:
                groups = m.groupdict()
                state = groups['state']
                etr_dict.update({'state':state})
                continue

            # xTR-ID 0xE52CBAD5-0x38D3485F-0x97DC3A75-0xC27B2130
            m = p20.match(line)
            if m:
                groups = m.groupdict()
                xtr_id = groups['xtr_id']
                etr_dict.update({'xtr_id':xtr_id})
                continue

            # Domain-ID local
            m = p21.match(line)
            if m:
                groups = m.groupdict()
                domain_id = groups['domain_id']
                etr_dict.update({'domain_id':domain_id})
                continue

            # Multihoming-ID unspecified
            m = p22.match(line)
            if m:
                groups = m.groupdict()
                multihoming_id = groups['multihoming_id']
                etr_dict.update({'multihoming_id':multihoming_id})
                continue

            # 22.22.22.22  yes    up          10/10   IPv4 none
            m = p23.match(line)
            if m:
                groups = m.groupdict()
                locators = groups['locators']
                local = groups['local']
                state = groups['state']
                priority = int(groups['priority'])
                weight = int(groups['weight'])
                scope = groups['scope']
                locators_dict = etr_dict.setdefault('locators',{})\
                                        .setdefault(locators,{})
                locators_dict.update({'local':local,
                                      'state':state,
                                      'priority':priority,
                                      'weight':weight,
                                      'scope':scope})
                continue
        return ret_dict


class ShowLispSiteDetail(ShowLispSiteDetailSuperParser):
    ''' Parser for
        *  show lisp site detail
        *  show lisp site name {site_name}
        *  show lisp site {eid}
        *  show lisp site {eid} instance-id {instance_id}
        *  show lisp site {eid} eid-table {eid_table}
        *  show lisp site {eid} eid-table vrf {vrf}
        *  show lisp {lisp_id} site detail
        *  show lisp {lisp_id} site name {site_name}
        *  show lisp {lisp_id} site {eid}
        *  show lisp {lisp_id} site {eid} instance-id {instance_id}
        *  show lisp {lisp_id} site {eid} eid-table {eid_table}
        *  show lisp {lisp_id} site {eid} eid-table vrf {vrf}
        *  show lisp locator-table {locator_table} site detail
        *  show lisp locator-table {locator_table} site name {site_name}
        *  show lisp locator-table {locator_table} site {eid}
        *  show lisp locator-table {locator_table} site {eid} instance-id {instance_id}
        *  show lisp locator-table {locator_table} site {eid} eid-table {eid_table}
        *  show lisp locator-table {locator_table} site {eid} eid-table vrf {vrf}
    '''
    cli_command = ['show lisp site detail',
                   'show lisp site name {site_name}',
                   'show lisp site {eid}',
                   'show lisp site {eid} instance-id {instance_id}',
                   'show lisp site {eid} eid-table {eid_table}',
                   'show lisp site {eid} eid-table vrf {vrf}',
                   'show lisp {lisp_id} site detail',
                   'show lisp {lisp_id} site name {site_name}',
                   'show lisp {lisp_id} site {eid}',
                   'show lisp {lisp_id} site {eid} instance-id {instance_id}',
                   'show lisp {lisp_id} site {eid} eid-table {eid_table}',
                   'show lisp {lisp_id} site {eid} eid-table vrf {vrf}',
                   'show lisp locator-table {locator_table} site detail',
                   'show lisp locator-table {locator_table} site name {site_name}',
                   'show lisp locator-table {locator_table} site {eid}',
                   'show lisp locator-table {locator_table} site {eid} instance-id {instance_id}',
                   'show lisp locator-table {locator_table} site {eid} eid-table {eid_table}',
                   'show lisp locator-table {locator_table} site {eid} eid-table vrf {vrf}']

    def cli(self, output=None, lisp_id=None, eid=None, instance_id=None, eid_table=None,
            vrf=None, locator_table=None, site_name=None):

        if output is None:
            if lisp_id and instance_id and eid:
                output = self.device.execute(self.cli_command[9].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, eid=eid))
            elif lisp_id and eid and eid_table:
                 output = self.device.execute(self.cli_command[10].\
                                             format(lisp_id=lisp_id, eid=eid, eid_table=eid_table))
            elif lisp_id and eid and vrf:
                 output = self.device.execute(self.cli_command[11].\
                                             format(lisp_id=lisp_id, eid=eid, vrf=vrf))
            elif locator_table and instance_id and eid:
                output = self.device.execute(self.cli_command[15].\
                                            format(locator_table=locator_table, instance_id=instance_id, eid=eid))
            elif locator_table and eid_table and eid:
                output = self.device.execute(self.cli_command[16].\
                                            format(locator_table=locator_table, eid_table=eid_table, eid=eid))
            elif locator_table and vrf and eid:
                output = self.device.execute(self.cli_command[17].\
                                            format(locator_table=locator_table, vrf=vrf, eid=eid))
            elif locator_table and eid:
                output = self.device.execute(self.cli_command[14].\
                                            format(locator_table=locator_table, eid=eid))
            elif locator_table and site_name:
                output = self.device.execute(self.cli_command[13].\
                                            format(locator_table=locator_table, site_name=site_name))
            elif lisp_id and eid:
                output = self.device.execute(self.cli_command[8].\
                                            format(lisp_id=lisp_id, eid=eid))
            elif lisp_id and site_name:
                output = self.device.execute(self.cli_command[7].\
                                            format(lisp_id=lisp_id, site_name=site_name))
            elif eid and instance_id:
                output = self.device.execute(self.cli_command[3].\
                                            format(eid=eid, instance_id=instance_id))
            elif eid and eid_table:
                output = self.device.execute(self.cli_command[4].\
                                            format(eid=eid, eid_table=eid_table))
            elif eid and vrf:
                output = self.device.execute(self.cli_command[5].\
                                            format(eid=eid, vrf=vrf))
            elif eid:
                output = self.device.execute(self.cli_command[2].format(eid=eid))
            elif lisp_id:
                output = self.device.execute(self.cli_command[6].format(lisp_id=lisp_id))
            elif locator_table:
                output = self.device.execute(self.cli_command[12].format(locator_table=locator_table))
            elif site_name:
                output = self.device.execute(self.cli_command[1].format(site_name=site_name))
            else:
                output = self.device.execute(self.cli_command[0])
        return super().cli(output=output)


class ShowLispEthernetServerDetail(ShowLispSiteDetailSuperParser):
    ''' Parser for
        * show lisp instance-id {instance_id} ethernet server detail
        * show lisp instance-id {instance_id} ethernet server name {site_name}
        * show lisp instance-id {instance_id} ethernet server {eid}
        * show lisp instance-id {instance_id} ethernet server etr-address {etr_address}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server detail
        * show lisp {lisp_id} instance-id {instance_id} ethernet server name {site_name}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server {eid}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server etr-address {etr_address}
        * show lisp eid-table vrf {vrf} ethernet server detail
        * show lisp eid-table vrf {vrf} ethernet server name {site_name}
        * show lisp eid-table vrf {vrf} ethernet server {eid}
        * show lisp eid-table vrf {vrf} ethernet server etr-address {etr_address}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server name {site_name}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server etr-address {etr_address}
    '''
    cli_command = ['show lisp instance-id {instance_id} ethernet server detail',
                   'show lisp instance-id {instance_id} ethernet server name {site_name}',
                   'show lisp instance-id {instance_id} ethernet server {eid}',
                   'show lisp instance-id {instance_id} ethernet server etr-address {etr_address}',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet server detail',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet server name {site_name}',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet server {eid}',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet server etr-address {etr_address}',
                   'show lisp eid-table vrf {vrf} ethernet server detail',
                   'show lisp eid-table vrf {vrf} ethernet server name {site_name}',
                   'show lisp eid-table vrf {vrf} ethernet server {eid}',
                   'show lisp eid-table vrf {vrf} ethernet server etr-address {etr_address}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ethernet server detail',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ethernet server name {site_name}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ethernet server {eid}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ethernet server etr-address {etr_address}']
    def cli(self, output=None, lisp_id=None, eid=None, instance_id=None, eid_table=None,
            vrf=None, locator_table=None, site_name=None, etr_address=None):

        if output is None:
            if locator_table and instance_id and site_name:
                output = self.device.execute(self.cli_command[13].\
                                            format(locator_table=locator_table, instance_id=instance_id, site_name=site_name))
            elif locator_table and instance_id and eid:
                output = self.device.execute(self.cli_command[14].\
                                            format(locator_table=locator_table, instance_id=instance_id, eid=eid))
            elif locator_table and instance_id and etr_address:
                output = self.device.execute(self.cli_command[15].\
                                            format(locator_table=locator_table, instance_id=instance_id, etr_address=etr_address))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[12].\
                                            format(locator_table=locator_table, instance_id=instance_id))
            elif lisp_id and instance_id and site_name:
                output = self.device.execute(self.cli_command[5].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, site_name=site_name))
            elif lisp_id and instance_id and eid:
                output = self.device.execute(self.cli_command[6].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, eid=eid))
            elif lisp_id and instance_id and etr_address:
                output = self.device.execute(self.cli_command[7].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, etr_address=etr_address))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[4].\
                                            format(lisp_id=lisp_id, instance_id=instance_id))
            elif etr_address and instance_id:
                output = self.device.execute(self.cli_command[3].\
                                            format(etr_address=etr_address, instance_id=instance_id))
            elif eid and instance_id:
                output = self.device.execute(self.cli_command[2].\
                                            format(eid=eid, instance_id=instance_id))
            elif site_name and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(site_name=site_name, instance_id=instance_id))
            elif etr_address and vrf:
                output = self.device.execute(self.cli_command[11].\
                                            format(etr_address=etr_address, vrf=vrf))
            elif eid and vrf:
                output = self.device.execute(self.cli_command[10].\
                                            format(eid=eid, vrf=vrf))
            elif site_name and vrf:
                output = self.device.execute(self.cli_command[9].\
                                            format(site_name=site_name, vrf=vrf))
            elif vrf:
                output = self.device.execute(self.cli_command[8].\
                                            format(vrf=vrf))
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id))
        return super().cli(output=output)


class ShowLispIpv4ServerDetail(ShowLispSiteDetailSuperParser):
    ''' Parser for
        * show lisp instance-id {instance_id} ipv4 server detail
        * show lisp instance-id {instance_id} ipv4 server name {site_name}
        * show lisp instance-id {instance_id} ipv4 server {eid}
        * show lisp instance-id {instance_id} ipv4 server etr-address {etr_address}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server detail
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server name {site_name}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server {eid}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server etr-address {etr_address}
        * show lisp eid-table {eid_table} ipv4 server detail
        * show lisp eid-table {eid_table} ipv4 server name {site_name}
        * show lisp eid-table {eid_table} ipv4 server {eid}
        * show lisp eid-table {eid_table} ipv4 server etr-address {etr_address}
        * show lisp eid-table vrf {vrf} ipv4 server detail
        * show lisp eid-table vrf {vrf} ipv4 server name {site_name}
        * show lisp eid-table vrf {vrf} ipv4 server {eid}
        * show lisp eid-table vrf {vrf} ipv4 server etr-address {etr_address}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server name {site_name}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server etr-address {etr_address}
    '''
    cli_command = ['show lisp instance-id {instance_id} ipv4 server detail',
                   'show lisp instance-id {instance_id} ipv4 server name {site_name}',
                   'show lisp instance-id {instance_id} ipv4 server {eid}',
                   'show lisp instance-id {instance_id} ipv4 server etr-address {etr_address}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server detail',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server name {site_name}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server {eid}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server etr-address {etr_address}',
                   'show lisp eid-table vrf {vrf} ipv4 server detail',
                   'show lisp eid-table vrf {vrf} ipv4 server name {site_name}',
                   'show lisp eid-table vrf {vrf} ipv4 server {eid}',
                   'show lisp eid-table vrf {vrf} ipv4 server etr-address {etr_address}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server detail',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server name {site_name}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server {eid}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server etr-address {etr_address}',
                   'show lisp eid-table {eid_table} ipv4 server detail',
                   'show lisp eid-table {eid_table} ipv4 server name {site_name}',
                   'show lisp eid-table {eid_table} ipv4 server {eid}',
                   'show lisp eid-table {eid_table} ipv4 server etr-address {etr_address}']

    def cli(self, output=None, lisp_id=None, eid=None, instance_id=None, eid_table=None,
            vrf=None, locator_table=None, site_name=None, etr_address=None):

        if output is None:
            if locator_table and instance_id and site_name:
                output = self.device.execute(self.cli_command[13].\
                                            format(locator_table=locator_table, instance_id=instance_id, site_name=site_name))
            elif locator_table and instance_id and eid:
                output = self.device.execute(self.cli_command[14].\
                                            format(locator_table=locator_table, instance_id=instance_id, eid=eid))
            elif locator_table and instance_id and etr_address:
                output = self.device.execute(self.cli_command[15].\
                                            format(locator_table=locator_table, instance_id=instance_id, etr_address=etr_address))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[12].\
                                            format(locator_table=locator_table, instance_id=instance_id))
            elif lisp_id and instance_id and site_name:
                output = self.device.execute(self.cli_command[5].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, site_name=site_name))
            elif lisp_id and instance_id and eid:
                output = self.device.execute(self.cli_command[6].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, eid=eid))
            elif lisp_id and instance_id and etr_address:
                output = self.device.execute(self.cli_command[7].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, etr_address=etr_address))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[4].\
                                            format(lisp_id=lisp_id, instance_id=instance_id))
            elif etr_address and instance_id:
                output = self.device.execute(self.cli_command[3].\
                                            format(etr_address=etr_address, instance_id=instance_id))
            elif eid and instance_id:
                output = self.device.execute(self.cli_command[2].\
                                            format(eid=eid, instance_id=instance_id))
            elif site_name and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(site_name=site_name, instance_id=instance_id))
            elif etr_address and vrf:
                output = self.device.execute(self.cli_command[11].\
                                            format(etr_address=etr_address, vrf=vrf))
            elif eid and vrf:
                output = self.device.execute(self.cli_command[10].\
                                            format(eid=eid, vrf=vrf))
            elif site_name and vrf:
                output = self.device.execute(self.cli_command[9].\
                                            format(site_name=site_name, vrf=vrf))
            elif vrf:
                output = self.device.execute(self.cli_command[8].\
                                            format(vrf=vrf))
            elif eid_table and site_name:
                output = self.device.execute(self.cli_command[17].\
                                            format(eid_table=eid_table, site_name=site_name))
            elif eid_table and eid:
                output = self.device.execute(self.cli_command[18].\
                                            format(eid_table=eid_table, eid=eid))
            elif eid_table and etr_address:
                output = self.device.execute(self.cli_command[19].\
                                            format(eid_table=eid_table, etr_address=etr_address))
            elif eid_table:
                output = self.device.execute(self.cli_command[16].\
                                            format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id))
        return super().cli(output=output)


class ShowLispIpv6ServerDetail(ShowLispSiteDetailSuperParser):
    ''' Parser for
        * show lisp instance-id {instance_id} ipv6 server detail
        * show lisp instance-id {instance_id} ipv6 server name {site_name}
        * show lisp instance-id {instance_id} ipv6 server {eid}
        * show lisp instance-id {instance_id} ipv6 server etr-address {etr_address}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server detail
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server name {site_name}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server {eid}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server etr-address {etr_address}
        * show lisp eid-table {eid_table} ipv6 server detail
        * show lisp eid-table {eid_table} ipv6 server name {site_name}
        * show lisp eid-table {eid_table} ipv6 server {eid}
        * show lisp eid-table {eid_table} ipv6 server etr-address {etr_address}
        * show lisp eid-table vrf {vrf} ipv6 server detail
        * show lisp eid-table vrf {vrf} ipv6 server name {site_name}
        * show lisp eid-table vrf {vrf} ipv6 server {eid}
        * show lisp eid-table vrf {vrf} ipv6 server etr-address {etr_address}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server name {site_name}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server etr-address {etr_address}
    '''
    cli_command = ['show lisp instance-id {instance_id} ipv6 server detail',
                   'show lisp instance-id {instance_id} ipv6 server name {site_name}',
                   'show lisp instance-id {instance_id} ipv6 server {eid}',
                   'show lisp instance-id {instance_id} ipv6 server etr-address {etr_address}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server detail',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server name {site_name}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server {eid}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server etr-address {etr_address}',
                   'show lisp eid-table vrf {vrf} ipv6 server detail',
                   'show lisp eid-table vrf {vrf} ipv6 server name {site_name}',
                   'show lisp eid-table vrf {vrf} ipv6 server {eid}',
                   'show lisp eid-table vrf {vrf} ipv6 server etr-address {etr_address}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server detail',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server name {site_name}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server {eid}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server etr-address {etr_address}',
                   'show lisp eid-table {eid_table} ipv6 server detail',
                   'show lisp eid-table {eid_table} ipv6 server name {site_name}',
                   'show lisp eid-table {eid_table} ipv6 server {eid}',
                   'show lisp eid-table {eid_table} ipv6 server etr-address {etr_address}']

    def cli(self, output=None, lisp_id=None, eid=None, instance_id=None, eid_table=None,
            vrf=None, locator_table=None, site_name=None, etr_address=None):

        if output is None:
            if locator_table and instance_id and site_name:
                output = self.device.execute(self.cli_command[13].\
                                            format(locator_table=locator_table, instance_id=instance_id, site_name=site_name))
            elif locator_table and instance_id and eid:
                output = self.device.execute(self.cli_command[14].\
                                            format(locator_table=locator_table, instance_id=instance_id, eid=eid))
            elif locator_table and instance_id and etr_address:
                output = self.device.execute(self.cli_command[15].\
                                            format(locator_table=locator_table, instance_id=instance_id, etr_address=etr_address))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[12].\
                                            format(locator_table=locator_table, instance_id=instance_id))
            elif lisp_id and instance_id and site_name:
                output = self.device.execute(self.cli_command[5].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, site_name=site_name))
            elif lisp_id and instance_id and eid:
                output = self.device.execute(self.cli_command[6].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, eid=eid))
            elif lisp_id and instance_id and etr_address:
                output = self.device.execute(self.cli_command[7].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, etr_address=etr_address))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[4].\
                                            format(lisp_id=lisp_id, instance_id=instance_id))
            elif etr_address and instance_id:
                output = self.device.execute(self.cli_command[3].\
                                            format(etr_address=etr_address, instance_id=instance_id))
            elif eid and instance_id:
                output = self.device.execute(self.cli_command[2].\
                                            format(eid=eid, instance_id=instance_id))
            elif site_name and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(site_name=site_name, instance_id=instance_id))
            elif etr_address and vrf:
                output = self.device.execute(self.cli_command[11].\
                                            format(etr_address=etr_address, vrf=vrf))
            elif eid and vrf:
                output = self.device.execute(self.cli_command[10].\
                                            format(eid=eid, vrf=vrf))
            elif site_name and vrf:
                output = self.device.execute(self.cli_command[9].\
                                            format(site_name=site_name, vrf=vrf))
            elif vrf:
                output = self.device.execute(self.cli_command[8].\
                                            format(vrf=vrf))
            elif eid_table and site_name:
                output = self.device.execute(self.cli_command[17].\
                                            format(eid_table=eid_table, site_name=site_name))
            elif eid_table and eid:
                output = self.device.execute(self.cli_command[18].\
                                            format(eid_table=eid_table, eid=eid))
            elif eid_table and etr_address:
                output = self.device.execute(self.cli_command[19].\
                                            format(eid_table=eid_table, etr_address=etr_address))
            elif eid_table:
                output = self.device.execute(self.cli_command[16].\
                                            format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id))
        return super().cli(output=output)


class ShowLispRegistrationHistorySchema(MetaParser):
    """
    Schema for 'show lisp {lisp_id} instance-id {instance_id} {address-family} server registration-history'
    """
    schema = {
        'lisp_id': {
            int: {
                'eid_address': {
                    str: ListOf({
                        'time': str,
                        'instance_id': int,
                        'protocol': str,
                        'roam': str,
                        'wlc': str,
                        'source': str,
                        'reg_type': str,
                        'eid': str,
                        'mask': int
                        })
                    }
                }
            }
        }


class ShowLispRegistrationHistory(ShowLispRegistrationHistorySchema):
    """
    Parser for 'show lisp {lisp_id} instance-id {instance_id} {address-family} server registration-history'
    """
    cli_command = ['show lisp {lisp_id} instance-id {instance_id} {address_family} server {eid} registration-history',
                   'show lisp {lisp_id} instance-id {instance_id} {address_family} server registration-history',
                   'show lisp {lisp_id} instance-id {instance_id} {address_family} server {address_resolution} {eid} registration-history',
                   'show lisp {lisp_id} instance-id {instance_id} {address_family} server {address_resolution} registration-history',
                   'show lisp instance-id {instance_id} {address_family} server registration-history',
                   'show lisp server registration-history']

    def cli(self, output=None, lisp_id=None, instance_id=None, address_family=None, eid=None, address_resolution=None):

        if output is None:
            if lisp_id and instance_id and address_family and address_resolution and eid:
                output = self.device.execute(self.cli_command[2].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, address_family=address_family,\
                                                address_resolution=address_resolution, eid=eid))
            elif lisp_id and instance_id and address_family and address_resolution:
                output = self.device.execute(self.cli_command[3].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, address_family=address_family,\
                                                address_resolution=address_resolution))
            elif lisp_id and instance_id and address_family and eid:
                output = self.device.execute(self.cli_command[0].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, address_family=address_family,\
                                                eid=eid))
            elif lisp_id and instance_id and address_family:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, address_family=address_family))
            elif instance_id and address_family:
                output = self.device.execute(self.cli_command[4].\
                                            format(instance_id=instance_id, address_family=address_family))
            else:
                output = self.device.execute(self.cli_command[5])
        ret_dict ={}

        # *Mar  5 20:40:31.737 17476    TCP   No   No  80.80.80.11
        p1 = re.compile(r"^(\*?)(?P<time>([\w:\s\.]+))\s+(?P<instance_id>\d+)\s+"
                        r"(?P<protocol>\S+)\s+(?P<roam>\S+)\s+(?P<wlc>\S+)\s+"
                        r"((?P<source>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[a-fA-F\d\:]+)))$")

        # +*2001:192:168:1::71/128 / aabb.cc00.c901
        # + 0.0.0.0/0
        p2 = re.compile(r"^(?P<reg_type>\+|\-)\*?\s?(?P<eid>([0-9a-fA-F.:]+))"
                        r"\/(?P<mask>\d{1,3})(\s\/\s([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})?$")

        for line in output.splitlines():
            line = line.strip()

            # *Mar  5 20:40:31.737 17476    TCP   No   No  80.80.80.11
            m = p1.match(line)
            if m:
                if lisp_id != "all":
                    lisp_id = int(lisp_id) if lisp_id else 0
                groups = m.groupdict()
                time = groups['time'].strip()
                instance_id = int(groups['instance_id'])
                protocol = groups['protocol']
                roam = groups['roam']
                wlc = groups['wlc']
                source = groups['source']
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})
                continue

            # +*2001:192:168:1::71/128 / aabb.cc00.c901
            # + 0.0.0.0/0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                reg_type = groups['reg_type']
                eid = groups['eid']
                mask = int(groups['mask'])
                eid_address = "{}/{}".format(eid,mask)
                eid_dict = lisp_id_dict.setdefault('eid_address',{})\
                                       .setdefault(eid_address,[])
                eid_dict.append({'time':time,
                                 'instance_id':instance_id,
                                 'protocol':protocol,
                                 'roam':roam,
                                 'wlc':wlc,
                                 'source':source,
                                 'reg_type':reg_type,
                                 'eid':eid,
                                 'mask':mask})
                continue
        return ret_dict


class ShowLispIpv4ServerExtranetPolicyEid(ShowLispSiteDetailSuperParser):
    ''' Parser for
        * show lisp instance-id {instance_id} ipv4 server extranet-policy {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server extranet-policy {prefix}
        * show lisp eid-table {eid_table} ipv4 server extranet-policy {prefix}
        * show lisp eid-table vrf {vrf} ipv4 server extranet-policy {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server extranet-policy {prefix}
    '''
    cli_command = ['show lisp instance-id {instance_id} ipv4 server extranet-policy {prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server extranet-policy {prefix}',
                   'show lisp eid-table {eid_table} ipv4 server extranet-policy {prefix}',
                   'show lisp eid-table vrf {vrf} ipv4 server extranet-policy {prefix}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server extranet-policy {prefix}']

    def cli(self, output=None, lisp_id=None, instance_id=None, eid_table=None, prefix=None, vrf=None, locator_table=None):

        if output is None:
            if locator_table and instance_id and prefix:
                output = self.device.execute(self.cli_command[4].\
                                            format(locator_table=locator_table,
                                                   instance_id=instance_id,
                                                   prefix=prefix))
            elif lisp_id and instance_id and prefix:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id,
                                                   instance_id=instance_id,
                                                   prefix=prefix))
            elif instance_id and prefix:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id,
                                                   prefix=prefix))
            elif vrf and prefix:
                output = self.device.execute(self.cli_command[3].\
                                            format(vrf=vrf,
                                                   prefix=prefix))
            else:
                output = self.device.execute(self.cli_command[2].\
                                            format(eid_table=eid_table,
                                                   prefix=prefix))
        return super().cli(output=output)


class ShowLispIpv6ServerExtranetPolicyEid(ShowLispSiteDetailSuperParser):
    ''' Parser for
        * show lisp instance-id {instance_id} ipv6 server extranet-policy {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server extranet-policy {prefix}
        * show lisp eid-table {eid_table} ipv6 server extranet-policy {prefix}
        * show lisp eid-table vrf {vrf} ipv6 server extranet-policy {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server extranet-policy {prefix}
    '''
    cli_command = ['show lisp instance-id {instance_id} ipv6 server extranet-policy {prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server extranet-policy {prefix}',
                   'show lisp eid-table {eid_table} ipv6 server extranet-policy {prefix}',
                   'show lisp eid-table vrf {vrf} ipv6 server extranet-policy {prefix}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server extranet-policy {prefix}']

    def cli(self, output=None, lisp_id=None, instance_id=None, eid_table=None, prefix=None, vrf=None, locator_table=None):

        if output is None:
            if locator_table and instance_id and prefix:
                output = self.device.execute(self.cli_command[4].\
                                            format(locator_table=locator_table,
                                                   instance_id=instance_id,
                                                   prefix=prefix))
            elif lisp_id and instance_id and prefix:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id,
                                                   instance_id=instance_id,
                                                   prefix=prefix))
            elif instance_id and prefix:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id,
                                                   prefix=prefix))
            elif vrf and prefix:
                output = self.device.execute(self.cli_command[3].\
                                            format(vrf=vrf,
                                                   prefix=prefix))
            else:
                output = self.device.execute(self.cli_command[2].\
                                            format(eid_table=eid_table,
                                                   prefix=prefix))
        return super().cli(output=output)


class ShowLispSchema(MetaParser):
    """
    Schema for 'show lisp'
    """
    schema = {
        'lisp_id': {
            int: {
                Optional('domain_id'): int,
                Optional('multihoming_id'): int,
                'locator_table': str,
                'locator_default_set': str,
                'eid_instance_count': str,
                'capability': ListOf(str),
                'tcp_path_mtu_discovery': bool
                }
            }
        }


class ShowLisp(ShowLispSchema):
    """
    Parser for 'show lisp'
    """
    cli_command = ['show lisp',
                   'show lisp {lisp_id}']

    def cli(self, output=None, lisp_id=None):

        if output is None:
            if lisp_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id))
            else:
                output = self.device.execute(self.cli_command[0])
        ret_dict ={}

        # Output for router lisp 0
        p1 = re.compile(r'^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)$')

        # Router-lisp ID:        0
        p2 = re.compile(r'^Router-lisp\s+ID:\s+(?P<lisp_id>\d+)$')

        # Domain ID:             0
        p3 = re.compile(r'^Domain\s+ID:\s+(?P<domain_id>\d+)$')

        # Multihoming ID:        0
        p4 = re.compile(r'^Multihoming\s+ID:\s+(?P<multihoming_id>\d+)$')

        # Locator table:         default
        p5 = re.compile(r'^Locator\s+table:\s+(?P<locator_table>\S+)$')

        # Locator default-set:   N/A
        p6 = re.compile(r'^Locator\s+default-set:\s+(?P<locator_default_set>\S+)$')

        # EID instance count:    7
        p7 = re.compile(r'^EID\s+instance count:\s+(?P<eid_instance_count>\d+)$')

        # Capability:            Publish-Subscribe Instance-ID
        # Capability:            Domain-Info
        p8 = re.compile(r'^Capability:\s+(?P<capability>Publish-Subscribe\s+Instance-ID|\S+)$')

        # Domain-Info
        p9 = re.compile(r'^(?P<domain>Domain-Info)$')

        # Route-Tag
        p10 = re.compile(r'^(?P<route>Route-Tag)$')

        # SGT
        p11 = re.compile(r'^(?P<sgt>SGT)$')

        # Default-originate
        p12 = re.compile(r'^(?P<default>Default-originate)$')

        # Service-registration
        p13 = re.compile(r'^(?P<service>Service-registration)$')

        # Extranet-policy-propagation
        p14 = re.compile(r'^(?P<extranet>Extranet-policy-propagation)$')

        # Default-ETR Route-metric
        p15 = re.compile(r'^(?P<etr>Default-ETR Route-metric)$')

        # Unknown vendor type skip
        p16 = re.compile(r'^(?P<vendor>Unknown\s+vendor\s+type\s+skip)$')

        # RAR-notify
        p17 = re.compile(r'^(?P<rar>RAR-notify)$')

        # Extended Subscription
        p18 = re.compile(r'^(?P<extended>Extended\s+Subscription)$')

        # TCP path mtu discovery OFF
        p19 = re.compile(r'^TCP\s+path\s+mtu\s+discovery\s+(?P<tcp_path_mtu_discovery>ON|OFF)$')

        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})
                continue

            # Router-lisp ID:        0
            m = p2.match(line)
            if m:
                if not lisp_id:
                    groups = m.groupdict()
                    lisp_id = int(groups['lisp_id'])
                    lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                           .setdefault(lisp_id,{})
                    continue

            # Domain ID:             0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                domain_id = int(groups['domain_id'])
                lisp_id_dict.update({'domain_id':domain_id})
                continue

            # Multihoming ID:        0
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                multihoming_id = int(groups['multihoming_id'])
                lisp_id_dict.update({'multihoming_id':multihoming_id})
                continue

            # Locator table:         default
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                locator_table = groups['locator_table']
                lisp_id_dict.update({'locator_table':locator_table})
                continue

            # Locator default-set:   N/A
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                locator_default_set = groups['locator_default_set']
                lisp_id_dict.update({'locator_default_set':locator_default_set})
                continue

            # EID instance count:    7
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                eid_instance_count = groups['eid_instance_count']
                lisp_id_dict.update({'eid_instance_count':eid_instance_count})
                continue

            # Capability:            Publish-Subscribe Instance-ID
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                capability = groups['capability']
                capability_list = lisp_id_dict.setdefault('capability',[])
                capability_list.append(capability)
                continue

            # Domain-Info
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                domain = groups['domain']
                capability_list.append(domain)
                continue

            # Route-Tag
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                route = groups['route']
                capability_list.append(route)
                continue

            # SGT
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                sgt = groups['sgt']
                capability_list.append(sgt)
                continue

            # Default-originate
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                default = groups['default']
                capability_list.append(default)
                continue

            # Service-registration
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                service = groups['service']
                capability_list.append(service)
                continue

            # Extranet-policy-propagation
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                extranet = groups['extranet']
                capability_list.append(extranet)
                continue

            # Default-ETR Route-metric
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                etr = groups['etr']
                capability_list.append(etr)
                continue

            # Unknown vendor type skip
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                vendor = groups['vendor']
                capability_list.append(vendor)
                continue

            # RAR-notify
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                rar = groups['rar']
                capability_list.append(rar)
                continue

            # Extended Subscription
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                extended = groups['extended']
                capability_list.append(extended)
                lisp_id_dict.update({'capability':capability_list})
                continue

            # TCP path mtu discovery OFF
            m = p19.match(line)
            if m:
                groups = m.groupdict()
                tcp_path_mtu = groups['tcp_path_mtu_discovery']
                tcp_path_mtu_discovery = bool(re.search("ON",tcp_path_mtu))
                lisp_id_dict.update({'tcp_path_mtu_discovery':tcp_path_mtu_discovery})
                continue
        return ret_dict


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
                        Optional('pub_sub'): {
                            'role': bool,
                            Optional('publishers'): ListOf(str),
                            Optional('subscribers'): ListOf(str)
                            },
                        Optional('site_registration_limit'): int,
                        Optional('mapping_servers'): {
                            Any():{
                                'ms_address': str,
                                Optional('prefix_list'): str
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
                                    'interface': str,
                                    },
                                },
                            },
                        'encapsulation_type': str,
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
        p6 = re.compile(r'Proxy\-(ITR|ETR) +Router +\((?P<proxy_type>(PITR|PETR))\)'
                        r'*: +(?P<proxy_itr_router>(enabled|disabled))'
                        r'(?: +RLOCs: +(?P<proxy_itr_rloc>'
                        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})))?$')

        # ITR local RLOC (last resort):             *** NOT FOUND ***
        p7 = re.compile(r'^ITR +local +RLOC +\(last +resort\):\s+'
                        r'(?P<local_rloc_last_resort>.*)$')

        # ITR use proxy ETR RLOC(Encap IID):        1.1.1.1 (self), 66.66.66.66
        p8 = re.compile(r'^ITR\s+use +proxy +ETR +RLOC\(Encap IID\) *'
                        r': +(?P<use_proxy_etr_rloc_1>[\d.]+ *'
                        r'(\(self\))?),? *(?P<use_proxy_etr_rloc_2>[\d.]+)?$')

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

        # Publication-Subscription:                 enabled
        p25 = re.compile(r'^Publication-Subscription:\s+(?P<role>enabled|disabled)$')

        # Publisher(s):                           *** NOT FOUND ***
        p26 = re.compile(r'^Publisher\(s\):\s+(?P<publishers>\s+[\d.:]+)(?: +.*)?$')

        # Subscriber(s):                           *** NOT FOUND ***
        p27 = re.compile(r'^Subscriber\(s\):\s+(?P<subscribers>.*)')

        # Site Registration Limit:                  0
        p28 = re.compile(r'Site Registration Limit:\s+(?P<site_registration_limit>\d+)$')

        # ITR Map-Resolver(s):                 10.64.4.4, 10.166.13.13
        p29 = re.compile(r'ITR +Map\-Resolver\(s\) *: +(?P<mr_address>.*)$')

        #                                      10.84.66.66 *** not reachable ***
        p30 = re.compile(r'^(?P<prefix_list>[\d.:]+)(?: +.*)?$')

        # ETR Map-Server(s):                   10.64.4.4 (17:49:58), 10.166.13.13 (00:00:35)
        p31 = re.compile(r'ETR +Map\-Server\(s\) *: +(?P<ms_address>.*)$')

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

            # ITR Map-Resolver(s):                 10.64.4.4, 10.166.13.13
            m = p29.match(line)
            if m:
                map_resolvers = m.groupdict()['mr_address'].split(',')
                for ms in map_resolvers:
                    try:
                        map_resolver, uptime = ms.split()
                        map_resolver = map_resolver.replace(' ', '')
                    except ValueError:
                        map_resolver = ms.replace(' ', '')
                    # Set etr_dict under service
                    etr_mr_dict = instance_dict.setdefault('map_resolvers', {}).\
                                    setdefault(map_resolver, {})
                    etr_mr_dict.update({'mr_address':map_resolver})
                    count = 1
                continue

            #                                  10.84.66.66 (never)
            m = p30.match(line)
            if m:
                group = m.groupdict()
                prefix_list = group['prefix_list']
                if count == 0:
                    publishers_list.append(prefix_list)
                elif etr_mr_dict:
                    etr_mr_dict.update({'prefix_list':prefix_list})
                else:
                    etr_ms_dict.update({'prefix_list':prefix_list})
                continue

            # ETR Map-Server(s):                   10.64.4.4 (17:49:58), 10.166.13.13 (00:00:35)
            m = p31.match(line)
            if m:
                map_servers = m.groupdict()['ms_address'].split(',')
                for ms in map_servers:
                    try:
                        map_server, uptime = ms.split()
                        map_server = map_server.replace(' ', '')
                    except:
                        map_server = ms.replace(' ', '')
                    # Set etr_dict under service
                    etr_ms_dict = instance_dict.setdefault('mapping_servers', {}).\
                                    setdefault(map_server, {})
                    etr_ms_dict.update({'ms_address':map_server})
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

            # Encapsulation type:                       vxlan
            m = p63.match(line)
            if m:
                group = m.groupdict()
                encapsulation_type = group['encapsulation_type']
                instance_dict.update({'encapsulation_type':encapsulation_type})
                continue
        return ret_dict


class ShowLispSiteSummarySchema(MetaParser):
    """
    Schema for 'show lisp site summary'
    """
    schema = {
        'lisp_id': {
            int: {
                'site': {
                    str: {
                        'ipv4': {
                            'configured': int,
                            'registered': int,
                            'inconsistent': int
                            },
                        'ipv6': {
                            'configured': int,
                            'registered': int,
                            'inconsistent': int
                            },
                        'mac': {
                            'configured': int,
                            'registered': int,
                            'inconsistent': int
                            }
                        }
                    },
                'site_registration_limit': int,
                'site_registration_count': int,
                'ar_entries': int,
                'configured_sites': int,
                'registered_sites': int,
                'sites_with_inconsistent_reg': int,
                'configured_registered_prefixes': {
                    'ipv4': {
                        'configured': int,
                        'registered': int
                        },
                    'ipv6': {
                        'configured': int,
                        'registered': int
                        },
                    'mac': {
                        'configured': int,
                        'registered': int
                        }
                    }
                }
            }
        }


class ShowLispSiteSummary(ShowLispSiteSummarySchema):
    """
    Parser for 'show lisp site summary'
    """
    cli_command = ['show lisp site summary',
                   'show lisp {lisp_id} site summary',
                   'show lisp site summary instance-id {instance_id}',
                   'show lisp site summary eid-table vrf {vrf}',
                   'show lisp site summary eid-table {eid_table}']

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, eid_table=None):

        if output is None:
            if instance_id:
                output = self.device.execute(self.cli_command[2].\
                                            format(instance_id=instance_id))
            elif vrf:
                output = self.device.execute(self.cli_command[3].\
                                            format(vrf=vrf))
            elif eid_table:
                output = self.device.execute(self.cli_command[4].\
                                            format(eid_table=eid_table))
            elif lisp_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id))
            else:
                output = self.device.execute(self.cli_command[0])
        ret_dict = {}

        # Edoras                        0          0      0          0          0      0          0          0      0
        p1 = re.compile(r'^(?P<site>\S+)\s+(?P<v4_configured>\d+)\s+'
                        r'(?P<v4_registered>\d+)\s+(?P<v4_inconsistent>\d+)\s+'
                        r'(?P<v6_configured>\d+)\s+(?P<v6_registered>\d+)\s+'
                        r'(?P<v6_inconsistent>\d+)\s+(?P<mac_configured>\d+)\s+'
                        r'(?P<mac_registered>\d+)\s+(?P<mac_inconsistent>\d+)$')

        # Site-registration limit for router lisp 0:              0
        p2 = re.compile(r'^Site-registration\s+limit\s+for\s+'
                        r'router\s+lisp\s+(?P<lisp_id>\d+):\s+(?P<site_registration_limit>\d+)$')

        # Site-registration count for router lisp 0:              5
        p3 = re.compile(r'^Site-registration\s+count\s+for\s+router\s+lisp\s+\d+'
                        r':\s+(?P<site_registration_count>\d+)$')

        # Number of address-resolution entries:                   3
        p4 = re.compile(r'^Number\s+of\s+address-resolution\s+entries:\s+(?P<ar_entries>\d+)$')

        # Number of configured sites:                             2
        p5 = re.compile(r'^Number\s+of\s+configured\s+sites:\s+(?P<configured_sites>\d+)$')

        # Number of registered sites:                             1
        p6 = re.compile(r'^Number\s+of\s+registered\s+sites:\s+(?P<registered_sites>\d+)$')

        # Sites with inconsistent registrations:                  0
        p7 = re.compile(r'^Sites\s+with\s+inconsistent\s+registrations:'
                        r'\s+(?P<sites_with_inconsistent_reg>\d+)$')

        # Number of configured EID prefixes:                    4
        p8 = re.compile(r'^Number\s+of\s+configured\s+EID\s+prefixes:'
                        r'\s+(?P<ipv4_configured>\d+)$')

        # Number of registered EID prefixes:                    2
        p9 = re.compile(r'^Number\s+of\s+registered\s+EID\s+prefixes:'
                        r'\s+(?P<ipv4_registered>\d+)$')

        # IPv4
        # IPv6
        # MAC
        p10 = re.compile(r'^(?P<ip_version>IPv4|IPv6|MAC)$')

        for line in output.splitlines():
            line = line.strip()

            # Edoras                        0          0      0          0          0      0          0          0      0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                site = groups['site']
                v4_configured = int(groups['v4_configured'])
                v4_registered = int(groups['v4_registered'])
                v4_inconsistent = int(groups['v4_inconsistent'])
                v6_configured = int(groups['v6_configured'])
                v6_registered = int(groups['v6_registered'])
                v6_inconsistent = int(groups['v6_inconsistent'])
                mac_configured = int(groups['mac_configured'])
                mac_registered = int(groups['mac_registered'])
                mac_inconsistent = int(groups['mac_inconsistent'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(None,{})
                site_dict = lisp_id_dict.setdefault('site',{})\
                                        .setdefault(site,{})
                ipv4_dict = site_dict.setdefault('ipv4',{})
                ipv4_dict.update({'configured':v4_configured,
                                  'registered':v4_registered,
                                  'inconsistent':v4_inconsistent})
                ipv6_dict = site_dict.setdefault('ipv6',{})
                ipv6_dict.update({'configured':v6_configured,
                                  'registered':v6_registered,
                                  'inconsistent':v6_inconsistent})
                mac_dict = site_dict.setdefault('mac',{})
                mac_dict.update({'configured':mac_configured,
                                  'registered':mac_registered,
                                  'inconsistent':mac_inconsistent})
                continue

            # Site-registration limit for router lisp 0:              0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                site_registration_limit = int(groups['site_registration_limit'])
                ret_dict['lisp_id'][lisp_id] = ret_dict['lisp_id'].pop(None)
                lisp_id_dict.update({'site_registration_limit':site_registration_limit})
                continue

            # Site-registration count for router lisp 0:              5
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                site_registration_count = int(groups['site_registration_count'])
                lisp_id_dict.update({'site_registration_count':site_registration_count})
                continue

            # Number of address-resolution entries:                   3
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                ar_entries = int(groups['ar_entries'])
                lisp_id_dict.update({'ar_entries':ar_entries})
                continue

            # Number of configured sites:                             2
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                configured_sites = int(groups['configured_sites'])
                lisp_id_dict.update({'configured_sites':configured_sites})
                continue

            # Number of registered sites:                             1
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                registered_sites = int(groups['registered_sites'])
                lisp_id_dict.update({'registered_sites':registered_sites})
                continue

            # Sites with inconsistent registrations:                  0
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                sites_with_inconsistent_reg = int(groups['sites_with_inconsistent_reg'])
                lisp_id_dict.update({'sites_with_inconsistent_reg':sites_with_inconsistent_reg})
                continue

            # IPv4
            # IPv6
            # MAC
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                ip_version = groups['ip_version'].lower()
                ip_dict = lisp_id_dict.setdefault('configured_registered_prefixes',{})\
                                      .setdefault(ip_version,{})

            # Number of configured EID prefixes:                    4
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                configured = int(groups['ipv4_configured'])
                configured_reg_dict = lisp_id_dict.setdefault('configured_registered_prefixes',{})
                ip_dict.update({'configured':configured})
                continue

            # Number of registered EID prefixes:                    2
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                registered = int(groups['ipv4_registered'])
                ip_dict.update({'registered':registered})
                continue
        return ret_dict


class ShowLispInstanceIdServiceStatisticsSchema(MetaParser):

    ''' Schema for
    * show lisp instance-id {instance_id} {service} statistics
    * show lisp {lisp_id} {instance_id} {service} statistics
    * show lisp locator-table {locator_table} instance-id {instance_id} {service} statistics'''
    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
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
                            'eid_prefix_map_cache': int,
                            'rejected_eid_prefix_due_to_limit': int,
                            'times_signal_suppresion_turned_on': int,
                            'time_since_last_signal_suppressed': str,
                            'negative_entries_map_cache': int,
                            'total_rlocs_map_cache': int,
                            'average_rlocs_per_eid_prefix': int,
                            'policy_active_entries': int
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
                        'itr_map_resolvers': {
                            str: {
                                'last_reply': str,
                                'metric': int,
                                'req_sent': int,
                                'positive': int,
                                'negative': int,
                                'no_reply': int,
                                'avgrtt': {
                                    '5_sec': int,
                                    '1_min': int,
                                    '5_min': int
                                    }
                                }
                            },
                        'etr_map_servers': {
                            str: {
                                'avgrtt': {
                                    '5_sec': int,
                                    '1_min': int,
                                    '5_min': int
                                    }
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
            }
        }



class ShowLispInstanceIdServiceStatistics(ShowLispInstanceIdServiceStatisticsSchema):
    ''' Parser for 
    * show lisp instance-id {instance_id} {service} statistics
    * show lisp {lisp_id} {instance_id} {service} statistics
    * show lisp locator-table {locator_table} instance-id {instance_id} {service} statistics'''

    cli_command = ['show lisp instance-id {instance_id} {service} statistics',
                   'show lisp {lisp_id} {instance_id} {service} statistics',
                   'show lisp locator-table {locator_table} instance-id {instance_id} {service} statistics']

    def cli(self, output=None, lisp_id=None, instance_id=None, service=None, locator_table=None):

        if output is None:
            if lisp_id and instance_id and service:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id, service=service))
            elif locator_table and instance_id and service:
                output = self.device.execute(self.cli_command[2].format(locator_table=locator_table, instance_id=instance_id, service=service))
            elif instance_id and service:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id, service=service))
            else:
                raise TypeError("No arguments provided to parser")
        ret_dict = {}

        # Output for router lisp 0
        # Output for router lisp 0 instance-id 101
        p1 = re.compile(r'^Output for router lisp (?P<lisp_id>\d+)(\s+instance-id\s+\d+)?$')

        # LISP EID Statistics for instance ID 4100 - last cleared: never
        p2 = re.compile(r'^LISP EID Statistics for instance ID (?P<instance_id>\d+) - last cleared: (?P<last_cleared>\S+)$')

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

        # Map-Requests expired on-queue/no-reply          0/3
        p8 = re.compile(r'^Map-Requests expired on-queue\/no-reply\s+(?P<on_queue>\d+)\/(?P<no_reply>\d+)$')

        # Map-Resolver Map-Requests forwarded:            0
        p9 = re.compile(r'^Map-Resolver Map-Requests forwarded:\s+(?P<map_resolver_forwarded>\d+)$')

        # Map-Server Map-Requests forwarded:              0
        p10 = re.compile(r'^Map-Server Map-Requests forwarded:\s+(?P<map_server_forwarded>\d+)$')

        # Map-Reply records in/out:                         24/1
        p11 = re.compile(r'^Map-Reply records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Authoritative records in/out:                   23/1
        p12 = re.compile(r'^Authoritative records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Non-authoritative records in/out:               1/0
        p13 = re.compile(r'^Non-authoritative records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Negative records in/out:                        22/0
        p14 = re.compile(r'^Negative records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # RLOC-probe records in/out:                      1/1
        p15 = re.compile(r'^RLOC-probe records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Server Proxy-Reply records out:             0
        p16 = re.compile(r'^Map-Server Proxy-Reply records out:\s+(?P<out>\d+)$')

        # WLC Map-Subscribe records in/out:                 0/2
        p17 = re.compile(r'^WLC Map-Subscribe records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Subscribe failures in/out:                  0/0
        p18 = re.compile(r'^Map-Subscribe failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # WLC Map-Unsubscribe records in/out:               0/0
        p19 = re.compile(r'^WLC Map-Unsubscribe records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Unsubscribe failures in/out:                0/0
        p20 = re.compile(r'^Map-Unsubscribe failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Register records in/out:                      0/6
        p21 = re.compile(r'^Map-Register records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Registers in (5 sec/1 min/5 min):           0/0/0
        p22 = re.compile(r'^Map-Registers in \(5 sec\/1 min\/5 min\):\s+(?P<sec_5>\d+)\/(?P<min_1>\d+)\/(?P<min_5>\d+)$')

        # Map-Server AF disabled:                         0
        p23 = re.compile(r'^Map-Server AF disabled:\s+(?P<map_server_af_disabled>\d+)$')

        # Not valid site eid prefix:                      0
        p24 = re.compile(r'^Not valid site eid prefix:\s+(?P<not_valid_site_eid_prefix>\d+)$')

        # Authentication failures:                        0
        p25 = re.compile(r'^Authentication failures:\s+(?P<authentication_failures>\d+)$')

        # Disallowed locators:                            0
        p26 = re.compile(r'^Disallowed locators:\s+(?P<disallowed_locators>\d+)$')

        # Miscellaneous:                                  0
        p27 = re.compile(r'^Miscellaneous:\s+(?P<misc>\d+)$')

        # WLC Map-Register records in/out:                  0/0
        p28 = re.compile(r'^WLC Map-Register records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # WLC AP Map-Register in/out:                     0/0
        p29 = re.compile(r'^WLC AP Map-Register in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # WLC Client Map-Register in/out:                 0/0
        p30 = re.compile(r'^WLC Client Map-Register in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # WLC Map-Register failures in/out:               0/0
        p31 = re.compile(r'^WLC Map-Register failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Notify records in/out:                        8/0
        p32 = re.compile(r'^Map-Notify records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Authentication failures:                        0
        p33 = re.compile(r'^Authentication failures:\s+(?P<authentication_failures>\d+)')

        # WLC Map-Notify records in/out:                    0/0
        p34 = re.compile(r'^WLC Map-Notify records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)')

        # WLC AP Map-Notify in/out:                       0/0
        p35 = re.compile(r'^WLC AP Map-Notify in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)')

        # WLC Client Map-Notify in/out:                   0/0
        p36 = re.compile(r'^WLC Client Map-Notify in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)')

        # WLC Map-Notify failures in/out:                 0/0
        p37 = re.compile(r'^WLC Map-Notify failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription Request records in/out:            0/4
        p38 = re.compile(r'^Subscription Request records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # IID subscription requests in/out:             0/0
        p39 = re.compile(r'^IID subscription requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Pub-refresh subscription requests in/out:     0/0
        p40 = re.compile(r'^Pub-refresh subscription requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Policy subscription requests in/out:          0/4
        p41 = re.compile(r'^Policy subscription requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription Request failures in/out:           0/0
        p42 = re.compile(r'^Subscription Request failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription Status records in/out:             2/0
        p43 = re.compile(r'^Subscription Status records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # End of Publication records in/out:            0/0
        p44 = re.compile(r'^End of Publication records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription rejected records in/out:         0/0
        p45 = re.compile(r'^Subscription rejected records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription removed records in/out:          0/0
        p46 = re.compile(r'^Subscription removed records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription Status failures in/out:            0/0
        p47 = re.compile(r'^Subscription Status failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Solicit Subscription records in/out:            2/0
        p48 = re.compile(r'^Solicit Subscription records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Solicit Subscription failures in/out:           0/0
        p49 = re.compile(r'^Solicit Subscription failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Publication records in/out:                     0/0
        p50 = re.compile(r'^Publication records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Publication failures in/out:                    0/0
        p51 = re.compile(r'^Publication failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Mapping record TTL alerts:                        0
        p52 = re.compile(r'^Mapping record TTL alerts:\s+(?P<mapping_rec_ttl_alerts>\d+)$')

        # Map-Request invalid source rloc drops:            0
        p53 = re.compile(r'^Map-Request invalid source rloc drops:\s+(?P<map_request_invalid_source_rloc>\d+)$')

        # Map-Register invalid source rloc drops:           0
        p54 = re.compile(r'^Map-Register invalid source rloc drops:\s+(?P<map_register_invalid_source_rloc>\d+)$')

        # DDT Requests failed:                              0
        p55 = re.compile(r'^DDT Requests failed:\s+(?P<ddt_requests_failed>\d+)$')

        # DDT ITR Map-Requests dropped:                     0 (nonce-collision: 0, bad-xTR-nonce: 0)
        p56 = re.compile(r'^DDT ITR Map-Requests dropped:\s+(?P<dropped>\d+)\s+'
                         r'\(nonce-collision:\s+(?P<nonce_collision>\d+), '
                         r'bad-xTR-nonce:\s+(?P<bad_xtr_nonce>\d+)\)$')

        # Cache entries created/deleted:                    10/8
        p57 = re.compile(r'^Cache entries created\/deleted:\s+(?P<created>\d+)\/(?P<deleted>\d+)$')

        # NSF CEF replay entry count                        0
        p58 = re.compile(r'^NSF CEF replay entry count\s+(?P<nsf_cef_replay_entry_count>\d+)$')

        # Number of EID-prefixes in map-cache:              2
        p59 = re.compile(r'^Number of EID-prefixes in map-cache:\s+(?P<eid_prefix_map_cache>\d+)$')

        # Number of rejected EID-prefixes due to limit:     0
        p60 = re.compile(r'^Number of rejected EID-prefixes due to limit:\s+'
                         r'(?P<rejected_eid_prefix_due_to_limit>\d+)$')

        # Number of times signal suppression was turned on: 0
        p61 = re.compile(r'^Number of times signal suppression was turned on:\s+'
                         r'(?P<times_signal_suppresion_turned>\d+)$')

        # Time since last signal suppressed change:         never
        p62 = re.compile(r'^Time since last signal suppressed change:\s+'
                         r'(?P<time_since_last_signal>never|\d+)$')

        # Number of negative entries in map-cache:          2
        p63 = re.compile(r'^Number of negative entries in map-cache:\s+'
                         r'(?P<negative_entries_map_cache>\d+)$')

        # Total number of RLOCs in map-cache:               0
        p64 = re.compile(r'^Total number of RLOCs in map-cache:\s+(?P<total_rlocs_map_cache>\d+)$')

        # Average RLOCs per EID-prefix:                     0
        p65 = re.compile(r'^Average RLOCs per EID-prefix:\s+(?P<average_rlocs_per_eid_prefix>\d+)$')

        # Policy active entries:                            0
        p66 = re.compile(r'^Policy active entries:\s+(?P<policy_active_entries>\d+)$')

        # Number of data signals processed:                 2 (+ dropped 0)
        p67 = re.compile(r'^Number of data signals processed:\s+'
                         r'(?P<processed>\d+)\s+\(\+\s+dropped\s(?P<dropped>\d+)\)$')

        # Number of reachability reports:                   0 (+ dropped 0)
        p68 = re.compile(r'^Number of reachability reports:\s+'
                         r'(?P<count>\d+)\s+\(\+\s+dropped\s(?P<dropped>\d+)\)$')

        # Number of SMR signals dropped:                    0
        p69 = re.compile(r'^Number of SMR signals dropped:\s+(?P<dropped>\d+)$')

        #   44.44.44.44          6d21h      202176        8        0        0        6    0/ 0/ 0
        p70 = re.compile(r'^(?P<itr_map_resolvers>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                         r'\s+(?P<last_reply>\S+)\s+(?P<metric>\d+)\s+(?P<req_sent>\d+)\s+'
                         r'(?P<positive>\d+)\s+(?P<negative>\d+)\s+(?P<no_reply>\d+)\s+'
                         r'(?P<sec_5>\d+)\/\s(?P<min_1>\d+)\/\s(?P<min_5>\d+)$')

        # 44.44.44.44          0/ 0/ 0
        p71 = re.compile(r'^(?P<etr_map_servers>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                         r'(?P<sec_5>\d+)\/\s+(?P<min_1>\d+)\/\s(?P<min_5>\d+)$')

        # LISP RLOC Statistics - last cleared: never
        p72 = re.compile(r'^LISP RLOC Statistics - last cleared:\s(?P<last_cleared>\S+)$')

        # RTR Map-Requests forwarded:                       0
        p73 = re.compile(r'^RTR Map-Requests forwarded:\s+(?P<map_requests_forwarded>\d+)$')

        # RTR Map-Notifies forwarded:                       0
        p74 = re.compile(r'^RTR Map-Notifies forwarded:\s+(?P<map_notifies_forwarded>\d+)$')

        # DDT-Map-Requests in/out:                          0/0
        p75 = re.compile(r'^DDT-Map-Requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # DDT-Map-Referrals in/out:                         0/0
        p76 = re.compile(r'^DDT-Map-Referrals in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Request format errors:                        0
        p77 = re.compile(r'^Map-Request format errors:\s+(?P<map_request_format>\d+)$')

        # Map-Reply format errors:                          0
        p78 = re.compile(r'^Map-Reply format errors:\s+(?P<map_reply_format>\d+)$')

        # Map-Referral format errors:                       0
        p79 = re.compile(r'^Map-Referral format errors:\s+(?P<map_referral>\d+)$')

        # Invalid IP version drops:                         0
        p80 = re.compile(r'^Invalid IP version drops:\s+(?P<ip_version_drops>\d+)$')

        # Invalid IP header drops:                          0
        p81 = re.compile(r'^Invalid IP header drops:\s+(?P<ip_header_drops>\d+)$')

        # Invalid IP proto field drops:                     0
        p82 = re.compile(r'^Invalid IP proto field drops:\s+(?P<ip_proto_field_drops>\d+)$')

        # Invalid packet size drops:                        0
        p83 = re.compile(r'^Invalid packet size drops:\s+(?P<packet_size_drops>\d+)$')

        # Invalid LISP control port drops:                  0
        p84 = re.compile(r'^Invalid LISP control port drops:\s+(?P<lisp_control_port_drops>\d+)$')

        # Invalid LISP checksum drops:                      0
        p85 = re.compile(r'^Invalid LISP checksum drops:\s+(?P<lisp_checksum_drops>\d+)$')

        # Unsupported LISP packet type drops:               0
        p86 = re.compile(r'^Unsupported LISP packet type drops:\s+(?P<unsupported_lisp_packet_drops>\d+)$')

        # Unknown packet drops:                             0
        p87 = re.compile(r'^Unknown packet drops:\s+(?P<unknown_packet_drops>\d+)$')

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

            # LISP EID Statistics for instance ID 4100 - last cleared: never
            m = p2.match(line)
            if m:
                lisp_id = int(lisp_id) if lisp_id else 0
                lisp_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                group = m.groupdict()
                instance_id = int(group['instance_id'])
                last_cleared = group['last_cleared']
                instance_dict = lisp_dict.setdefault('instance_id',{}).\
                                          setdefault(instance_id,{})
                instance_dict.update({'last_cleared':last_cleared})
                continue

            # Map-Requests in/out:                              1/24
            m = p3.match(line)
            if m:
                group = m.groupdict()
                map_in = int(group['in'])
                out = int(group['out'])
                control_dict = instance_dict.setdefault('control_packets',{})
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

            # Map-Requests expired on-queue/no-reply          0/3
            m = p8.match(line)
            if m:
                group = m.groupdict()
                on_queue = int(group['on_queue'])
                no_reply = int(group['no_reply'])
                expired_dict = map_dict.setdefault('expired',{})
                expired_dict.update({'on_queue':on_queue,
                                     'no_reply':no_reply})
                continue

            # Map-Resolver Map-Requests forwarded:            0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                map_resolver_forwarded = int(group['map_resolver_forwarded'])
                map_dict.update({'map_resolver_forwarded':map_resolver_forwarded})
                continue

            # Map-Server Map-Requests forwarded:              0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                map_server_forwarded = int(group['map_server_forwarded'])
                map_dict.update({'map_server_forwarded':map_server_forwarded})
                continue

            # Map-Reply records in/out:                         24/1
            m = p11.match(line)
            if m:
                group = m.groupdict()
                map_reply_in = int(group['in'])
                out = int(group['out'])
                map_reply_dict = control_dict.setdefault('map_reply',{})
                map_reply_dict.update({'in':map_reply_in,
                                       'out':out})
                continue

            # Authoritative records in/out:                   23/1
            m = p12.match(line)
            if m:
                group = m.groupdict()
                auth_in = int(group['in'])
                out = int(group['out'])
                auth_dict = map_reply_dict.setdefault('authoritative',{})
                auth_dict.update({'in':auth_in,
                                  'out':out})
                continue

            # Non-authoritative records in/out:               1/0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                non_auth_in = int(group['in'])
                out = int(group['out'])
                non_auth_dict = map_reply_dict.setdefault('non_authoritative',{})
                non_auth_dict.update({'in':non_auth_in,
                                      'out':out})
                continue

            # Negative records in/out:                        22/0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                negative_in = int(group['in'])
                out = int(group['out'])
                negative_dict = map_reply_dict.setdefault('negative',{})
                negative_dict.update({'in':negative_in,
                                      'out':out})
                continue

            # RLOC-probe records in/out:                      1/1
            m = p15.match(line)
            if m:
                group = m.groupdict()
                rloc_probe_in = int(group['in'])
                out = int(group['out'])
                rloc_probe_dict = map_reply_dict.setdefault('rloc_probe',{})
                rloc_probe_dict.update({'in':rloc_probe_in,
                                        'out':out})
                continue

            # Map-Server Proxy-Reply records out:             0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                out = int(group['out'])
                map_server_dict = map_reply_dict.setdefault('map_server_proxy_reply',{})
                map_server_dict.update({'out':out})
                continue

            # WLC Map-Subscribe records in/out:                 0/2
            m = p17.match(line)
            if m:
                group = m.groupdict()
                wlc_in = int(group['in'])
                out = int(group['out'])
                wlc_dict = control_dict.setdefault('wlc_map_subscribe',{})
                wlc_dict.update({'in':wlc_in,
                                 'out':out})
                continue

            # Map-Subscribe failures in/out:                  0/0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                sub_in = int(group['in'])
                out = int(group['out'])
                fail_dict = wlc_dict.setdefault('failures',{})
                fail_dict.update({'in':sub_in,
                                  'out':out})
                continue

            # WLC Map-Unsubscribe records in/out:               0/0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                unsub_in = int(group['in'])
                out = int(group['out'])
                wlc_unsub_dict = control_dict.setdefault('wlc_map_unsubscribe',{})
                wlc_unsub_dict.update({'in':unsub_in,
                                       'out':out})
                continue

            # Map-Unsubscribe failures in/out:                0/0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                fail_unsub_in = int(group['in'])
                out = int(group['out'])
                wlc_map_unsub_dict = wlc_unsub_dict.setdefault('failures',{})
                wlc_map_unsub_dict.update({'in':fail_unsub_in,
                                           'out':out})
                continue

            # Map-Register records in/out:                      0/6
            m = p21.match(line)
            if m:
                group = m.groupdict()
                map_record_in = int(group['in'])
                out = int(group['out'])
                map_reg_record_dict = control_dict.setdefault('map_register',{})
                map_reg_record_dict.update({'in':map_record_in,
                                           'out':out})
                continue

            # Map-Registers in (5 sec/1 min/5 min):           0/0/0
            m = p22.match(line)
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
            m = p23.match(line)
            if m:
                group = m.groupdict()
                map_server_af_disabled = int(group['map_server_af_disabled'])
                map_reg_record_dict.update({'map_server_af_disabled':map_server_af_disabled})
                continue

            # Not valid site eid prefix:                      0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                not_valid_site_eid_prefix = int(group['not_valid_site_eid_prefix'])
                map_reg_record_dict.update({'not_valid_site_eid_prefix':not_valid_site_eid_prefix})
                continue

            # Authentication failures:                        0
            m = p25.match(line)
            if m and "authentication_failures" not in map_reg_record_dict:
                group = m.groupdict()
                authentication_failures = int(group['authentication_failures'])
                map_reg_record_dict.update({'authentication_failures':authentication_failures})
                continue

            # Disallowed locators:                            0
            m = p26.match(line)
            if m:
                group = m.groupdict()
                disallowed_locators = int(group['disallowed_locators'])
                map_reg_record_dict.update({'disallowed_locators':disallowed_locators})
                continue

            # Miscellaneous:                                  0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                misc = int(group['misc'])
                map_reg_record_dict.update({'misc':misc})
                continue

            # WLC Map-Register records in/out:                  0/0
            m = p28.match(line)
            if m:
                group = m.groupdict()
                wlc_map_in = int(group['in'])
                out = int(group['out'])
                wlc_map_registers_dict = control_dict.setdefault('wlc_map_registers',{})
                wlc_map_registers_dict.update({'in':wlc_map_in,
                                               'out':out})
                continue

            # WLC AP Map-Register in/out:                     0/0
            m = p29.match(line)
            if m:
                group = m.groupdict()
                wlc_ap_map_in = int(group['in'])
                out = int(group['out'])
                wlc_ap_dict = wlc_map_registers_dict.setdefault('ap',{})
                wlc_ap_dict.update({'in':wlc_ap_map_in,
                                    'out':out})
                continue

            # WLC Client Map-Register in/out:                 0/0
            m = p30.match(line)
            if m:
                group = m.groupdict()
                wlc_client_map_in = int(group['in'])
                out = int(group['out'])
                wlc_client_dict = wlc_map_registers_dict.setdefault('client',{})
                wlc_client_dict.update({'in':wlc_client_map_in,
                                        'out':out})
                continue

            # WLC Map-Register failures in/out:               0/0
            m = p31.match(line)
            if m:
                group = m.groupdict()
                wlc_fail_map_in = int(group['in'])
                out = int(group['out'])
                wlc_fail_dict = wlc_map_registers_dict.setdefault('failures',{})
                wlc_fail_dict.update({'in':wlc_fail_map_in,
                                      'out':out})
                continue

            # Map-Notify records in/out:                        8/0
            m = p32.match(line)
            if m:
                group = m.groupdict()
                map_notify_in = int(group['in'])
                out = int(group['out'])
                map_notify_dict = control_dict.setdefault('map_notify',{})
                map_notify_dict.update({'in':map_notify_in,
                                        'out':out})
                continue

            # Authentication failures:                        0
            m = p33.match(line)
            if m:
                group = m.groupdict()
                authentication_failures = int(group['authentication_failures'])
                map_notify_dict.update({'authentication_failures':authentication_failures})
                continue

            # WLC Map-Notify records in/out:                    0/0
            m = p34.match(line)
            if m:
                group = m.groupdict()
                wlc_map_notify_in = int(group['in'])
                out = int(group['out'])
                wlc_map_notify_dict = control_dict.setdefault('wlc_map_notify',{})
                wlc_map_notify_dict.update({'in':wlc_map_notify_in,
                                            'out':out})
                continue

            # WLC AP Map-Notify in/out:                       0/0
            m = p35.match(line)
            if m:
                group = m.groupdict()
                wlc_ap_notify_in = int(group['in'])
                out = int(group['out'])
                wlc_ap_notify_dict = wlc_map_notify_dict.setdefault('ap',{})
                wlc_ap_notify_dict.update({'in':wlc_ap_notify_in,
                                           'out':out})
                continue

            # WLC Client Map-Notify in/out:                   0/0
            m = p36.match(line)
            if m:
                group = m.groupdict()
                wlc_client_notify_in = int(group['in'])
                out = int(group['out'])
                wlc_client_notify_dict = wlc_map_notify_dict.setdefault('client',{})
                wlc_client_notify_dict.update({'in':wlc_client_notify_in,
                                               'out':out})
                continue

            # WLC Map-Notify failures in/out:                 0/0
            m = p37.match(line)
            if m:
                group = m.groupdict()
                wlc_failures_notify_in = int(group['in'])
                out = int(group['out'])
                wlc_fail_notify_dict = wlc_map_notify_dict.setdefault('failures',{})
                wlc_fail_notify_dict.update({'in':wlc_failures_notify_in,
                                             'out':out})
                continue

            # Subscription Request records in/out:            0/4
            m = p38.match(line)
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
            m = p39.match(line)
            if m:
                group = m.groupdict()
                iid_in = int(group['in'])
                out = int(group['out'])
                iid_dict = subscription_request_dict.setdefault('iid',{})
                iid_dict.update({'in':iid_in,
                                 'out':out})
                continue

            # Pub-refresh subscription requests in/out:     0/0
            m = p40.match(line)
            if m:
                group = m.groupdict()
                pub_in = int(group['in'])
                out = int(group['out'])
                pub_refresh_dict = subscription_request_dict.setdefault('pub_refresh',{})
                pub_refresh_dict.update({'in':pub_in,
                                         'out':out})
                continue

            # Policy subscription requests in/out:          0/4
            m = p41.match(line)
            if m:
                group = m.groupdict()
                policy_in = int(group['in'])
                out = int(group['out'])
                policy_dict = subscription_request_dict.setdefault('policy',{})
                policy_dict.update({'in':policy_in,
                                    'out':out})
                continue

            # Subscription Request failures in/out:           0/0
            m = p42.match(line)
            if m:
                group = m.groupdict()
                policy_in = int(group['in'])
                out = int(group['out'])
                failures_dict = subscription_request_dict.setdefault('failures',{})
                failures_dict.update({'in':policy_in,
                                      'out':out})
                continue

            # Subscription Status records in/out:             2/0
            m = p43.match(line)
            if m:
                group = m.groupdict()
                sub_request_in = int(group['in'])
                out = int(group['out'])
                sub_status_dict = publish_dict.setdefault('subscription_status',{})
                sub_status_dict.update({'in':sub_request_in,
                                        'out':out})
                continue

            # End of Publication records in/out:            0/0
            m = p44.match(line)
            if m:
                group = m.groupdict()
                iid_in = int(group['in'])
                out = int(group['out'])
                end_pub_dict = sub_status_dict.setdefault('end_of_publication',{})
                end_pub_dict.update({'in':iid_in,
                                     'out':out})
                continue

            # Subscription rejected records in/out:         0/0
            m = p45.match(line)
            if m:
                group = m.groupdict()
                pub_in = int(group['in'])
                out = int(group['out'])
                sub_reject_dict = sub_status_dict.setdefault('subscription_rejected',{})
                sub_reject_dict.update({'in':pub_in,
                                        'out':out})
                continue

            # Subscription removed records in/out:          0/0
            m = p46.match(line)
            if m:
                group = m.groupdict()
                policy_in = int(group['in'])
                out = int(group['out'])
                sub_removed_dict = sub_status_dict.setdefault('subscription_removed',{})
                sub_removed_dict.update({'in':policy_in,
                                         'out':out})
                continue

            # Subscription Status failures in/out:            0/0
            m = p47.match(line)
            if m:
                group = m.groupdict()
                policy_in = int(group['in'])
                out = int(group['out'])
                sub_failures_dict = sub_status_dict.setdefault('failures',{})
                sub_failures_dict.update({'in':policy_in,
                                          'out':out})
                continue

            # Solicit Subscription records in/out:            2/0
            m = p48.match(line)
            if m:
                group = m.groupdict()
                sub_request_in = int(group['in'])
                out = int(group['out'])
                solicit_subscription_dict = publish_dict.setdefault('solicit_subscription',{})
                solicit_subscription_dict.update({'in':sub_request_in,
                                                  'out':out})
                continue

            # Solicit Subscription failures in/out:           0/0
            m = p49.match(line)
            if m:
                group = m.groupdict()
                iid_in = int(group['in'])
                out = int(group['out'])
                solicit_fail_dict = solicit_subscription_dict.setdefault('failures',{})
                solicit_fail_dict.update({'in':iid_in,
                                          'out':out})
                continue

            # Publication records in/out:                     0/0
            m = p50.match(line)
            if m:
                group = m.groupdict()
                sub_request_in = int(group['in'])
                out = int(group['out'])
                solicit_publication_dict = publish_dict.setdefault('publication',{})
                solicit_publication_dict.update({'in':sub_request_in,
                                                 'out':out})
                continue

            # Publication failures in/out:                    0/0
            m = p51.match(line)
            if m:
                group = m.groupdict()
                iid_in = int(group['in'])
                out = int(group['out'])
                solicit_failure_dict = solicit_publication_dict.setdefault('failures',{})
                solicit_failure_dict.update({'in':iid_in,
                                             'out':out})
                continue

            # Mapping record TTL alerts:                        0
            m = p52.match(line)
            if m:
                group = m.groupdict()
                mapping_rec_ttl_alerts = int(group['mapping_rec_ttl_alerts'])
                error_dict = instance_dict.setdefault('errors',{})
                error_dict.update({'mapping_rec_ttl_alerts':mapping_rec_ttl_alerts})
                continue

            # Map-Request invalid source rloc drops:            0
            m = p53.match(line)
            if m:
                group = m.groupdict()
                map_request_invalid_source_rloc_drops = int(group['map_request_invalid_source_rloc'])
                error_dict.update({'map_request_invalid_source_rloc_drops':map_request_invalid_source_rloc_drops})
                continue

            # Map-Register invalid source rloc drops:           0
            m = p54.match(line)
            if m:
                group = m.groupdict()
                map_register_invalid_source_rloc_drops = int(group['map_register_invalid_source_rloc'])
                error_dict.update({'map_register_invalid_source_rloc_drops':map_register_invalid_source_rloc_drops})
                continue

            # DDT Requests failed:                              0
            m = p55.match(line)
            if m:
                group = m.groupdict()
                ddt_requests_failed = int(group['ddt_requests_failed'])
                error_dict.update({'ddt_requests_failed':ddt_requests_failed})
                continue

            # DDT ITR Map-Requests dropped:                     0 (nonce-collision: 0, bad-xTR-nonce: 0)
            m = p56.match(line)
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
            m = p57.match(line)
            if m:
                group = m.groupdict()
                created = int(group['created'])
                deleted = int(group['deleted'])
                cache_dict = instance_dict.setdefault('cache_related',{})
                cache_entries_dict = cache_dict.setdefault('cache_entries',{})
                cache_entries_dict.update({'created':created,
                                           'deleted':deleted})
                continue

            # NSF CEF replay entry count                        0
            m = p58.match(line)
            if m:
                group = m.groupdict()
                nsf_cef_replay_entry_count = int(group['nsf_cef_replay_entry_count'])
                cache_dict.update({'nsf_cef_replay_entry_count':nsf_cef_replay_entry_count})
                continue

            # Number of EID-prefixes in map-cache:              2
            m = p59.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_map_cache = int(group['eid_prefix_map_cache'])
                cache_dict.update({'eid_prefix_map_cache':eid_prefix_map_cache})
                continue

            # Number of rejected EID-prefixes due to limit:     0
            m = p60.match(line)
            if m:
                group = m.groupdict()
                rejected_eid_prefix_due_to_limit = int(group['rejected_eid_prefix_due_to_limit'])
                cache_dict.update({'rejected_eid_prefix_due_to_limit':rejected_eid_prefix_due_to_limit})
                continue

            # Number of times signal suppression was turned on: 0
            m = p61.match(line)
            if m:
                group = m.groupdict()
                times_signal_suppresion_turned_on = int(group['times_signal_suppresion_turned'])
                cache_dict.update({'times_signal_suppresion_turned_on':times_signal_suppresion_turned_on})
                continue

            # Time since last signal suppressed change:         never
            m = p62.match(line)
            if m:
                group = m.groupdict()
                time_since_last_signal_suppressed = group['time_since_last_signal']
                cache_dict.update({'time_since_last_signal_suppressed':time_since_last_signal_suppressed})
                continue

            # Number of negative entries in map-cache:          2
            m = p63.match(line)
            if m:
                group = m.groupdict()
                negative_entries_map_cache = int(group['negative_entries_map_cache'])
                cache_dict.update({'negative_entries_map_cache':negative_entries_map_cache})
                continue

            # Total number of RLOCs in map-cache:               0
            m = p64.match(line)
            if m:
                group = m.groupdict()
                total_rlocs_map_cache = int(group['total_rlocs_map_cache'])
                cache_dict.update({'total_rlocs_map_cache':total_rlocs_map_cache})
                continue

            # Average RLOCs per EID-prefix:                     0
            m = p65.match(line)
            if m:
                group = m.groupdict()
                average_rlocs_per_eid_prefix = int(group['average_rlocs_per_eid_prefix'])
                cache_dict.update({'average_rlocs_per_eid_prefix':average_rlocs_per_eid_prefix})
                continue

            # Policy active entries:                            0
            m = p66.match(line)
            if m:
                group = m.groupdict()
                policy_active_entries = int(group['policy_active_entries'])
                cache_dict.update({'policy_active_entries':policy_active_entries})
                continue

            # Number of data signals processed:                 2 (+ dropped 0)
            m = p67.match(line)
            if m:
                group = m.groupdict()
                processed = int(group['processed'])
                dropped = int(group['dropped'])
                forwarding_dict = instance_dict.setdefault('forwarding',{})
                data_signal_dict = forwarding_dict.setdefault('data_signals',{})
                data_signal_dict.update({'processed':processed,
                                         'dropped':dropped})
                continue

            # Number of reachability reports:                   0 (+ dropped 0)
            m = p68.match(line)
            if m:
                group = m.groupdict()
                count = int(group['count'])
                dropped = int(group['dropped'])
                reachability_dict = forwarding_dict.setdefault('reachability_reports',{})
                reachability_dict.update({'count':count,
                                         'dropped':dropped})
                continue

            # Number of SMR signals dropped:                    0
            m = p69.match(line)
            if m:
                group = m.groupdict()
                dropped = int(group['dropped'])
                smr_signal_dict = forwarding_dict.setdefault('smr_signals',{})
                smr_signal_dict.update({'dropped':dropped})
                continue

            # 44.44.44.44          6d21h      202176        8        0        0        6    0/ 0/ 0
            m = p70.match(line)
            if m:
                group = m.groupdict()
                itr_map_resolvers = group['itr_map_resolvers']
                last_reply = group['last_reply']
                metric = int(group['metric'])
                req_sent = int(group['req_sent'])
                positive = int(group['positive'])
                negative = int(group['negative'])
                no_reply = int(group['no_reply'])
                sec_5 = int(group['sec_5'])
                min_1 = int(group['min_1'])
                min_5 = int(group['min_5'])
                itr_map_dict = instance_dict.setdefault('itr_map_resolvers',{})
                itr_map_resolvers_dict = itr_map_dict.setdefault(itr_map_resolvers,{})
                itr_map_resolvers_dict.update({'last_reply':last_reply,
                                               'metric':metric,
                                               'req_sent':req_sent,
                                               'positive':positive,
                                               'negative':negative,
                                               'no_reply':no_reply})
                avg_dict = itr_map_resolvers_dict.setdefault('avgrtt',{})
                avg_dict.update({'5_sec':sec_5,
                                 '1_min':min_1,
                                 '5_min':min_5})
                continue

            # 44.44.44.44          0/ 0/ 0
            m = p71.match(line)
            if m:
                group = m.groupdict()
                etr_map_servers = group['etr_map_servers']
                sec_5 = int(group['sec_5'])
                min_1 = int(group['min_1'])
                min_5 = int(group['min_5'])
                etr_map_dict = instance_dict.setdefault('etr_map_servers',{})
                etr_map_servers_dict = etr_map_dict.setdefault(etr_map_servers,{})\
                                                   .setdefault('avgrtt',{})
                etr_map_servers_dict.update({'5_sec':sec_5,
                                             '1_min':min_1,
                                             '5_min':min_5})
                continue

            # LISP RLOC Statistics - last cleared: never
            m = p72.match(line)
            if m:
                group = m.groupdict()
                last_cleared = group['last_cleared']
                rloc_stat_dict = instance_dict.setdefault('rloc_statistics',{})
                rloc_stat_dict.update({'last_cleared':last_cleared})
                continue

            # RTR Map-Requests forwarded:                       0
            m = p73.match(line)
            if m:
                group = m.groupdict()
                map_requests_forwarded = int(group['map_requests_forwarded'])
                control_packets_dict = rloc_stat_dict.setdefault('control_packets',{})
                rtr_dict = control_packets_dict.setdefault('rtr',{})
                rtr_dict.update({'map_requests_forwarded':map_requests_forwarded})
                continue

            # RTR Map-Notifies forwarded:                       0
            m = p74.match(line)
            if m:
                group = m.groupdict()
                map_notifies_forwarded = int(group['map_notifies_forwarded'])
                rtr_dict.update({'map_notifies_forwarded':map_notifies_forwarded})
                continue

            # DDT-Map-Requests in/out:                          0/0
            m = p75.match(line)
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
            m = p76.match(line)
            if m:
                group = m.groupdict()
                map_requests_in = int(group['in'])
                out = int(group['out'])
                map_referral_request = ddt_dict.setdefault('map_referrals',{})
                map_referral_request.update({'in':map_requests_in,
                                             'out':out})
                continue

            # Map-Request format errors:                        0
            m = p77.match(line)
            if m:
                group = m.groupdict()
                map_request_format = int(group['map_request_format'])
                map_errors_dict = rloc_stat_dict.setdefault('errors',{})
                map_errors_dict.update({'map_request_format':map_request_format})
                continue

            # Map-Reply format errors:                          0
            m = p78.match(line)
            if m:
                group = m.groupdict()
                map_reply_format = int(group['map_reply_format'])
                map_errors_dict.update({'map_reply_format':map_reply_format})
                continue

            # Map-Referral format errors:                       0
            m = p79.match(line)
            if m:
                group = m.groupdict()
                map_referral = int(group['map_referral'])
                map_errors_dict.update({'map_referral':map_referral})
                continue

            # Invalid IP version drops:                         0
            m = p80.match(line)
            if m:
                group = m.groupdict()
                ip_version_drops = int(group['ip_version_drops'])
                misc_dict = instance_dict.setdefault('misc_statistics',{})
                invalid_dict = misc_dict.setdefault('invalid',{})
                invalid_dict.update({'ip_version_drops':ip_version_drops})
                continue

            # Invalid IP header drops:                          0
            m = p81.match(line)
            if m:
                group = m.groupdict()
                ip_header_drops = int(group['ip_header_drops'])
                invalid_dict.update({'ip_header_drops':ip_header_drops})
                continue

            # Invalid IP proto field drops:                     0
            m = p82.match(line)
            if m:
                group = m.groupdict()
                ip_proto_field_drops = int(group['ip_proto_field_drops'])
                invalid_dict.update({'ip_proto_field_drops':ip_proto_field_drops})
                continue

            # Invalid packet size drops:                        0
            m = p83.match(line)
            if m:
                group = m.groupdict()
                packet_size_drops = int(group['packet_size_drops'])
                invalid_dict.update({'packet_size_drops':packet_size_drops})
                continue

            # Invalid LISP control port drops:                  0
            m = p84.match(line)
            if m:
                group = m.groupdict()
                lisp_control_port_drops = int(group['lisp_control_port_drops'])
                invalid_dict.update({'lisp_control_port_drops':lisp_control_port_drops})
                continue

            # Invalid LISP checksum drops:                      0
            m = p85.match(line)
            if m:
                group = m.groupdict()
                lisp_checksum_drops = int(group['lisp_checksum_drops'])
                invalid_dict.update({'lisp_checksum_drops':lisp_checksum_drops})
                continue

            # Unsupported LISP packet type drops:               0
            m = p86.match(line)
            if m:
                group = m.groupdict()
                unsupported_lisp_packet_drops = int(group['unsupported_lisp_packet_drops'])
                misc_dict.update({'unsupported_lisp_packet_drops':unsupported_lisp_packet_drops})
                continue

            # Unknown packet drops:                             0
            m = p87.match(line)
            if m:
                group = m.groupdict()
                unknown_packet_drops = int(group['unknown_packet_drops'])
                misc_dict.update({'unknown_packet_drops':unknown_packet_drops})
                continue
        return ret_dict


class ShowLispMapCacheSuperParserSchema(MetaParser):
    """ Schema for show lisp site"""
    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'eid_table': str,
                        'entries': int,
                        'eid_prefix': {
                            str: {
                                'uptime': str,
                                'expiry_time': str,
                                'via': str,
                                Optional('map_reply_state'): str,
                                Optional('site'): str,
                                Optional('sgt'): int,
                                Optional('map_cache_type'): str,
                                Optional('action'): str,
                                Optional('negative_cache_entry'): bool,
                                Optional('locators'): {
                                    str: {
                                        Optional('uptime'): str,
                                        Optional('rloc_state'): str,
                                        Optional('priority'): int,
                                        Optional('weight'): int,
                                        Optional('encap_iid'): str,
                                        Optional('metric'): int
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispMapCacheSuperParser(ShowLispMapCacheSuperParserSchema):
    """Parser for show lisp instance-id {instance_id} ipv4 map-cache"""

    def cli(self, output=None):

        ret_dict = {}

        # LISP IPv4 Mapping Cache for LISP 0 EID-table vrf red (IID 4100), 5 entries
        p1 = re.compile(r'^LISP (IPv4|IPv6) Mapping Cache for LISP (?P<lisp_id>\d+)\s+'
                        r'EID-table\s+(?P<eid_table>[a-zA-Z0-9\s]+)'
                        r'\(IID\s+(?P<instance_id>\d+)\),\s+(?P<entries>\d+)\s+entries$')

        # 50.1.1.0/24, uptime: 2d09h, expires: 20:10:07, via map-reply, complete, local-to-site
        p2 = re.compile(r'^(?P<eid_prefix>[a-fA-F\d\:]+\/\d{1,3}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/'
                        r'\d{1,2}),\s+uptime:\s(?P<uptime>\S+),\sexpires:\s'
                        r'(?P<expiry_time>\d{1,2}:\d{2}:\d{2}|never),\svia\s(?P<via>\S+)(,'
                        r'\s(?P<map_reply_state>(complete|unknown-eid-forward'
                        r'|send-map-request|drop|incomplete)))?'
                        r'(,\s(?P<site>local-to-site|remote-to-site))?$')

        # SGT: 10, software only
        # SGT: 10
        p3 = re.compile(r'^(SGT: (?P<sgt>\d+))?(,\s)?(?P<map_cache_type>software only)?$')

        # action: send-map-request + Encapsulating to proxy ETR
        # Negative cache entry, action: send-map-request
        p4 = re.compile(r'^(?P<negative_cache_entry>Negative cache entry,\s)?'
                        r'action:\s(?P<action>(send-map-request\s\+\s'
                        r'Encapsulating to proxy ETR)|send-map-request)$')

        # 100.165.165.165  2d09h     up          10/10        4100
        p5 = re.compile(r'^(?P<locators>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(?P<uptime>\S+)\s+(?P<rloc_state>\S+)\s+(?P<priority>\d+)'
                        r'\/(?P<weight>\d+)\s+(?P<encap_iid>\d+|-)(\s+(?P<metric>\d+))?$')

        for line in output.splitlines():
            line = line.strip()

            # LISP IPv4 Mapping Cache for LISP 0 EID-table vrf red (IID 4100), 5 entries
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id = int(group['lisp_id'])
                instance_id = int(group['instance_id'])
                eid_table = group['eid_table']
                entries = int(group['entries'])
                lisp_dict = ret_dict.setdefault('lisp_id',{})\
                                    .setdefault(lisp_id,{})\
                                    .setdefault('instance_id',{})\
                                    .setdefault(instance_id,{})
                lisp_dict.update({'eid_table':eid_table,
                                  'entries':entries})
                continue

            # 0.0.0.0/0, uptime: 2d09h, expires: 00:12:57, via map-reply, unknown-eid-forward
            m = p2.match(line)
            if m:
                group = m.groupdict()
                eid_prefix = group['eid_prefix']
                uptime = group['uptime']
                expiry_time = group['expiry_time']
                via = group['via']
                eid_dict = lisp_dict.setdefault('eid_prefix',{})\
                                    .setdefault(eid_prefix,{})
                eid_dict.update({'uptime':uptime,
                                 'expiry_time':expiry_time,
                                 'via':via})
                if group['map_reply_state']:
                    map_reply_state = group['map_reply_state']
                    eid_dict.update({'map_reply_state':map_reply_state})
                if group['site']:
                    site = group['site']
                    eid_dict.update({'site':site})
                continue

            # SGT: 10, software only
            # SGT: 10
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if group['sgt']:
                    sgt = int(group['sgt'])
                    eid_dict.update({'sgt':sgt})
                if group['map_cache_type']:
                    map_cache_type = group['map_cache_type']
                    eid_dict.update({'map_cache_type':map_cache_type})
                continue

            # action: send-map-request + Encapsulating to proxy ETR
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if group['action']:
                    action = group['action']
                    eid_dict.update({'action':action})
                if group['negative_cache_entry']:
                    negative_cache_entry = group['negative_cache_entry']
                    eid_dict.update({'negative_cache_entry':True})
                if not group['negative_cache_entry']:
                    eid_dict.update({'negative_cache_entry':False})
                continue

            # 100.165.165.165  2d09h     up          10/10        4100
            m = p5.match(line)
            if m:
                group = m.groupdict()
                locators = group['locators']
                uptime = group['uptime']
                rloc_state = group['rloc_state']
                priority = int(group['priority'])
                weight = int(group['weight'])
                encap_iid = group['encap_iid']
                locators_dict = eid_dict.setdefault('locators',{}).\
                                         setdefault(locators,{})
                locators_dict.update({'uptime':uptime,
                                      'rloc_state':rloc_state,
                                      'priority':priority,
                                      'weight':weight,
                                      'encap_iid':encap_iid})
                if group['metric']:
                    metric = int(group['metric'])
                    locators_dict.update({'metric':metric})
                continue
        return ret_dict


class ShowLispInstanceIdIpv4MapCache(ShowLispMapCacheSuperParser):

    """
    Parser for
    * show lisp instance-id {instance_id} ipv4 map-cache
    * show lisp {lisp_id} instance-id {instance_id} ipv4 map-cache
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 map-cache
    * show lisp eid-table vrf {vrf} ipv4 map-cache
    * show lisp eid-table {eid_table} ipv4 map-caches"""

    cli_command = ['show lisp instance-id {instance_id} ipv4 map-cache',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 map-cache',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 map-cache',
                   'show lisp eid-table vrf {vrf} ipv4 map-cache',
                   'show lisp eid-table {eid_table} ipv4 map-cache']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, locator_table=None, vrf=None, output=None):
        if output is None:
            if locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].format(locator_table=locator_table, instance_id=instance_id))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id))
            elif vrf:
                output = self.device.execute(self.cli_command[3].format(vrf=vrf))
            elif eid_table:
                output = self.device.execute(self.cli_command[4].format(eid_table=eid_table))
            else:
                raise TypeError("No arguments provided to parser")
        return super().cli(output=output)


class ShowLispInstanceIdIpv6MapCache(ShowLispMapCacheSuperParser):

    """
    Parser for
    * show lisp instance-id {instance_id} ipv6 map-cache
    * show lisp {lisp_id} instance-id {instance_id} ipv6 map-cache
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 map-cache
    * show lisp eid-table vrf {vrf} ipv6 map-cache
    * show lisp eid-table {eid_table} ipv6 map-caches"""

    cli_command = ['show lisp instance-id {instance_id} ipv6 map-cache',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 map-cache',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 map-cache',
                   'show lisp eid-table vrf {vrf} ipv6 map-cache',
                   'show lisp eid-table {eid_table} ipv6 map-cache']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, locator_table=None, vrf=None, output=None):
        if output is None:
            if locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].format(locator_table=locator_table, instance_id=instance_id))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id))
            elif vrf:
                output = self.device.execute(self.cli_command[3].format(vrf=vrf))
            elif eid_table:
                output = self.device.execute(self.cli_command[4].format(eid_table=eid_table))
            else:
                raise TypeError("No arguments provided to parser")
        return super().cli(output=output)


# ==============================
# Schema for
# 'show lisp remote-locator-set {remote_locator_type}',
# 'show lisp remote-locator-set name {remote_locator_name}',
# 'show lisp {lisp_id} remote-locator-set {remote_locator_type}',
# 'show lisp {lisp_id} remote-locator-set name {remote_locator_name}'
# ==============================
class ShowLispRemoteLocatorSetSchema(MetaParser):
    """Schema for
        'show lisp remote-locator-set {remote_locator_type}',
        'show lisp remote-locator-set name {remote_locator_name}',
        'show lisp {lisp_id} remote-locator-set {remote_locator_type}',
        'show lisp {lisp_id} remote-locator-set name {remote_locator_name}'
    """
    schema = {
        'lisp_id': {
            int: {
                'remote_locator_name': {
                    str: {
                        'rloc': {
                            str: {
                                'instance_id':{
                                    str: {
                                        'priority': str,
                                        'weight': str,
                                        Optional('metric'): str,
                                        Optional('domain_id'): str,
                                        Optional('multihome_id'): str,
                                        Optional('etr_type'): str,
                                        Optional('srvc_ins_id'): str,
                                        Optional('srvc_ins_type'): str
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispRemoteLocatorSet(ShowLispRemoteLocatorSetSchema):
    cli_command = ['show lisp remote-locator-set {remote_locator_type}',
                    'show lisp remote-locator-set name {remote_locator_name}',
                    'show lisp {lisp_id} remote-locator-set {remote_locator_type}',
                    'show lisp {lisp_id} remote-locator-set name {remote_locator_name}']

    def cli(self, lisp_id=None, remote_locator_type=None, remote_locator_name=None, output=None):
        if output is None:
            if lisp_id and remote_locator_type:
                cmd = self.cli_command[2].format(lisp_id=lisp_id, remote_locator_type=remote_locator_type)
            elif lisp_id and remote_locator_name:
                cmd = self.cli_command[3].format(lisp_id=lisp_id, remote_locator_name=remote_locator_name)
            elif remote_locator_type:
                cmd = self.cli_command[0].format(remote_locator_type=remote_locator_type)
            else:
                cmd = self.cli_command[1].format(remote_locator_name=remote_locator_name)
            output = self.device.execute(cmd)
        ret_dict = {}

        # LISP remote-locator-set default-etr-locator-set-ipv4 Information
        p1 = re.compile(r'^LISP\s+remote-locator-set\s+(?P<remote_locator_name>\S+)\s+Information$')

        # 7.7.7.7         2/3  /-          101                0/0      Default
        # 32.32.32.32   32/10 /0          -                  0/0      Service
        p2 = re.compile(r'^(?P<rloc>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(\*)?\s+'
                        r'(?P<priority>\d+)\/(?P<weight>[\d\s]+)'
                        r'(\/(?P<metric>[\d-]+))?\s+(?P<instance_id>\d+|-)'
                        r'(\s+)?(?P<domain_id>\d+)?(\/)?(?P<multihome_id>\d+)?'
                        r'(\s+(?P<etr_type>\S+))?(\s+)?(?P<srvc_ins_id>\S+)?(\s+)?'
                        r'(\/(?P<srvc_ins_type>\S+))?$')

        for line in output.splitlines():
            line = line.strip()

            # LISP remote-locator-set default-etr-locator-set-ipv4 Information
            m = p1.match(line)
            if m:
                lisp_id = int(lisp_id) if lisp_id else 0
                group = m.groupdict()
                remote_locator_name = group['remote_locator_name']
                lisp_dict = ret_dict.setdefault('lisp_id',{}).\
                                     setdefault(lisp_id,{}).\
                                     setdefault('remote_locator_name',{}).\
                                     setdefault(remote_locator_name,{})
                continue

            # 7.7.7.7         2/3  /-          101                0/0      Default
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rloc = group['rloc']
                priority = group['priority']
                weight = group['weight']
                instance_id = group['instance_id']
                rloc_dict = lisp_dict.setdefault('rloc',{}).\
                                      setdefault(rloc,{}).\
                                      setdefault('instance_id',{}).\
                                      setdefault(instance_id,{})
                rloc_dict.update({'priority':priority,
                                  'weight':weight})
                if group['metric']:
                    metric = group['metric']
                    rloc_dict.update({'metric':metric})
                if group['domain_id']:
                    domain_id = group['domain_id']
                    rloc_dict.update({'domain_id':domain_id})
                if group['multihome_id']:
                    multihome_id = group['multihome_id']
                    rloc_dict.update({'multihome_id':multihome_id})
                if group['etr_type']:
                    etr_type = group['etr_type']
                    rloc_dict.update({'etr_type':etr_type})
                if group['srvc_ins_id']:
                    srvc_ins_id = group['srvc_ins_id']
                    rloc_dict.update({'srvc_ins_id':srvc_ins_id})
                if group['srvc_ins_type']:
                    srvc_ins_type = group['srvc_ins_type']
                    rloc_dict.update({'srvc_ins_type':srvc_ins_type})
                continue
        return ret_dict
