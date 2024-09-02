"""show_lisp_super.py

    Super parsers for show_lisp.py
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


# ==============================
# Schema for 'show lisp session'
# ==============================
class ShowLispSessionSuperParserSchema(MetaParser):

    ''' Schema for "show lisp session" '''

    schema = {
        'vrf': {
            str : {
                'total': str,
                'established': str,
                Optional('peers'): {
                    str: ListOf({
                        Optional('port'): str,
                        'state': str,
                        'time': str,
                        'in': str,
                        'out': str,
                        'users': str,
                        Optional('rtt'): str
                        })
                    }
                }
            }
        }


# ==============================
# Parser for 'show lisp session'
# ==============================
class ShowLispSessionSuperParser(ShowLispSessionSuperParserSchema):

    ''' Parser for "show lisp session"'''
    def cli(self, output=None, vrf=None):

        # Init vars
        ret_dict = {}

        # Sessions for VRF default, total: 7, established: 4
        p1 = re.compile(r'^Sessions\s+for\s+VRF\s+(?P<vrf>\S+),\s+'
                        r'total:\s+(?P<total>\d+),\s+established:\s+'
                        r'(?P<established>\d+)$')

        # 201.201.201.201:22400          Up         00:03:22       14/16    4      125
        # 2001:2001:2001:2001::.22400    Up         00:03:22       14/16    4      125
        p2 = re.compile(r'^(?P<peers>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))'
                        r'((:|\.)(?P<port>\d+))?\s+(?P<state>\S+)\s+'
                        r'(?P<time>\S+)\s+(?P<in>\d+)'
                        r'\/(?P<out>\d+)\s+(?P<users>\d+)(\s+(?P<rtt>\d+))?$')

        for line in output.splitlines():
            line = line.strip()

            # Sessions for VRF default, total: 7, established: 4
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf']
                total = group['total']
                established = group['established']
                vrf_dict = ret_dict.setdefault('vrf',{}).\
                                    setdefault(vrf,{})
                vrf_dict.update({'total':total,
                                 'established':established})
                continue

            # 201.201.201.201:22400          Up         00:03:22       14/16    4      125
            # 2001:2001:2001:2001::.22400    Up         00:03:22       14/16    4      125
            m = p2.match(line)
            if m:
                group = m.groupdict()
                peers = group['peers']
                state = group['state']
                time = group['time']
                peer_in = group['in']
                out = group['out']
                users = group['users']
                peers_list = vrf_dict.setdefault('peers',{}).\
                                      setdefault(peers,[])
                if group['port'] and group['rtt']:
                    peers_list.append({'port':group['port'],
                                       'state':state,
                                       'time':time,
                                       'in':peer_in,
                                       'out':out,
                                       'users':users,
                                       'rtt':group['rtt']})
                elif group['rtt']:
                    peers_list.append({'state':state,
                                       'time':time,
                                       'in':peer_in,
                                       'out':out,
                                       'users':users,
                                       'rtt':group['rtt']})
                else:
                    peers_list.append({'state':state,
                                       'time':time,
                                       'in':peer_in,
                                       'out':out,
                                       'users':users})
                continue

        return ret_dict

# =======================================================================
# Schema for 'show lisp {lisp_id} instance-id <instance_id> <service> dabatase'
# =======================================================================
class ShowLispDatabaseSuperParserSchema(MetaParser):

    '''Schema for "show lisp <lisp_id> instance-id <instance_id> <service> dabatase" '''
    schema = {
        'lisp_id': {
            Any(): {
                'instance_id': {
                    int: {
                        'eid_table': str,
                        'lsb': str,
                        'entries': {
                            'total': int,
                            'no_route': int,
                            'inactive': int,
                            Optional('do_not_register'): int,
                            'eids': {
                                str: {
                                    'eid': str,
                                    'mask': int,
                                    Optional('do_not_register'): bool,
                                    Optional('dynamic_eid'): str,
                                    Optional('locator_set'): str,
                                    Optional('no_route_to_prefix'): bool,
                                    Optional('proxy'): bool,
                                    Optional('sgt'): str,
                                    Optional('domain_id'): str,
                                    Optional('service_insertion'): str,
                                    Optional('service_insertion_id'): int,
                                    Optional('auto_discover_rlocs'): bool,
                                    Optional('uptime'): str,
                                    Optional('last_change'): str,
                                    Optional('locators'): {
                                        str: {
                                            'priority': int,
                                            'weight': int,
                                            'source': str,
                                            'location': str,
                                            'state': str,
                                            Optional('affinity_id_x'): int,
                                            Optional('affinity_id_y'): int
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
        # LISP ETR IPv4 Mapping Database for EID-table vrf INTERNAL (IID 4099), LSBs: 0x1
        # LISP ETR IPv6 Mapping Database for LISP 0 EID-table vrf red (IID 4100), LSBs: 0x1
        p1 = re.compile(r'^LISP\s+ETR\s+(MAC|IPv6|IPv4)\s+Mapping\s+Database\s+for(\s+LISP\s+'
                        r'(?P<lisp_id>\d+))?\s+EID-table\s+'
                        r'(?P<eid_table>(vrf\s\w+)|(Vlan\s\d+)|default)\s+'
                        r'\(IID\s(?P<instance_id>\d+)\),\sLSBs:\s(?P<lsb>\S+)$')

        # Entries total 2, no-route 0, inactive 0, do-not-register 1
        p2 = re.compile(r'^Entries\s+total\s+(?P<total>\d+),\s+no-route\s+'
                        r'(?P<no_route>\d),\s+inactive\s+(?P<inactive>\d+)'
                        r'(,\s+do-not-register\s+(?P<do_not_register>\d+))?$')

        # aabb.cc00.c901/48, dynamic-eid Auto-L2-group-101, inherited from default locator-set RLOC *** NO ROUTE TO EID PREFIX ***
        p3 = re.compile(r'^(?P<eid>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}|'
                        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[a-fA-F\d\:]+)(\/)?'
                        r'(?P<mask>\d{1,3})(,\s)?(route-import)?'
                        r'(dynamic-eid\s+(?P<dynamic_eid>\S+))?'
                        r'(,\s(?P<do_not_register>do\snot\sregister))?(,\sinherited\sfrom\sdefault\s+)?'
                        r'((,\s)?locator-set\s(?P<locator_set>\S+))?'
                        r'(,\s(?P<auto_discover_rlocs>auto-discover-rlocs))?'
                        r'(\s\*\*\*\s(?P<no_route_to_prefix>NO ROUTE TO EID PREFIX)\s\*\*\*)?'
                        r'(,\s(?P<proxy>proxy))?(,\s(?P<default>default-ETR))?$')

        # Uptime: 1w3d, Last-change: 1w3d
        p4 = re.compile(r'^Uptime:\s+(?P<uptime>\S+),\s+Last-change:\s+(?P<last_change>\S+)$')

        # Domain-ID: local
        p5 = re.compile(r'^Domain-ID:\s+(?P<domain_id>\S+)$')

        # Service-Insertion: N/A 
        # Service-Insertion: N/A (0)
        p6 = re.compile(r'^Service-Insertion: (?P<service_insertion>[^\s]+)\s?(\((?P<service_insertion_id>\d+)\))?$')

        # SGT: 10
        p7 = re.compile(r'^SGT:\s+(?P<sgt>\d+)$')

        # 11.11.11.11   10/10   cfg-intf   site-self, reachable
        # 11:11:11:11:: 10/10   cfg-intf   site-self, reachable
        p8 = re.compile(r'^(?P<locators>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))'
                        r'\s+(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<source>\S+)'
                        r'\s+(?P<location>\S+),\s(?P<state>\S+)$')

        # Affinity-id: 20 , 20
        p9 = re.compile(r'^Affinity-id:\s+(?P<affinity_id_x>\d+)(\s+,\s+(?P<affinity_id_y>\d+))?$')

        lisp_id = "default"

        for line in output.splitlines():
            line = line.strip()

            # LISP ETR IPv4 Mapping Database for EID-table default (IID 1), LSBs: 0x1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if group['lisp_id']:
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
                if group['do_not_register']:
                    entries_dict['do_not_register'] = int(group['do_not_register'])
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
                if group['do_not_register']:
                    eid_dict.update({'do_not_register':True})
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
            # Service-Insertion: N/A (0)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                service_insertion = group['service_insertion'].strip()
                service_insertion_id = group['service_insertion_id']
                eid_dict.update({'service_insertion':service_insertion})
                if service_insertion_id is not None:
                    eid_dict.update({'service_insertion_id':int(service_insertion_id)})
                continue

            # SGT: 10
            m = p7.match(line)
            if m:
                group = m.groupdict()
                sgt = group['sgt']
                eid_dict.update({'sgt':sgt})
                continue

            # 11.11.11.11   10/10   cfg-intf   site-self, reachable
            # 11:11:11:11:: 10/10   cfg-intf   site-self, reachable
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
            
            # Affinity-id: 20 , 20
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                if groups['affinity_id_y']:
                    locator_dict.update({'affinity_id_y':int(groups['affinity_id_y'])})
                locator_dict.update({'affinity_id_x':int(groups['affinity_id_x'])})
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
                                        Optional('port'): int,
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
        p1 = re.compile(r'^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)')

        # Site Name      Last      Up     Who Last             Inst     EID Prefix
        #                Register         Registered           ID
        # Shire          never     no     --                   0        1.1.1.0/24
        #                00:00:06  yes*#  11.11.11.11:29972    10       2001:DB8::2/128
        p2 = re.compile(r'^((?P<site_name>\S+)\s+)?(?P<last_registered>\S+)\s+'
                        r'(?P<up>yes|no)\*?#?\s+(?P<who_last_registered>\S+)\s+'
                        r'(?P<instance_id>\d+)\s+(?P<eid_prefix>\d{1,3}\.'
                        r'\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3}'
                        r'|any-mac|([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{2})$')

        # Site Name      Last      Up     Who Last             Inst     EID Prefix
        #                Register         Registered           ID
        # Shire          00:00:06  yes*#  1000:1000:1000:1000:1000:1000:1000:1000
        #                                                      10       2001:DB8::2/128
        p3_1 = re.compile(r'^((?P<site_name>\S+)\s+)?(?P<last_registered>\S+)\s+'
                          r'(?P<up>yes|no)\*?#?\s+(?P<who_last_registered>\S+)$')
        p3_2 = re.compile(r'^(?P<instance_id>\d+)\s+(?P<eid_prefix>\d{1,3}\.'
                          r'\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3}'
                          r'|any-mac|([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{2})$')

        current_prefix_dict = {}
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

            # Site Name      Last      Up     Who Last             Inst     EID Prefix
            #                Register         Registered           ID
            # Shire          never     no     --                   0        1.1.1.0/24
            #                00:00:06  yes*#  11.11.11.11:29972    10       2001:DB8::2/128
            m = p2.match(line)
            if m:
                try:
                    lisp_id = int(lisp_id) if lisp_id else 0
                    lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                except ValueError:
                    pass
                group = m.groupdict()
                site_name = group['site_name']
                last_registered = group['last_registered']
                up = group['up']
                who_last_registered = group['who_last_registered']
                flag = 0
                if group['who_last_registered'].count(":") > 1:
                    (who_last_registered, port) = group['who_last_registered'].split(".")
                    flag = 1
                elif group['who_last_registered'].count(".") > 1:
                    (who_last_registered, port) = group['who_last_registered'].split(":")
                    flag = 1
                instance_id = int(group['instance_id'])
                eid_prefix = group['eid_prefix']
                if site_name:
                    site_dict = lisp_id_dict.setdefault('site_name', {}) \
                                            .setdefault(site_name, {})
                site_info = site_dict.setdefault('instance_id', {}) \
                                     .setdefault(instance_id, {}) \
                                     .setdefault('eid_prefix', {}) \
                                     .setdefault(eid_prefix, {})
                if flag:
                    site_info.update({'last_registered':last_registered,
                                      'who_last_registered':who_last_registered,
                                      'port':int(port),
                                      'up':up})
                else:
                    site_info.update({'last_registered':last_registered,
                                      'who_last_registered':who_last_registered,
                                      'up':up})
                continue

            # Site Name      Last      Up     Who Last             Inst     EID Prefix
            #                Register         Registered           ID
            # Shire          00:00:06  yes*#  1000:1000:1000:1000:1000:1000:1000:1000.27643
            #                                                      10       2001:DB8::2/128
            m = p3_1.match(line)
            if m:
                try:
                    lisp_id = int(lisp_id) if lisp_id else 0
                    lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                except ValueError:
                    pass
                group = m.groupdict()
                site_name = group['site_name']
                if site_name:
                    site_dict = lisp_id_dict.setdefault('site_name', {}) \
                                            .setdefault(site_name, {})
                who_last_registered=group['who_last_registered']
                port_flag=0
                if group['who_last_registered'].count(":") > 1:
                    (who_last_registered, port) = group['who_last_registered'].split(".")
                    port_flag=1
                elif group['who_last_registered'].count(".") > 1:
                    (who_last_registered, port) = group['who_last_registered'].split(":")
                    port_flag=1
                if port_flag:
                    current_prefix_dict.update({'last_registered':group['last_registered'],
                                            'who_last_registered':who_last_registered,
                                            'port':int(port),
                                            'up':group['up']})
                else:
                    current_prefix_dict.update({'last_registered':group['last_registered'],
                                            'who_last_registered':who_last_registered,
                                            'up':group['up']})
                continue

            m = p3_2.match(line)
            if m:
                group = m.groupdict()
                instance_id = int(group['instance_id'])
                eid_prefix = group['eid_prefix']

                site_info = site_dict.setdefault('instance_id', {}) \
                                     .setdefault(instance_id, {}) \
                                     .setdefault('eid_prefix', {}) \
                                     .setdefault(eid_prefix, {})
                if port_flag:
                    site_info.update({'last_registered':current_prefix_dict['last_registered'],
                                      'who_last_registered':current_prefix_dict['who_last_registered'],
                                      'port':current_prefix_dict['port'],
                                      'up':current_prefix_dict['up']})
                else:
                    site_info.update({'last_registered':current_prefix_dict['last_registered'],
                                      'who_last_registered':current_prefix_dict['who_last_registered'],
                                      'up':current_prefix_dict['up']})

                current_prefix_dict = {}
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
        # Map-Server(s): 1:1:1:1::
        p4_1 = re.compile(r'^Map-Server\(s\):\s+(?P<map_servers>(\d{1,3}\.\d{1,3}'
                          r'\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))$')

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
            # Map-Server(s): 1:1:1:1::
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
                                'pubsub_state': str,
                                Optional('type'): str
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

        # 23.23.23.23                 ETR Map-Server not found   Down    T     Off
        # 23.23.23.23                 Unreachable                Down    L     Off
        # 23.23.23.23                 Reachable                  Up
        # 2001:199:199:199::199       ETR Map-Server             Down    S     Off
        # 101.101.101.101             No ETR MS                  Down    ?     Established
        p2 = re.compile(r'^(?P<publisher_ip>[\da-fA-F\.:]+)\s+(?P<state>ETR Map-Server '
                        r'not found|ETR Map-Server|Unreachable|Reachable|No ETR MS)\s+'
                        r'(?P<session>\w+)\s+((?P<type>L|T|S|\?)\s+)?(?P<pubsub_state>\w+)$')

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

            # 23.23.23.23   ETR Map-Server not found   Down   Off
            # 23.23.23.23   Unreachable                Down   Off
            # 23.23.23.23   Reachable                  Down   Off
            # 23.23.23.23   No ETR MS                  Down   Off
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
                                Optional('exported_to'): list,
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
                                        Optional('sgt'): int,
                                        Optional('multihoming_id'): str,
                                        Optional('extranet_iid'): int,
                                        Optional('locators'): {
                                            str: {
                                                'priority': int,
                                                'weight': int,
                                                'state': str, # (up|down)
                                                'encap_iid': str,
                                                Optional('metric'): int,
                                                Optional('domain_id'): int,
                                                Optional('multihoming_id'): int,
                                                Optional('affinity_id_x'): int,
                                                Optional('affinity_id_y'): int,
                                                Optional('rdp'): str
                                            }
                                        }
                                    }
                                },
                                Optional('merged_locators'): {
                                    str: {
                                        'priority': int,
                                        'weight': int,
                                        'state': str, # (up|down)
                                        'encap_iid': str,
                                        'rdp_len': int,
                                        'src_add': str,
                                        'publishers': { # Same as src_add
                                            str: {
                                               'priority': int,
                                                'weight': int,
                                                'state': str,
                                                'encap_iid': str,
                                                'rdp_len': int
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

        # Publication Information for LISP 0 EID-table vrf red (IID 4100)
        p1 = re.compile(r"^Publication\s+Information\s+for\s+LISP\s+"
                        r"(?P<lisp_id>\d+)\s+EID-table\s+vrf\s+\S+\s+"
                        r"\(IID\s+(?P<instance_id>\d+)\)$")

        # EID-prefix: 192.168.1.71/32
        # EID-prefix: 2001:172:168:1::/64
        p2 = re.compile(r"^EID-prefix:\s+(?P<eid_prefixes>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}"
                        r"|[a-fA-F\d\:]+\/\d{1,3})|([a-fA-F\d\:]+\/\d{1,3}))$")

        # First published:      03:05:56
        p3 = re.compile(r"^First\s+published:\s+(?P<first_published>\S+)$")

        # Last published:      03:05:56
        p4 = re.compile(r"^Last\s+published:\s+(?P<last_published>\S+)$")

        # State:                complete
        p5 = re.compile(r"^State:\s+(?P<state>\S+)$")

        # Exported to:          map-cache
        # Exported to:          local-eid, map-cache
        p6 = re.compile(r"^Exported\s+to:\s+(?P<exported_to>[\s\S]+)$")

        # Publisher 100.100.100.100:4342, last published 16:02:47, TTL never
        # Publisher 2001:13:13:13::13.4342, last published 00:03:35, TTL never, Expires: never
        p7 = re.compile(r"^Publisher\s+(?P<publishers>((\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})?"
                        r"|([a-fA-F\d\:]+)))?\.?\:?(?P<port>\d+),\s+last\s+published\s+"
                        r"(?P<last_published>\S+),\s+TTL\s+(?P<ttl>\w+)")

        # publisher epoch 1, entry epoch 1
        p8 = re.compile(r"^publisher\s+epoch\s+(?P<publisher_epoch>\d+),"
                        r"\s+entry\s+epoch\s+(?P<entry_epoch>\d+)")

        # entry-state complete
        p9 = re.compile(r"^entry-state\s+(?P<entry_state>\S+)")

        # routing table tag 101
        p10 = re.compile(r"^routing\s+table\s+tag\s+(?P<routing_tag>\d+)")

        # xTR-ID 0x790800FF-0x426D6D8E-0xC6C5F60C-0xB4386D22
        p11 = re.compile(r"^xTR-ID\s+(?P<xtr_id>\S+)")

        # site-ID unspecified
        p12 = re.compile(r"^site-ID\s+(?P<site_id>\S+)")

        # Domain-ID unset
        p13 = re.compile(r"^Domain-ID\s+(?P<domain_id>\S+)")

        # Multihoming-ID unspecified
        p14 = re.compile(r"^Multihoming-ID\s+(?P<multihoming_id>\S+)")

        # Merge Locator Information
        # Locator        Pri/Wgt  State     Encap-IID  RDP-Len Src-Address
        # 100.88.88.88    20/90   up        -          0       100.77.77.77
        # 100::88:88:88   20/90   up        -          0       100.77.77.77
        p15 = re.compile(r"^(?P<merged_locators>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+)\S+)\s+"
                         r"(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<state>\S+)\s+(?P<encap_iid>\S+)\s+"
                         r"(?P<rdp_len>\d+)\s+(?P<src_add>\S+)$")

        # 100.88.88.88  100/50   up        -                   [-]
        p16 = re.compile(r"^(?P<locators>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+"
                         r"(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<state>\S+)\s+(?P<encap_iid>\S+)"
                         r"\s+(?P<rdp>\S+)")

        # 100.88.88.88  100/50   up        -                   1/1       44
        # 2001:2:2:2::2   50/50   up        -                  1/1       44
        p17 = re.compile(r"^(?P<locators>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+"
                         r"(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<state>\S+)\s+(?P<encap_iid>\S+)"
                         r"|\s+(?P<domain_id>\d+)\/(?P<multihoming_id>\d+)\s+(?P<metric>\d+)")

        # Affinity-id: 20 , 20
        p18 = re.compile(r'^Affinity-id:\s+(?P<affinity_id_x>\d+)(\s+,\s+(?P<affinity_id_y>\d+))?$')

        # Instance ID:                              4100
        p19 = re.compile(r"^\s+Instance\s+ID:\s+(?P<inst_id>\S+)")

        # Publisher 100.100.100.100:4342
        p20 = re.compile(r"^Publisher\s+(?P<publishers>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
                        r":(?P<port>\d+)$")

        # Publisher 100::100:100:100.4342
        p21 = re.compile(r"^Publisher\s+(?P<publishers>[a-fA-F\d\:]+)\.(?P<port>\d+)$")

        # last published 16:02:47, TTL never
        p22 = re.compile(r"^last\s+published\s+(?P<last_published>\S+),\s+TTL\s+(?P<ttl>\w+)")

        # SGT 100
        p23 = re.compile(r"^SGT\s+(?P<sgt>\d+)$")

        for line in output.splitlines():
            line = line.strip()
            count += 1

            # Publication Information for LISP 0 EID-table vrf red (IID 4100)
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

            # EID-prefix: 192.168.1.71/3
            # EID-prefix: 2001:172:168:1::/64
            m = p2.match(line)
            if m:
                if not lisp_id and instance_id != "*":
                    lisp_id = 0
                    instance_id = int(instance_id)
                    lisp_id_dict = lisp_v4_pub_pre.setdefault('lisp_id',{})\
                                                .setdefault(lisp_id,{})
                    instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                               .setdefault(instance_id,{})
                groups = m.groupdict()
                eid_prefixes = groups['eid_prefixes']
                eid_prefix_dict = instance_id_dict.setdefault('eid_prefixes',{})\
                                                  .setdefault(eid_prefixes,{})
                continue

            # First published:      03:05:56
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                first_published = groups['first_published']
                eid_prefix_dict.update({'first_published':first_published})
                continue

            # Last published:      03:05:56
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                last_published = groups['last_published']
                eid_prefix_dict.update({'last_published':last_published})
                continue

            # State:                complete
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                state = groups['state']
                eid_prefix_dict.update({'state':state})
                continue

            # Exported to:          map-cache
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                exported_to = groups['exported_to']
                exported_list = eid_prefix_dict.setdefault('exported_to',[])
                exported_list.append(exported_to)
                eid_prefix_dict.update({'exported_to':exported_list})
                continue

            # Publisher 100.100.100.100:4342, last published 16:02:47, TTL never
            # Publisher 2001:4:4:4::4.4342, last published 00:00:52, TTL never, Expires: never'
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

            # publisher epoch 0,entry epoch 0
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                publisher_epoch = int(groups['publisher_epoch'])
                entry_epoch = int(groups['entry_epoch'])
                publish_dict.update({'publisher_epoch':publisher_epoch})
                publish_dict.update({'entry_epoch':entry_epoch})
                continue

            # entry-state complete
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                entry_state = groups['entry_state']
                publish_dict.update({'entry_state':entry_state})
                continue

            # routing table tag 101
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                routing_tag = int(groups['routing_tag'])
                publish_dict.update({'routing_tag':routing_tag})
                continue

            # xTR-ID 0x790800FF-0x426D6D8E-0xC6C5F60C-0xB4386D22
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                xtr_id = groups['xtr_id']
                publish_dict.update({'xtr_id':xtr_id})
                continue

            # site-ID unspecified
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                site_id = groups['site_id']
                publish_dict.update({'site_id':site_id})
                continue

            # Domain-ID unset
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                domain_id = (groups['domain_id'])
                publish_dict.update({'domain_id':domain_id})
                continue

            # Multihoming-ID unspecified
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                multihoming_id = (groups['multihoming_id'])
                publish_dict.update({'multihoming_id':multihoming_id})
                continue

            # Merge Locator Information
            # Locator        Pri/Wgt  State     Encap-IID  RDP-Len Src-Address
            # 100.88.88.88    20/90   up        -          0       100.77.77.77
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                merged_locators = (groups['merged_locators'])
                priority = int(groups['priority'])
                weight = int(groups['weight'])
                state = groups['state']
                encap_iid = groups['encap_iid']
                rdp_len = int(groups['rdp_len'])
                src_add = groups['src_add']
                merged_dict = eid_prefix_dict.setdefault('merged_locators',{})\
                                             .setdefault(merged_locators,{})
                merged_dict.update({'priority':priority})
                merged_dict.update({'weight':weight})
                merged_dict.update({'state':state})
                merged_dict.update({'encap_iid':encap_iid})
                merged_dict.update({'rdp_len':rdp_len})
                merged_dict.update({'src_add':src_add})

                # Merge Locator Information
                #     Locator           Pri/Wgt  State     Encap-IID  RDP-Len Src-Address
                #     100.88.88.88       10/50   up        -          0       100.44.44.44
                #     100.88.88.88       10/50   up        -          1       100.78.78.78
                merged_publisher_dict = merged_dict.setdefault('publishers',{}) \
                                                   .setdefault(src_add,{})
                merged_publisher_dict.update({'priority':priority})
                merged_publisher_dict.update({'weight':weight})
                merged_publisher_dict.update({'state':state})
                merged_publisher_dict.update({'encap_iid':encap_iid})
                merged_publisher_dict.update({'rdp_len':rdp_len})
                continue

            # 22.22.22.22   10/10   up        -      [-]
            m = p16.match(line)
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
                if groups['rdp'] != None:
                    rdp = groups['rdp']
                    locator_dict.update({'rdp':rdp})
                continue

            # 100.88.88.88  100/50   up        -                   1/1       44
            m = p17.match(line)
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

            # Affinity-id: 20 , 20
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                affinity_id_x = int(groups['affinity_id_x'])
                if groups['affinity_id_y']:
                    affinity_id_y = int(groups['affinity_id_y'])
                    locator_dict.update({'affinity_id_x':affinity_id_x,
                                         'affinity_id_y':affinity_id_y})
                else:
                    locator_dict.update({'affinity_id_x':affinity_id_x})
                continue

            # Publisher 100.100.100.100:4342
            m = p20.match(line)
            if m:
                groups = m.groupdict()
                publishers = groups['publishers']
                port = int(groups['port'])
                publishers = "{}:{}".format(publishers,port)
                publish_dict = eid_prefix_dict.setdefault('publishers',{})\
                                              .setdefault(publishers,{})
                publish_dict.update({'port':port})
                continue

            # Publisher 100::100:100:100:100:100.4342
            m = p21.match(line)
            if m:
                groups = m.groupdict()
                publishers = groups['publishers']
                port = int(groups['port'])
                publishers = "{}.{}".format(publishers,port)
                publish_dict = eid_prefix_dict.setdefault('publishers',{})\
                                              .setdefault(publishers,{})
                publish_dict.update({'port':port})
                continue

        # last published 16:02:47, TTL never
            m = p22.match(line)
            if m:
                groups = m.groupdict()
                last_published = groups['last_published']
                ttl = groups['ttl']
                publish_dict.update({'last_published':last_published})
                publish_dict.update({'ttl':ttl})
                continue

            # SGT 100
            m = p23.match(line)
            if m:
                groups = m.groupdict()
                sgt = int(groups['sgt'])
                publish_dict.update({'sgt':sgt})
                continue

        return lisp_v4_pub_pre

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
                                    'type': str,
                                    Optional('affinity_id_x'): int,
                                    Optional('affinity_id_y'): int
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
                subscribers_dict = lisp_id_dict.setdefault('subscribers', {}).setdefault(group['subscriber_ip'], [])
                if group['affinity_id_y']:
                    subscribers_dict.append({'port': int(group['port']),
                                             'type': group['type'],
                                             'affinity_id_x':int(group['affinity_id_x']),
                                             'affinity_id_y':int(group['affinity_id_y'])})
                elif group['affinity_id_x']:
                    subscribers_dict.append({'port': int(group['port']),
                                             'type': group['type'],
                                             'affinity_id_x':int(group['affinity_id_x'])})
                else:
                    subscribers_dict.append({'port': int(group['port']),
                                             'type': group['type']})
                continue
        return ret_dict

class ShowLispSubscriptionSchema(MetaParser):

    ''' Schema for
        show lisp instance-id {instance_id} ipv4 subscription
        show lisp {lisp_id} instance-id {instance_id} ipv4 subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 subscription
        show lisp eid-table {eid_table} ipv4 subscription
        show lisp eid-table vrf {eid_table} ipv4 subscription
        show lisp instance-id {instance_id} ipv6 subscription
        show lisp {lisp_id} instance-id {instance_id} ipv6 subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 subscription
        show lisp eid-table {eid_table} ipv6 subscription
        show lisp eid-table vrf {eid_table} ipv6 subscription
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'eid_table': str,
                        'entries': int,
                        Optional('eid_prefix'): {
                            str: { # EID prefix
                                'source': str,
                                Optional('created'): str,
                                Optional('last_update'): str
                                }
                            }
                        }
                    }
                }
            }
        }

class ShowLispSubscriptionSuperParser(ShowLispSubscriptionSchema):
    
    ''' 
        Schema for
        show lisp instance-id {instance_id} ipv4 subscription
        show lisp {lisp_id} instance-id {instance_id} ipv4 subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 subscription
        show lisp eid-table {eid_table} ipv4 subscription
        show lisp eid-table vrf {eid_table} ipv4 subscription
        show lisp instance-id {instance_id} ipv6 subscription
        show lisp {lisp_id} instance-id {instance_id} ipv6 subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 subscription
        show lisp eid-table {eid_table} ipv6 subscription
        show lisp eid-table vrf {eid_table} ipv6 subscription
    '''
    
    def cli(self, lisp_id=None, instance_id=None, output=None):
        parsed_dict = {}

        # LISP EID Subscriptions for LISP 0 EID-table vrf red (IID 4100), 2 entries
        p1 = re.compile(r"^LISP\s+EID\s+Subscriptions\s+for(\s+LISP\s+"
                        r"(?P<lisp_id>\d+))?\s+EID-table\s+(vrf\s+|Vlan\s+)?(?P<eid_table>\S+)\s+"
                        r"\(IID\s+(?P<instance_id>\d+)\),\s+(?P<entries>\d+)\s+entries$")

        #Prefix                                  Source                         Created     Last Update
        #2.2.2.0/24                              remote-eid,eid-watch           00:01:58    00:01:58   
        #172.168.0.0/16                          remote-eid                     20:53:49    20:53:49   
        #aaaa.aaaa.aaaa/48                       remote-eid                     20:53:49    20:53:49
        p2 = re.compile(r"^(?P<eid_prefix>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
                        r"\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3}|"
                        r"([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{2})\s+"
                        r"(?P<source>\S+)\s+" 
                        r"(?P<created>\S+)\s+(?P<last_update>\S+)$")

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
                instance_id_dict.update({'eid_table': group['eid_table']})
                instance_id_dict.update({'entries': int(group['entries'])})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict = instance_id_dict.setdefault('eid_prefix',{})\
                                                    .setdefault(str(group['eid_prefix']), {})
                eid_prefix_dict.update({'source': group['source'].strip()})
                eid_prefix_dict.update({'created': group['created'].strip()})
                eid_prefix_dict.update({'last_update': group['last_update'].strip()})
                continue

        return parsed_dict

class ShowLispSubscriptionPrefixSchema(MetaParser):

    ''' Schema for
        show lisp instance-id {instance_id} ipv4 subscription {eid_prefix}/detail
        show lisp {lisp_id} instance-id {instance_id} ipv4 subscription {eid_prefix}/detail
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 subscription {eid_prefix}/detail
        show lisp eid-table {eid_table} ipv4 subscription {eid_prefix}/detail
        show lisp eid-table vrf {eid_table} ipv4 subscription {eid_prefix}/detail
        show lisp instance-id {instance_id} ipv6 subscription {eid_prefix}/detail
        show lisp {lisp_id} instance-id {instance_id} ipv6 subscription {eid_prefix}/detail
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 subscription {eid_prefix}/detail
        show lisp eid-table {eid_table} ipv6 subscription {eid_prefix}/detail
        show lisp eid-table vrf {eid_table} ipv6 subscription {eid_prefix}/detail
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'eid_table': str,
                        'entries': int,
                        Optional('eid_prefix'): {
                            str: { # EID prefix
                                Optional('source'): str,
                                Optional('up_time'): str,
                                Optional('last_change'): str,
                                Optional('map_server'): {
                                    str: { #map server eid
                                        'state' : str
                                        }   
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    
class ShowLispSubscriptionPrefixSuperParser(ShowLispSubscriptionPrefixSchema):
    
    ''' 
        Schema for
        show lisp instance-id {instance_id} ipv4 subscription
        show lisp {lisp_id} instance-id {instance_id} ipv4 subscription
        show lisp instance-id {instance_id} ipv6 subscription
        show lisp {lisp_id} instance-id {instance_id} ipv6 subscription
    '''
    
    def cli(self, lisp_id=None, instance_id=None, output=None):
        parsed_dict = {}

        # LISP EID Subscriptions for LISP 0 EID-table vrf red (IID 4100), 2 entries
        p1 = re.compile(r"^LISP\s+EID\s+Subscriptions\s+for(\s+LISP\s+"
                        r"(?P<lisp_id>\d+))?\s+EID-table\s+(vrf\s+|Vlan\s+)?(?P<eid_table>\S+)\s+"
                        r"\(IID\s+(?P<instance_id>\d+)\),\s+(?P<entries>\d+)\s+entries$")
        
        # 172.168.0.0/16, Uptime: 00:01:15, Last-change: 00:01:15
        p2 = re.compile(r"^(?P<eid_prefix>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
                        r"\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3}|"
                        r"([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{2}),\sUptime:\s+"
                        r"(?P<up_time>\S+),\sLast-change:\s+(?P<last_change>\S+)$")
        
        # Source: remote-eid
        p3 = re.compile(r"^Source:\s+(?P<source>\S+)$")
        
        # Map-server                              State                          
        # 100.44.44.44                            Subs Acked                     
        # 100.55.55.55                            Subs Acked
        p4 = re.compile(r"^(?P<map_server>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+(?P<state>.+)")
        
        for line in output.splitlines():
            line = line.strip()
            
            # LISP EID Subscriptions for LISP 0 EID-table vrf red (IID 4100), 2 entries
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id_dict = \
                    parsed_dict.setdefault('lisp_id', {}) \
                        .setdefault(int(group['lisp_id']), {})
                instance_id_dict = \
                    lisp_id_dict.setdefault('instance_id', {}) \
                        .setdefault(int(group['instance_id']), {})
                instance_id_dict.update({'eid_table': group['eid_table']})
                instance_id_dict.update({'entries': int(group['entries'])})
                continue

            # 172.168.0.0/16, Uptime: 00:01:15, Last-change: 00:01:15
            m = p2.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict = instance_id_dict.setdefault('eid_prefix',{})\
                                                    .setdefault(str(group['eid_prefix']), {})
                eid_prefix_dict.update({'up_time': group['up_time'].strip()})
                eid_prefix_dict.update({'last_change': group['last_change'].strip()})
                continue

            # Source: remote-eid
            m = p3.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict.update({'source': group['source'].strip()})
                continue
            
            # Map-server                              State                          
            # 100.44.44.44                            Subs Acked                     
            # 100.55.55.55                            Subs Acked
            m = p4.match(line)
            if m:
                group = m.groupdict()
                map_server_dict = eid_prefix_dict.setdefault('map_server',{})\
                                                    .setdefault(str(group['map_server']), {})
                map_server_dict.update({'state': group['state'].strip()})
                continue
            
        return parsed_dict

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
                        Optional('counters_not_accurate'): bool,
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
                                Optional('itr_rloc'): str,
                                Optional('affinity_id_x'): int,
                                Optional('affinity_id_y'): int
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
        # LISP IPv4 Mapping Cache for LISP 0 EID-table default (IID 10), 2 entries
        p1 = re.compile(r"^LISP\s+(IPv4|IPv6|MAC)\s+Mapping\s+Cache\s+for(\s+LISP\s+"
                        r"(?P<lisp_id>\d+))?\s+EID-table\s+(vrf\s+|Vlan\s+)?(?P<eid_table>\S+)\s+"
                        r"\(IID\s+(?P<instance_id>\d+)\),\s+(?P<entries>\d+)\s+entries$")

        # 191.168.1.11/32, uptime: 02:26:35, expires: 21:33:24, via map-reply, self, complete, remote-to-site
        # 2001:194:168:1::72/128, uptime: 00:44:35, expires: 23:15:25, via map-reply, complete
        # 2001:194:168:1::72/128, uptime: 00:44:35, expires: 1d11h, via map-reply, complete
        p2 = re.compile(r"^(?P<eid>[a-fA-F\d\:\.]+)\/(?P<mask>\d{1,3}),\s+uptime:\s+"
                         r"(?P<uptime>\S+),\s+expires:\s+(?P<expires>(\d{2}:?){3}|never|(\dw\dd)|(\dd\d{1,2}h)),"
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
        # Active, Packets out: 2(1152 bytes), counters are not accurate (~ 00:01:05 ago)
        p7 = re.compile(r"^(?P<activity>Idle|Active|Exempt),\s+Packets\s+out:\s+"
                        r"(?P<packets_out>\d+)\((?P<packets_out_bytes>\d+)\s+bytes\)"
                        r"(,\s+(?P<counters_not_accurate>counters are not accurate))?"
                        r"(\s+\(\W+\d{1,2}:\d{2}:\d{2}\s+ago\))?$")

        # Negative cache entry, action: send-map-request
        p8 = re.compile(r"^Negative\s+cache\s+entry,\s+action:\s+(?P<action>\S+)$")

        # 101.101.101.101  02:26:35  up           1/100       -             1/2           -
        # 45.45.45.45  00:00:04  up, self    10/50   111                 3/3      0
        p9 = re.compile(r"^(?P<locators>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[a-fA-F\d\:]+)\s+"
                        r"(?P<uptime>\S+)\s+(?P<state>\S+)(,\s+self)?\s+"
                        r"(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<encap_iid>\S+)|\s+"
                        r"(?P<domain_id>\d+)\/(?P<multihome_id>\d+)\s+(?P<metric>\S+)$")

        # Last up-down state change:         02:26:35, state change count: 1
        p10 = re.compile(r"^Last\s+up-down\s+state\s+change:\s+"
                         r"(?P<state_change_time>\d{1,2}:\d{2}:\d{2}|\dw\dd),"
                         r"\s+state\s+change\s+count:\s+(?P<state_change_count>\d+)$")

        # Last route reachability change:    02:26:35, state change count: 1
        p11 = re.compile(r"^Last\s+route\s+reachability\s+change:\s+"
                         r"(?P<route_reachability_change_time>\d{1,2}:\d{2}:\d{2}|\dw\dd|never),\s+"
                         r"state\s+change\s+count:\s+(?P<route_reachability_change_count>\d+)$")

        # Last priority / weight change:     never/never
        p12 = re.compile(r"^Last\s+priority\s+\/\s+weight\s+change:\s+"
                         r"(?P<priority_change>\S+)\/(?P<weight_change>\S+)$")

        # RLOC route rejection reason:       reachability (minimum mask length check failed)
        p13 = re.compile(r"^RLOC\s+route\s+rejection\s+reason:\s+"
                         r"(?P<reject_reason>[\(\)\w\s-]+)$")

        # Last RLOC-probe sent:            00:24:49 (rtt 1ms)
        p14 = re.compile(r"^Last\s+RLOC-probe\s+sent:\s+"
                         r"(?P<rloc_probe_sent>\d{2}:\d{2}:\d{2}\s+\(rtt\s+\d+ms\)|never)$")

        # Next RLOC-probe in:              00:47:14
        p15 = re.compile(r"^Next\s+RLOC-probe\s+in:\s+"
                         r"(?P<rloc_probe_in>\d{2}:\d{2}:\d{2})$")

        # Latched to ITR-RLOC:             104.104.104.104
        # Latched to ITR-RLOC:             104:104:104:104::
        p16 = re.compile(r"^Latched\s+to\s+ITR-RLOC:\s+"
                         r"(?P<itr_rloc>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))$")

        # Affinity-id: 20 , 20
        p17 = re.compile(r'^Affinity-id:\s+(?P<affinity_id_x>\d+)(\s+,\s+(?P<affinity_id_y>\d+))?$')
        
        for line in output.splitlines():
            line = line.strip()

            # LISP IPv4 Mapping Cache for LISP 0 EID-table vrf red (IID 100), 3 entries
            # LISP IPv6 Mapping Cache for LISP 0 EID-table vrf red (IID 100), 3 entries
            # LISP IPv4 Mapping Cache for EID-table vrf red (IID 4100), 3 entries
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                if groups['lisp_id']:
                    lisp_id = int(groups['lisp_id'])
                else:
                    lisp_id = int(lisp_id) if lisp_id else 0
                instance_id = int(groups['instance_id'])
                eid_table = groups['eid_table']
                entries = int(groups['entries'])
                instance_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {}).setdefault('instance_id',{}).setdefault(instance_id,{})
                instance_id_dict.update({'eid_table':eid_table,'entries':entries})
                continue

            # 191.168.1.11/32, uptime: 02:26:35, expires: 21:33:24, via map-reply, self, complete, remote-to-site
            # 2001:194:168:1::72/128, uptime: 00:44:35, expires: 23:15:25, via map-reply, complete
            # 2001:194:168:1::72/128, uptime: 00:44:35, expires: 1d11h, via map-reply, complete
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
            # Active, Packets out: 2(1152 bytes), counters are not accurate (~ 00:01:05 ago)
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                activity = groups['activity']
                packets_out = int(groups['packets_out'])
                packets_out_bytes = int(groups['packets_out_bytes'])
                instance_id_dict.update({'activity':activity,
                                         'packets_out':packets_out,
                                         'packets_out_bytes':packets_out_bytes})
                if groups['counters_not_accurate']:
                    counters_not_accurate = groups['counters_not_accurate']
                    counters_not_accurate_bool = counters_not_accurate == "counters are not accurate"
                    instance_id_dict.update({'counters_not_accurate':counters_not_accurate_bool})
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
            # Latched to ITR-RLOC:             104:104:104:104::
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                itr_rloc = groups['itr_rloc']
                locators_dict.update({'itr_rloc':itr_rloc})
                continue
            
            # Affinity-id: 20 , 20
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                if groups['affinity_id_y']:
                    locators_dict.update({'affinity_id_y':int(groups['affinity_id_y'])})
                locators_dict.update({'affinity_id_x':int(groups['affinity_id_x'])})
                continue
        return ret_dict


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
                        Optional('instance_id'): {
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
                                        Optional('sgt'): int,
                                        Optional('etr'): {
                                            str: {
                                                Optional('port'): int,
                                                'last_registered': str,
                                                'proxy_reply': bool,
                                                'map_notify': bool,
                                                'ttl': str,
                                                Optional('nonce'): str,
                                                'state': str,
                                                'xtr_id': str,
                                                Optional('domain_id'): str,
                                                Optional('multihoming_id'): str,
                                                Optional('affinity_id_x'): int,
                                                Optional('affinity_id_y'): int,
                                                'locators': {
                                                    str: {
                                                        'local': str,
                                                        'state': str,
                                                        'priority': int,
                                                        'weight': int,
                                                        'scope': str,
                                                        Optional('rdp'): str
                                                        }
                                                    }
                                                }
                                            },
                                        Optional('merged_locators'): {
                                            str: {
                                                'local': str,
                                                'state': str,
                                                'priority': int,
                                                'weight': int,
                                                'scope': str,
                                                'reg_etr': str,
                                                Optional('port'): int,
                                                'rdp': str
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
        # EID-prefix: any-mac instance-id 101
        p3 = re.compile(r"^EID-prefix:\s+(?P<eid_prefix>\d{1,3}\.\d{1,3}\."
                        r"\d{1,3}\.\d{1,3}\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3}"
                        r"|([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{1,3}|any-mac)"
                        r"\s+instance-id\s+(?P<instance_id>\d+)$")

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
        # ETR 100.99.99.99:34273, last registered 00:00:39, no proxy-reply, map-notify
        # ETR 11.11.11.11, last registered 00:45:46, proxy-reply, map-notify
        p17 = re.compile(r"(^ETR\s+((?P<etrp>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+),|(?P<etr>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}),))"
                         r"\s+last\s+registered\s+(?P<last_registered>\d{1,2}:\d{2}:\d{2}|\dw\dd),"
                         r"\s+(?P<proxy_reply>[\S\s]+),\s+(?P<map_notify>map-notify)$")

        # TTL 1d00h, no merge, hash-function sha1, nonce 0x4536735E-0xE5D90458
        # TTL 1d00h, merge, hash-function sha1
        p18 = re.compile(r"^TTL\s+(?P<ttl>\S+),\s+(no\s+)?merge,\s+"
                         r"hash-function\s+sha1(,\s+nonce\s+(?P<nonce>\S+))?$")

        # nonce 0x4536735E-0xE5D90458
        p18_1 = re.compile(r"^nonce\s+(?P<nonce>\S+)$")

        # state complete, no security-capability
        p19 = re.compile(r"^state\s+(?P<state>\S+),\s+no\s+security-capability$")

        # xTR-ID 0xE52CBAD5-0x38D3485F-0x97DC3A75-0xC27B2130
        p20 = re.compile(r"^xTR-ID\s+(?P<xtr_id>\S+)$")

        # Domain-ID local
        p21 = re.compile(r"^Domain-ID\s+(?P<domain_id>local)$")

        # Domain-ID '1'
        p21_1 = re.compile(r"^Domain-ID\s+(?P<domain_id>\S+)$")

        # Multihoming-ID unspecified
        p22 = re.compile(r"^Multihoming-ID\s+(?P<multihoming_id>\S+)$")

        # Affinity-id: 20 , 20
        p22_1 = re.compile(r'^Affinity-id:\s+(?P<affinity_id_x>\d+)(\s+,\s+(?P<affinity_id_y>\d+))?$')

        # 22.22.22.22    yes    up          10/10   IPv4 none
        # 22:22:22:22::  yes    up          10/10   IPv4 none
        # 22:22:22:22::  yes    up          10/10   IPv6 none
        p23 = re.compile(r"^(?P<locators>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+"
                         r"(?P<local>yes|no)\s+(?P<state>\S+)\s+(?P<priority>\d+)"
                         r"\/(?P<weight>\d+)\s+(?P<scope>IPv4|IPv6)\snone$")

        # 22.22.22.22    yes    up          10/10   IPv4 none     [-]
        # 22:22:22:22::  yes    up          10/10   IPv6 none     [-]
        p24 = re.compile(r"^(?P<locators>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+"
                         r"(?P<local>yes|no)\s+(?P<state>\S+)\s+(?P<priority>\d+)"
                         r"\/(?P<weight>\d+)\s+(?P<scope>IPv4|IPv6)\snone\s+(?P<rdp>\S+)$")  

        # Merged locators
        #  Locator       Local  State      Pri/Wgt  Scope        Registering ETR          RDP
        #  100.99.99.99  yes    up          10/50   IPv4 none    100.99.99.99:30343       [-]
        #  A0:EE:EE::EE  yes    up          10/50   IPv6 none    A0:EE:EE::EE.30343       [-]
        p25 = re.compile(r"^(?P<merged_locators>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+"
                         r"(?P<local>yes|no)\s+(?P<state>\S+)\s+(?P<priority>\d+)"
                         r"\/(?P<weight>\d+)\s+(?P<scope>IPv4|IPv6)\snone\s+"
                         r"((?P<etrp>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)|([a-fA-F\d\:]+\.\d+))|"
                         r"(?P<etr>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+)))\s+"
                         r"(?P<rdp>\S+)$")

        # ETR 11.11.11.11:33079
        # ETR 11.11.11.11
        p26 = re.compile(r"(^ETR\s+((?P<etrp>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)|"
                         r"(?P<etr>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})))$")

        # ETR 100:99:99:99::
        # ETR 100:99:99:99::.34273
        p27 = re.compile(r"(^ETR\s+((?P<etrp>[a-fA-F\d\:]+\.\d+)|(?P<etr>[a-fA-F\d\:]+)))$")

        # last registered 00:45:46, proxy-reply, map-notify
        p28 = re.compile(r"last\s+registered\s+(?P<last_registered>\d{1,2}:\d{2}:\d{2}|\dw\dd),"
                         r"\s+(?P<proxy_reply>[\S\s]+),\s+(?P<map_notify>map-notify)$")

        # SGT: 10
        p29 = re.compile(r'SGT:\s+(?P<sgt>\d+)$')

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
            # EID-prefix: any-mac instance-id 101
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
                port = 0
                groups = m.groupdict()

                if groups['etrp']:

                    etrp = str(groups['etrp'])
                    (etr,port) = etrp.split(":")

                elif groups['etr']:
                    etr = groups['etr']

                etr_dict = instance_dict.setdefault('etr',{})\
                                        .setdefault(etr,{})

                if port != 0:
                   etr_dict.update({'port':int(port)})

                last_registered = groups['last_registered']
                proxy_reply = groups['proxy_reply']
                map_notify = groups['map_notify']
                proxy_reply_bool = proxy_reply == "proxy-reply"
                map_notify_bool = bool(re.search("map-notify",map_notify))

                etr_dict.update({'last_registered':last_registered,
                                 'proxy_reply':proxy_reply_bool,
                                 'map_notify':map_notify_bool})
                continue

            # TTL 1d00h, no merge, hash-function sha1, nonce 0xC7E970BF-0x125C7F7B
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                ttl = groups['ttl']
                etr_dict.update({'ttl':ttl})
                if groups['nonce']:
                    nonce = groups['nonce']
                    etr_dict.update({'nonce':nonce})
                continue

            #nonce 0xC7E970BF-0x125C7F7B
            m = p18_1.match(line)
            if m:
                groups = m.groupdict()
                nonce = groups['nonce']
                etr_dict.update({'nonce':nonce})
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

            # Domain-ID '1'
            m = p21_1.match(line)
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

            # Affinity-id: 20 , 20
            m = p22_1.match(line)
            if m:
                groups = m.groupdict()
                affinity_id_x = int(groups['affinity_id_x'])
                if groups['affinity_id_y']:
                    affinity_id_y = int(groups['affinity_id_y'])
                    etr_dict.update({'affinity_id_x':affinity_id_x,
                                     'affinity_id_y':affinity_id_y})
                else:
                    etr_dict.update({'affinity_id_x':affinity_id_x})
                continue

            # 22.22.22.22    yes    up          10/10   IPv4 none
            # 22:22:22:22::  yes    up          10/10   IPv6 none
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

            # 22.22.22.22   yes    up          10/10   IPv4 none     [-]
            # 22:22:22:22:: yes    up          10/10   IPv6 none     [-]
            m = p24.match(line)
            if m:
                groups = m.groupdict()
                locators = groups['locators']
                local = groups['local']
                state = groups['state']
                priority = int(groups['priority'])
                weight = int(groups['weight'])
                scope = groups['scope']
                rdp = groups['rdp']
                locators_dict = etr_dict.setdefault('locators',{})\
                                        .setdefault(locators,{})
                locators_dict.update({'local':local,
                                      'state':state,
                                      'priority':priority,
                                      'weight':weight,
                                      'scope':scope,
                                      'rdp':rdp})
                continue

            # Merged locators
            #  Locator       Local  State      Pri/Wgt  Scope        Registering ETR          RDP
            #  100.99.99.99  yes    up          10/50   IPv4 none    100.99.99.99:30343       [-]
            #  A0:EE:EE::EE  yes    up          10/50   IPv6 none    A0:EE:EE::EE.30343       [-]
            m = p25.match(line)
            if m:
                groups = m.groupdict()
                merged_locators = groups['merged_locators']
                local = groups['local']
                state = groups['state']
                priority = int(groups['priority'])
                weight = int(groups['weight'])
                scope = groups['scope']
                rdp = groups['rdp']
                merged_dict = instance_dict.setdefault('merged_locators',{})\
                                        .setdefault(merged_locators,{})
                if groups['etrp']:
                    etrp = str(groups['etrp'])
                    if etrp.count(":") > 1:
                        (etr, port) = etrp.split(".")
                    else:
                        (etr, port) = etrp.split(":")
                    port_val = int(port)
                    merged_dict.update({'port':port_val})
                elif groups['etr']:
                    etr = groups['etr']
                merged_dict.update({'local':local,
                                    'state':state,
                                    'priority':priority,
                                    'weight':weight,
                                    'scope':scope,
                                    'reg_etr':etr,
                                    'rdp':rdp})
                continue

            # ETR 11.11.11.11:33079
            # ETR 11.11.11.11
            m = p26.match(line)
            if m:
                port = 0
                groups = m.groupdict()
                if groups['etrp']:
                    etrp = str(groups['etrp'])
                    (etr,port) = etrp.split(":")
                elif groups['etr']:
                    etr = groups['etr']
                etr_dict = instance_dict.setdefault('etr',{})\
                                        .setdefault(etr,{})
                if port != 0:
                   etr_dict.update({'port':int(port)})
                continue

            # ETR 100:99:99:99::
            # ETR 100:99:99:99::.34273
            m = p27.match(line)
            if m:
                port = 0
                groups = m.groupdict()
                if groups['etrp']:
                    etrp = str(groups['etrp'])
                    (etr,port) = etrp.split(".")
                elif groups['etr']:
                    etr = groups['etr']
                etr_dict = instance_dict.setdefault('etr',{})\
                                        .setdefault(etr,{})
                if port != 0:
                   etr_dict.update({'port':int(port)})
                continue

            # last registered 00:45:46, proxy-reply, map-notify
            m = p28.match(line)
            if m:
                groups = m.groupdict()
                last_registered = groups['last_registered']
                proxy_reply = groups['proxy_reply']
                map_notify = groups['map_notify']
                proxy_reply_bool = proxy_reply == "proxy-reply"
                map_notify_bool = bool(re.search("map-notify",map_notify))

                etr_dict.update({'last_registered':last_registered,
                                 'proxy_reply':proxy_reply_bool,
                                 'map_notify':map_notify_bool})
                continue

            # SGT: 10
            m = p29.match(line)
            if m:
                groups = m.groupdict()
                sgt = int(groups['sgt'])
                instance_dict.update({'sgt':sgt})
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
                                        Optional('metric'): Or(int, None)
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
        # LISP IPv4 Mapping Cache for LISP 0 EID-table vrf NEW_VN (IID 4099), 3 entries
        # LISP IPv6 Mapping Cache for EID-table vrf red (IID 4100), 3 entries
        p1 = re.compile(r'^LISP (IPv4|IPv6|MAC) Mapping Cache for(\s+LISP (?P<lisp_id>\d+))?\s+'
                        r'EID-table\s+(?P<eid_table>[a-zA-Z0-9\s_]+)(\s+)?'
                        r'\(IID\s+(?P<instance_id>\d+)\),\s+(?P<entries>\d+)\s+entries$')

        # 50.1.1.0/24, uptime: 2d09h, expires: 20:10:07, via map-reply, complete, local-to-site
        # aabb.cc00.ca00/48, uptime: 00:00:23, expires: 00:59:36, via map-reply, complete, local-to-site
        p2 = re.compile(r'^(?P<eid_prefix>[a-fA-F\d\:]+\/\d{1,3}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/'
                        r'\d{1,2}|[a-fA-F\d\.]+\/\d{1,3}),\s+uptime:\s(?P<uptime>\S+),\sexpires:\s'
                        r'(?P<expiry_time>\d{1,2}:\d{2}:\d{2}|never),\svia\s(?P<via>\S+)(,'
                        r'\s(?P<map_reply_state>(complete|unknown-eid-forward|forward-native'
                        r'|send-map-request|drop|incomplete)))?'
                        r'(,\s(?P<site>local-to-site|remote-to-site))?$')

        # SGT: 10, software only
        # SGT: 10
        p3 = re.compile(r'^(SGT: (?P<sgt>\d+))?(,\s)?(?P<map_cache_type>software only)?$')

        # action: send-map-request + Encapsulating to proxy ETR
        # Negative cache entry, action: send-map-request
        p4 = re.compile(r'^(?P<negative_cache_entry>Negative cache entry,\s)?'
                        r'action:\s(?P<action>(send-map-request\s\+\s'
                        r'Encapsulating to proxy ETR)|send-map-request|forward-native)$')

        # 100.165.165.165  2d09h     up          10/10        4100
        # FE80::A8BB:CCFF:FE00:CA00  00:00:10  admin-down  255/0         -
        # 100.88.88.88  00:00:28  up         100/50        5000      -
        p5 = re.compile(r'^(?P<locators>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[a-fA-F\d\:]+)\s+'
                        r'(?P<uptime>\S+)\s+(?P<rloc_state>\S+)\s+(?P<priority>\d+)'
                        r'\/(?P<weight>\d+)\s+(?P<encap_iid>\d+|-)(\s+(?P<metric>\d+|-))?$')

        for line in output.splitlines():
            line = line.strip()

            # LISP IPv4 Mapping Cache for LISP 0 EID-table vrf red (IID 4100), 5 entries
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if group['lisp_id']:
                    lisp_id = int(group['lisp_id'])
                else:
                    lisp_id = 0
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
                    try:
                        # The value of metric can be an integer or '-'
                        metric = int(group['metric'])
                    except ValueError:
                        # Metric is unset. Output shows '-' when metric is unset
                        # Setting metric to None
                        metric = None
                    locators_dict.update({'metric': metric})
                continue
        return ret_dict


class ShowLispServerSubscriptionSchema(MetaParser):

    ''' Schema for
        show lisp instance-id {instance_id} ipv4 server subscription
        show lisp {lisp_id} instance-id {instance_id} ipv4 server subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server subscription
        show lisp eid-table {eid_table} ipv4 server subscription
        show lisp eid-table vrf {eid_table} ipv4 server subscription
        show lisp instance-id {instance_id} ipv6 server subscription
        show lisp {lisp_id} instance-id {instance_id} ipv6 server subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server subscription
        show lisp eid-table {eid_table} ipv6 server subscription
        show lisp eid-table vrf {eid_table} ipv6 server subscription
        show lisp instance-id {instance_id} ethernet server subscription
        show lisp {lisp_id} instance-id {instance_id} ethernet server subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ethernet server subscription
        show lisp eid-table vlan {eid_table} ethernet server subscription
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'entries': int,
                        Optional('eid_prefix'): {
                            str: { # EID prefix
                                'registration': str,
                                Optional('created'): str,
                                Optional('last_update'): str,
                                Optional('subscribers'): int
                                }
                            }
                        }
                    }
                }
            }
        }

class ShowLispServerSubscriptionSuperParser(ShowLispServerSubscriptionSchema):
    
    ''' parser for
        show lisp instance-id {instance_id} ipv4 server subscription
        show lisp {lisp_id} instance-id {instance_id} ipv4 server subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server subscription
        show lisp eid-table {eid_table} ipv4 server subscription
        show lisp eid-table vrf {eid_table} ipv4 server subscription
        show lisp instance-id {instance_id} ipv6 server subscription
        show lisp {lisp_id} instance-id {instance_id} ipv6 server subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server subscription
        show lisp eid-table {eid_table} ipv6 server subscription
        show lisp eid-table vrf {eid_table} ipv6 server subscription
        show lisp instance-id {instance_id} ethernet server subscription
        show lisp {lisp_id} instance-id {instance_id} ethernet server subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ethernet server subscription
        show lisp eid-table vlan {eid_table} ethernet server subscription
    '''
    
    def cli(self, lisp_id=None, instance_id=None, output=None):
        parsed_dict = {}

        if not lisp_id or isinstance(lisp_id, str):
            lisp_id = 0
        elif lisp_id.isdigit():
            lisp_id = int(lisp_id)

        # LISP EID Subscriptions for LISP 0 IID 4100, 2 entries 
        p1 = re.compile(r"^LISP\s+MS\s+EID\s+Subscriptions\s+for\s+LISP\s+"
                        r"(?P<lisp_id>\d+)?\s+"
                        r"IID\s+(?P<instance_id>\d+),\s+(?P<entries>\d+)\s+entries$")

        #Prefix                                  Source                         Created     Last Update   Subscribers
        #2.2.2.0/24                              2.2.2.0/24                     21:01:12    never           2      
        #172.168.0.0/16                          172.168.0.0/16                 20:53:14    never           1
        p2 = re.compile(r"^(?P<eid_prefix>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
                        r"\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3}|"
                        r"([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{2})\s+"
                        r"(?P<registration>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
                        r"\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3}|Unattached|"
                        r"([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{2})\s+"
                        r"(?P<created>\S+)\s+(?P<last_update>\S+)\s+(?P<subscribers>\d+)$")

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
                instance_id_dict.update({'entries': int(group['entries'])})
                continue
            
            m = p2.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict = instance_id_dict.setdefault('eid_prefix',{})\
                                                    .setdefault(str(group['eid_prefix']), {})
                eid_prefix_dict.update({'registration': group['registration'].strip()})
                eid_prefix_dict.update({'created': group['created'].strip()})
                eid_prefix_dict.update({'last_update': group['last_update'].strip()})
                subscriber = int(group['subscribers'])
                eid_prefix_dict.update({'subscribers': subscriber})
                continue

        return parsed_dict


class ShowLispServerSubscriptionPrefixSchema(MetaParser):

    ''' Schema for
        show lisp instance-id {instance_id} ipv4 server subscription {eid_prefix}/detail
        show lisp {lisp_id} instance-id {instance_id} ipv4 server subscription {eid_prefix}/detail
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server subscription {eid_prefix}/detail
        show lisp eid-table {eid_table} ipv4 server subscription {eid_prefix}/detail
        show lisp eid-table vrf {eid_table} ipv4 server subscription {eid_prefix}/detail
        show lisp instance-id {instance_id} ipv6 server subscription {eid_prefix}/detail
        show lisp {lisp_id} instance-id {instance_id} ipv6 server subscription {eid_prefix}/detail
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server subscription {eid_prefix}/detail
        show lisp eid-table {eid_table} ipv6 server subscription {eid_prefix}/detail
        show lisp eid-table vrf {eid_table} ipv6 server subscription {eid_prefix}/detail
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'entries': int,
                        Optional('eid_prefix'): {
                            str: { # EID prefix
                                Optional('first_subscribed'): str,
                                Optional('last_subscribed'): str,
                                Optional('registration'): str,
                                Optional('subscriber'): {
                                    str: { #map server eid
                                        Optional('locator'): str,
                                        Optional('port') : int,
                                        Optional('xtr_id') : str,
                                        Optional('subscriber_index'): int
                                        }   
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    
class ShowLispServerSubscriptionPrefixSuperParser(ShowLispServerSubscriptionPrefixSchema):
    
    ''' Parser for
        show lisp instance-id {instance_id} ipv4 server subscription {eid_prefix}/detail
        show lisp {lisp_id} instance-id {instance_id} ipv4 server subscription {eid_prefix}/detail
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server subscription {eid_prefix}/detail
        show lisp eid-table {eid_table} ipv4 server subscription {eid_prefix}/detail
        show lisp eid-table vrf {eid_table} ipv4 server subscription {eid_prefix}/detail
        show lisp instance-id {instance_id} ipv6 server subscription {eid_prefix}/detail
        show lisp {lisp_id} instance-id {instance_id} ipv6 server subscription {eid_prefix}/detail
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server subscription {eid_prefix}/detail
        show lisp eid-table {eid_table} ipv6 server subscription {eid_prefix}/detail
        show lisp eid-table vrf {eid_table} ipv6 server subscription {eid_prefix}/detail
    '''
    
    def cli(self, lisp_id=None, instance_id=None, output=None):
        parsed_dict = {}

        # LISP MS EID Subscriptions for LISP 0 IID 4100, 1 entries
        p1 = re.compile(r"^LISP\s+MS\s+EID\s+Subscriptions\s+for\s+LISP\s+"
                        r"(?P<lisp_id>\d+)?\s+"
                        r"IID\s+(?P<instance_id>\d+),\s+(?P<entries>\d+)\s+entries$")
        
        # Eid Prefix: 172.168.0.0/16
        p2 = re.compile(r"^Eid\s+Prefix:\s+(?P<eid_prefix>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
                        r"\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3}|"
                        r"([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{2})$")
        
        # First Subscribed: 00:00:55
        p3 = re.compile(r"^First\s+Subscribed:\s+(?P<first_subscribed>\S+)$")
        
        # Last Subscribed: 00:00:55
        p4 = re.compile(r"^Last\s+Subscribed:\s+(?P<last_subscribed>\S+)$")
        
        # Registration: 172.168.0.0/16
        p4_1 = re.compile(r"^Registration:\s+(?P<registration>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
                        r"\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3}|Unattached|"
                        r"([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{2})$")
        
        # Subscriber 100.11.11.11:45646
        p5 = re.compile(r'^Subscriber\s+(?P<subscriber>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))(:'
                         r'|\.)(?P<port>\d+)$')
        
        # xTR-ID 0xE9BF16D9-0x3D747C14-0x96C3FEB8-0x4AF6C2CB
        p6 = re.compile(r'^xTR-ID\s+(?P<xtr_id>\S+)$')
        
        # Subscriber Index: 5
        p7 = re.compile(r'^Subscriber\s+Index:\s+(?P<subscriber_index>\d+)$')
        
        for line in output.splitlines():
            line = line.strip()
            
            # LISP MS EID Subscriptions for LISP 0 IID 4100, 1 entries
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id_dict = \
                    parsed_dict.setdefault('lisp_id', {}) \
                        .setdefault(int(group['lisp_id']), {})
                instance_id_dict = \
                    lisp_id_dict.setdefault('instance_id', {}) \
                        .setdefault(int(group['instance_id']), {})
                instance_id_dict.update({'entries': int(group['entries'])})
                continue

            # Eid Prefix: 172.168.0.0/16
            m = p2.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict = instance_id_dict.setdefault('eid_prefix',{})\
                                                    .setdefault(str(group['eid_prefix']), {})
                continue

            # First Subscribed: 00:00:55
            m = p3.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict.update({'first_subscribed': group['first_subscribed'].strip()})
                continue
                
            # Last Subscribed: 00:00:55
            m = p4.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict.update({'last_subscribed': group['last_subscribed'].strip()})
                continue
              
            # Registration: 172.168.0.0/16
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict.update({'registration': group['registration'].strip()})
                continue
            
            
            # Subscriber 100.11.11.11:45646
            m = p5.match(line)
            if m:
                group = m.groupdict()
                subscribers_dict = eid_prefix_dict.setdefault('subscriber',{})\
                                                    .setdefault(str(group['subscriber']), {})
                subscribers_dict.update({'locator': group['subscriber'].strip()})
                subscribers_dict.update({'port': int(group['port'].strip())})
                continue
                
            # xTR-ID 0xE9BF16D9-0x3D747C14-0x96C3FEB8-0x4AF6C2CB
            m = p6.match(line)
            if m:
                group = m.groupdict()
                subscribers_dict.update({'xtr_id': group['xtr_id'].strip()})
                continue
                
            # Subscriber Index: 5
            m = p7.match(line)
            if m:
                group = m.groupdict()
                subscribers_dict.update({'subscriber_index': int(group['subscriber_index'].strip())})
                continue
            
        return parsed_dict


class ShowLispPublicationConfigPropSuperSchema(MetaParser):

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'eid_table': {
                            str: {
                                'eid_prefix': {
                                    str: {
                                        'eid': str,
                                        'mask': str,
                                        'last_published': str,
                                        'first_published': str,
                                        'exported_to': list,
                                        'publishers': {
                                            str: {
                                                'port': int,
                                                'last_published': str,
                                                'ttl': str,
                                                'expires': str,
                                                'epoch': {
                                                    'publisher': int,
                                                    'entry': int
                                                    },
                                                'entry_state': str,
                                                'xtr_id': str,
                                                'domain_id': str,
                                                'multihoming_id': str,
                                                Optional('extranet_iid'): str
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

class ShowLispPublicationConfigPropSuperParser(ShowLispPublicationConfigPropSuperSchema):

    """show lisp  instance-id {instance_id} ipv4 publication config-propagation {eid_prefix}"""

    def cli(self, instance_id, lisp_id=None, eid_prefix=None, output=None):

        ret_dict = {}

        # Publication Information for LISP 0 EID-table vrf internet (IID 5000)
        p1 = re.compile(r'^Publication\s+Information\s+for\s+LISP\s+(?P<lisp_id>\d+)'
                        r'\s+EID-table\s+(?P<eid_table>vrf\s+\S+)\s+'
                        r'\(IID\s+(?P<instance_id>\d+)\)$')

        # EID-prefix: 51.51.0.0/16
        p2 = re.compile(r'^EID-prefix:\s+(?P<eid>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|'
                        r'([a-fA-F\d\:]+))\/(?P<mask>\d{1,3})$')

        # First published:      10:24:38
        p3 = re.compile(r'^First\s+published:\s+(?P<first_published>never|\d{1,2}:\d{1,2}:\d{1,2})$')

        # Last published:       10:24:36
        p4 = re.compile(r'^Last\s+published:\s+(?P<last_published>never|\d{1,2}:\d{1,2}:\d{1,2})$')

        # Exported to:          local-eid
        p5 = re.compile(r'^Exported\s+to:\s+(?P<exported_to>[\s\S]+)$')

        # Publisher 100.77.77.77:4342, last published 00:03:39, TTL never, Expires: never
        # Publisher 100:77:77:77::.4342, last published 00:03:39, TTL never, Expires: never
        p6 = re.compile(r'^Publisher\s+(?P<publishers>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))(:'
                        r'|\.)(?P<port>\d+),\s+last\s+published\s+(?P<last_published>\d{1,2}:\d{1,2}:\d{1,2}),'
                        r'\s+TTL\s+(?P<ttl>\S+)\s+Expires:\s+'
                        r'(?P<expires>\S+)$')

        # publisher epoch 0, entry epoch 0
        p7 = re.compile(r"^publisher\s+epoch\s+(?P<publisher>\d+),"
                        r"\s+entry\s+epoch\s+(?P<entry>\d+)")

        # entry-state unknown
        p8 = re.compile(r'^entry-state\s+(?P<entry_state>\S+)$')

        # xTR-ID 0x790800FF-0x426D6D8E-0xC6C5F60C-0xB4386D22
        p9 = re.compile(r'^xTR-ID\s+(?P<xtr_id>\S+)$')

        # Domain-ID unset
        p10 = re.compile(r"^Domain-ID\s+(?P<domain_id>\S+)")

        # Multihoming-ID unspecified
        p11 = re.compile(r"^Multihoming-ID\s+(?P<multihoming_id>\S+)")

        # Extranet-IID 4101
        p12 = re.compile(r'^Extranet-IID\s+(?P<extranet_iid>\d+)$')

        # Publisher 100.77.77.77:4342
        # Publisher 100:77:77:77::.4342
        p13 = re.compile(r'^Publisher\s+(?P<publishers>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))(:'
                         r'|\.)(?P<port>\d+)$')

        # last published 00:03:39, TTL never, Expires: never
        p14 = re.compile(r'^last\s+published\s+(?P<last_published>\d{1,2}:\d{1,2}:\d{1,2}),'
                        r'\s+TTL\s+(?P<ttl>\S+)\s+Expires:\s+'
                        r'(?P<expires>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # Publication Information for LISP 0 EID-table vrf internet (IID 5000)
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                eid_table = groups['eid_table']
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})\
                                       .setdefault('instance_id',{})\
                                       .setdefault(instance_id,{})\
                                       .setdefault('eid_table',{})\
                                       .setdefault(eid_table,{})
                continue

            # EID-prefix: 51.51.0.0/16
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                eid = groups['eid']
                mask = groups['mask']
                eid_prefix = "{}/{}".format(eid,mask)
                eid_prefix_dict = lisp_id_dict.setdefault('eid_prefix',{})\
                                              .setdefault(eid_prefix,{})
                eid_prefix_dict.update({'eid':eid,
                                        'mask':mask})
                continue

            # First published:      10:24:38
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                first_published = groups['first_published']
                eid_prefix_dict.update({'first_published':first_published})
                continue

            # Last published:       10:24:36
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                last_published = groups['last_published']
                eid_prefix_dict.update({'last_published':last_published})
                continue

            # Exported to:          local-eid
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                exported_to = groups['exported_to']
                exported_list = eid_prefix_dict.setdefault('exported_to',[])
                exported_list.append(exported_to)
                eid_prefix_dict.update({'exported_to':exported_list})

            # Publisher 100.77.77.77:4342, last published 00:03:39, TTL never, Expires: never
            # Publisher 100:77:77:77::.4342, last published 00:03:39, TTL never, Expires: never
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                publishers = groups['publishers']
                port = int(groups['port'])
                last_published = groups['last_published']
                ttl = groups['ttl']
                expires = groups['expires']
                publisher_dict = eid_prefix_dict.setdefault('publishers',{}).\
                                                 setdefault(publishers,{})
                publisher_dict.update({'port':port,
                                       'last_published':last_published,
                                       'ttl':ttl,
                                       'expires':expires})
                continue

            # publisher epoch 0, entry epoch 0
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                publisher = int(groups['publisher'])
                entry = int(groups['entry'])
                epoch_dict = publisher_dict.setdefault('epoch',{})
                epoch_dict.update({'publisher':publisher,
                                   'entry':entry})
                continue

            # entry-state unknown
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                entry_state = groups['entry_state']
                publisher_dict.update({'entry_state':entry_state})
                continue

            # xTR-ID 0x790800FF-0x426D6D8E-0xC6C5F60C-0xB4386D22
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                xtr_id = groups['xtr_id']
                publisher_dict.update({'xtr_id':xtr_id})
                continue

            # Domain-ID unset
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                domain_id = groups['domain_id']
                publisher_dict.update({'domain_id':domain_id})
                continue

            # Multihoming-ID unspecified
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                multihoming_id = groups['multihoming_id']
                publisher_dict.update({'multihoming_id':multihoming_id})
                continue

            # Extranet-IID 4101
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                extranet_iid = groups['extranet_iid']
                publisher_dict.update({'extranet_iid':extranet_iid})
                continue

            # Publisher 100.77.77.77:4342
            # Publisher 100:77:77:77::.4342
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                publishers = groups['publishers']
                port = int(groups['port'])
                publisher_dict = eid_prefix_dict.setdefault('publishers',{}).\
                                                 setdefault(publishers,{})
                publisher_dict.update({'port':port})
                continue

            # last published 00:03:39, TTL never, Expires: never
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                publisher_dict.update({'last_published':groups['last_published'],
                                       'ttl':groups['ttl'],
                                       'expires':groups['expires']})
                continue

        return ret_dict


class ShowLispDatabaseConfigPropSuperSchema(MetaParser):

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
                        'do_not_register': int,
                        'eid_prefix': {
                            str: {
                                'eid': str,
                                'mask': str,
                                Optional('import_from'): str,
                                Optional('inherited_from'): str,
                                Optional('auto_disc_rloc'): bool,
                                Optional('proxy'): bool,
                                'up_time': str,
                                'last_change': str,
                                'service_insertion': str,
                                'extranet_iid': int,
                                'locators': {
                                    str: {
                                        'priority': int,
                                        'weight': int,
                                        'source': str,
                                        'state': str
                                        }
                                    },
                                Optional('map_servers'): {
                                    str: {
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
            }
        }


class ShowLispDatabaseConfigPropSuperParser(ShowLispDatabaseConfigPropSuperSchema):

    """
    Parser for
    * show lisp instance-id {instance_id} ipv4 database config-propagation
    * show lisp instance-id {instance_id} ipv6 database config-propagation
    """

    def cli(self, instance_id, lisp_id=None, eid_prefix=None, output=None):

        ret_dict = {}

        # LISP ETR IPv4 Mapping Database for LISP 0 EID-table vrf internet (IID 5000), LSBs: 0x3
        p1 = re.compile(r'^LISP\s+ETR\s+(IPv4|IPv6)\s+Mapping\s+Database\s+for\s+LISP\s+'
                        r'(?P<lisp_id>\d+)\s+EID-table\s+(?P<eid_table>vrf\s+\S+)\s+'
                        r'\(IID\s+(?P<instance_id>\d+)\),\s+LSBs:\s+(?P<lsb>\S+)$')

        # Entries total 7, no-route 0, inactive 0, do-not-register 0
        p2 = re.compile(r'^Entries\s+total\s+(?P<entries>\d+),\s+no-route\s+'
                        r'(?P<no_route>\d+),\s+inactive\s+(?P<inactive>\d+),\s+'
                        r'do-not-register\s+(?P<do_not_register>\d+)$')

        # 51.51.0.0/16, import from publication cfg prop, inherited from default locator-set RLOC, auto-discover-rlocs, proxy
        p3 = re.compile(r'^(?P<eid>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))'
                        r'\/(?P<mask>\d{1,3})(,\s+import\s+from\s+(?P<import_from>\S+'
                        r'|publication cfg prop))?(,\s+inherited\s+from\s+'
                        r'(?P<inherited_from>default locator-set RLOC|\S+))?'
                        r'(,\s+(?P<auto_disc_rloc>auto-discover-rlocs))?(,\s+(?P<proxy>proxy))?$')

        # Uptime: 01:30:26, Last-change: 01:30:26
        p4 = re.compile(r'^Uptime:\s+(?P<up_time>\d{1,2}:\d{1,2}:\d{1,2}),'
                        r'\s+Last-change:\s+(?P<last_change>\d{1,2}:\d{1,2}:\d{1,2})$')

        # Service-Insertion: N/A
        p5 = re.compile(r'^Service-Insertion:\s+(?P<service_insertion>\S+)$')

        # Extranet-IID: 5000  (Sourced by Config Propagation)
        p6 = re.compile(r'^Extranet-IID:\s+(?P<extranet_iid>\d+)')

        # 100.88.88.88   10/50   cfg-intf   site-self, reachable
        # 100:88:88:88:: 10/50   cfg-intf   site-self, reachable
        p7 = re.compile(r'^(?P<locators>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+'
                        r'(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<source>\S+)\s+'
                        r'(?P<state>site-self, reachable|site-other, report-reachable)$')

        # 100.77.77.77     04:29:46       Yes  4
        # 100:77:77:77::   04:29:46       Yes  4
        p8 = re.compile(r'^(?P<map_servers>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+'
                        r'(?P<uptime>\d{1,2}:\d{1,2}:\d{1,2})\s+(?P<ack>\S+)\s+'
                        r'(?P<domain_id>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # LISP ETR IPv4 Mapping Database for LISP 0 EID-table vrf internet (IID 5000), LSBs: 0x3
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                eid_table = groups['eid_table']
                lsb = groups['lsb']
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})\
                                       .setdefault('instance_id',{})\
                                       .setdefault(instance_id,{})
                lisp_id_dict.update({'eid_table':eid_table,
                                     'lsb':lsb})
                continue

            # Entries total 7, no-route 0, inactive 0, do-not-register 0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                entries = int(groups['entries'])
                no_route = int(groups['no_route'])
                inactive = int(groups['inactive'])
                do_not_register = int(groups['do_not_register'])
                lisp_id_dict.update({'entries':entries,
                                     'no_route':no_route,
                                     'inactive':inactive,
                                     'do_not_register':do_not_register})
                continue

            # 51.51.0.0/16, import from publication cfg prop, inherited from default locator-set RLOC, auto-discover-rlocs, proxy
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                eid = groups['eid']
                mask = groups['mask']
                eid_prefix = "{}/{}".format(eid,mask)
                eid_prefix_dict = lisp_id_dict.setdefault('eid_prefix',{}).\
                                               setdefault(eid_prefix,{})
                eid_prefix_dict.update({'eid':eid,
                                        'mask':mask})
                if groups['import_from']:
                    import_from = groups['import_from']
                    eid_prefix_dict.update({'import_from':import_from})
                if groups['inherited_from']:
                    inherited_from = groups['inherited_from']
                    eid_prefix_dict.update({'inherited_from':inherited_from})
                if groups['auto_disc_rloc']:
                    auto_disc_rloc = groups['auto_disc_rloc']
                    eid_prefix_dict.update({'auto_disc_rloc':True})
                if groups['proxy']:
                    proxy = groups['proxy']
                    eid_prefix_dict.update({'proxy':True})
                continue

            # Uptime: 01:30:26, Last-change: 01:30:26
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                up_time = groups['up_time']
                last_change = groups['last_change']
                eid_prefix_dict.update({'up_time':up_time,
                                        'last_change':last_change})
                continue

            # Service-Insertion: N/A
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                service_insertion = groups['service_insertion']
                eid_prefix_dict.update({'service_insertion':service_insertion})
                continue

            # Extranet-IID: 5000  (Sourced by Config Propagation)
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                extranet_iid = int(groups['extranet_iid'])
                eid_prefix_dict.update({'extranet_iid':extranet_iid})
                continue

            # 100.88.88.88   10/50   cfg-intf   site-self, reachable
            # 100:88:88:88:: 10/50   cfg-intf   site-self, reachable
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                locators = groups['locators']
                priority = int(groups['priority'])
                weight = int(groups['weight'])
                source = groups['source']
                state = groups['state']
                locators_dict = eid_prefix_dict.setdefault('locators',{}).\
                                                setdefault(locators,{})
                locators_dict.update({'priority':priority,
                                      'weight':weight,
                                      'source':source,
                                      'state':state})
                continue

            # 100.77.77.77     04:29:46       Yes  4
            # 100:77:77:77::   04:29:46       Yes  4
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                map_servers = groups['map_servers']
                uptime = groups['uptime']
                ack = groups['ack']
                domain_id = groups['domain_id']
                map_dict = eid_prefix_dict.setdefault('map_servers',{}).\
                                           setdefault(map_servers,{})
                map_dict.update({'uptime':uptime,
                                 'ack':ack,
                                 'domain_id':domain_id})
                continue
        return ret_dict


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
                                Optional('rloc'): str,
                                'encap_iid': str
                            }
                        }
                    }
                }
            }
        }
    }


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


class ShowLispIpv4PublisherRlocSchema(MetaParser):

    ''' Schema for
     * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher {publisher_id}
     * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 publisher {publisher_id}
     * show lisp instance-id {instance_id} ipv4 publisher {publisher_id}
     * show lisp eid-table {eid_table} ipv4 publisher {publisher_id}
     * show lisp eid-table vrf {vrf} ipv4 publisher {publisher_id}
     * show lisp eid-table vrf ipv4 publisher {publisher_id}
     * show lisp {lisp_id} instance-id {instance_id} ipv6 publisher {publisher_id}
     * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 publisher {publisher_id}
     * show lisp instance-id {instance_id} ipv6 publisher {publisher_id}
     * show lisp eid-table {eid_table} ipv6 publisher {publisher_id}
     * show lisp eid-table vrf {vrf} ipv6 publisher {publisher_id}
     * show lisp eid-table vrf ipv6 publisher {publisher_id}
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
                                Optional("rloc_set"): {
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


class ShowLispIpv4v6PublisherRloc(ShowLispIpv4PublisherRlocSchema):

    ''' Parser for
     * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher {publisher_id}
     * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 publisher {publisher_id}
     * show lisp instance-id {instance_id} ipv4 publisher {publisher_id}
     * show lisp eid-table {eid_table} ipv4 publisher {publisher_id}
     * show lisp eid-table vrf {vrf} ipv4 publisher {publisher_id}
     * show lisp eid-table vrf ipv4 publisher {publisher_id}
     * show lisp {lisp_id} instance-id {instance_id} ipv6 publisher {publisher_id}
     * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 publisher {publisher_id}
     * show lisp instance-id {instance_id} ipv6 publisher {publisher_id}
     * show lisp eid-table {eid_table} ipv6 publisher {publisher_id}
     * show lisp eid-table vrf {vrf} ipv6 publisher {publisher_id}
     * show lisp eid-table vrf ipv6 publisher {publisher_id}
    '''

    def cli(self, output=None, lisp_id=None, instance_id=None, publisher_id=None, locator_table=None,
            eid_table=None, vrf=None):

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
                        r'\sfor(\s+LISP\s+\d+)?\sEID-table\svrf\s(?P<eid_table>\S+).+$')

        # Publisher state: Established, Publisher epoch 0, Entries total 2
        p3 = re.compile(r'^Publisher\sstate:\s+(?P<state>\S+),\sPublisher\sepoch\s'\
                        r'(?P<epoch>\d+),\sEntries\stotal\s(?P<entries>\d+)$')

        # 0.0.0.0/0, Epoch: 0, Last Published: 5d22h
        # 2001:172:168:1::/64, Epoch: 0, Last Published: 00:00:43
        p4 = re.compile(r'^(?P<eid_prefix>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3})'\
                        r',\sEpoch:\s(?P<eid_epoch>\d+),\sLast Published:\s+(?P<last_pub_time>.+)$')

        # TTL: never, State unknown-eid-forward
        p5 = re.compile(r'^TTL:\s(?P<ttl>\S+),\sState\s(?P<eid_state>\S+)$')

        # 203.203.203.203  255/10   up        -
        # 2001:2:2:2::2   50/50   up        -
        p6 = re.compile(r'(?P<rloc_set>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
                        r'|[a-fA-F\d\:]+)\s+(?P<priority>\d+)\/(?P<weight>\d+)\s+'
                        r'(?P<rloc_state>\S+)\s+(?P<encap_iid>\S+)$')


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