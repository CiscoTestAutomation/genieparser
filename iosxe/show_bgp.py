''' show_bgp.py
    IOSXE parsers for the following show commands:

    * show bgp all detail
    * show bgp all neighbor
    * show bgp all summary
    * show bgp all cluster-ids
    * show bgp all
    * show ip bgp template peer-session <WORD>
    * show ip bgp template peer-policy <WORD>
    * show ip bgp all dampening parameters
    * show ip bgp <af_name> [ vrf <vrf_id> ] <ipv4prefix>
    * show bgp vrf [vrf_id] <af_name> <ipv6prefix>
    * show bgp <af_name> <ipv6prefix>
    * show bgp all neighbors <neighbor> policy
    * show ip route vrf <WORD> bgp
    * show vrf detail

    * show bgp all neighbor x.x.x.x advertised-routes
    * show bgp all neighbor x.x.x.x routes
    * show bgp all neighbor x.x.x.x received
    * show bgp all neighbor x.x.x.x received-routes

'''

import re   
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional


class ShowBgpAllSummarySchema(MetaParser):
    """
    Schema for:
            * show bgp all summary
    """
    schema = {
        'vrf':
            {Any():
                 {Optional('neighbor'):
                      {Any():
                           {'address_family':
                                {Any():
                                     {'version': int,
                                      'as': int,
                                      'msg_rcvd': int,
                                      'msg_sent': int,
                                      'tbl_ver': int,
                                      'input_queue': int,
                                      'output_queue': int,
                                      'up_down': str,
                                      'state_pfxrcd': str,
                                      Optional('route_identifier'): str,
                                      Optional('local_as'): int,
                                      Optional('bgp_table_version'): int,
                                      Optional('routing_table_version'): int,
                                      Optional('prefixes'):
                                          {'total_entries': int,
                                           'memory_usage': int,
                                           },
                                      Optional('path'):
                                          {'total_entries': int,
                                           'memory_usage': int,
                                           },
                                      Optional('cache_entries'):
                                          {Any():
                                               {
                                                'total_entries': int,
                                                'memory_usage': int,
                                               },
                                          },
                                      Optional('entries'):
                                          {Any():
                                              {
                                                  'total_entries': int,
                                                  'memory_usage': int,
                                              },
                                          },
                                      Optional('community_entries'):
                                          {'total_entries': int,
                                           'memory_usage': int,
                                           },
                                      Optional('attribute_entries'): str,
                                      Optional('total_memory'): int,
                                      Optional('activity_prefixes'): str,
                                      Optional('activity_paths'): str,
                                      Optional('scan_interval'): int,
                                      },
                                 },
                            },
                       },
                  },
             },
        }


class ShowBgpAllSummary(ShowBgpAllSummarySchema):
    """
    Parser for:
          *  show bgp All Summary
    """

    def cli(self):
        cmd = 'show bgp all summary'
        out = self.device.execute(cmd)

        # Init vars
        sum_dict = {}
        cache_dict = {}
        entries_dict = {}

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # For address family: IPv4 Unicast
            p1 = re.compile(r'^\s*For address family: +(?P<address_family>[a-zA-Z0-9\s\-\_]+)$')
            m = p1.match(line)
            if m:
                # Save variables for use later
                address_family = str(m.groupdict()['address_family']).lower()
                vrf = 'default'
                attribute_entries = ""
                num_prefix_entries = ""
                path_total_entries = ""
                total_memory = ""
                activity_paths = ""
                activity_prefixes = ""
                scan_interval = ""
                cache_dict = {}
                entries_dict = {}
                num_community_entries = ""
                continue

            # BGP router identifier 200.0.1.1, local AS number 100
            p2 = re.compile(r'^\s*BGP +router +identifier'
                            ' +(?P<route_identifier>[0-9\.\:]+), +local +AS'
                            ' +number +(?P<local_as>[0-9]+)$')
            m = p2.match(line)
            if m:
                route_identifier = str(m.groupdict()['route_identifier'])
                local_as = int(m.groupdict()['local_as'])
                if 'vrf' not in sum_dict:
                    sum_dict['vrf'] = {}
                if vrf not in sum_dict['vrf']:
                    sum_dict['vrf'][vrf] = {}
                continue

            # BGP table version is 28, main routing table version 28
            p3 = re.compile(r'^\s*BGP +table +version +is'
                            ' +(?P<bgp_table_version>[0-9]+),'
                            ' +main +routing +table +version'
                            ' +(?P<routing_table_version>[0-9]+)$')
            m = p3.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                routing_table_version = int(m.groupdict()['routing_table_version'])
                continue

            # 27 network entries using 6696 bytes of memory
            p4 = re.compile(r'^\s*(?P<networks>[0-9]+) +network +entries +using'
                            ' +(?P<bytes>[0-9]+) +bytes +of +memory$')

            m = p4.match(line)
            if m:
                num_prefix_entries = int(m.groupdict()['networks'])
                num_memory_usage = int(m.groupdict()['bytes'])
                continue

            # 27 path entries using 3672 bytes of memory
            p5 = re.compile(r'^\s*(?P<path>[0-9]+) +path +entries +using'
                            ' +(?P<memory_usage>[0-9]+) +bytes +of +memory$')
            m = p5.match(line)
            if m:
                path_total_entries = int(m.groupdict()['path'])
                path_memory_usage = int(m.groupdict()['memory_usage'])
                continue

            # 2 BGP rrinfo entries using 48 bytes of memory
            p5_1 = re.compile(r'^\s*(?P<num_entries>([0-9]+)) +BGP +(?P<entries_type>(\S+)) +entries +using'
                              ' +(?P<entries_byte>[0-9]+) +bytes +of +memory$')
            m = p5_1.match(line)
            if m:
                num_entries = int(m.groupdict()['num_entries'])
                entries_type = str(m.groupdict()['entries_type'])
                entries_byte = int(m.groupdict()['entries_byte'])

                entries_dict[entries_type] = {}
                entries_dict[entries_type]['total_entries'] = num_entries
                entries_dict[entries_type]['memory_usage'] = entries_byte
                continue

            # 4 BGP extended community entries using 96 bytes of memory
            p5_2 = re.compile(r'^\s*(?P<num_community_entries>[0-9]+) +BGP +extended +community +entries +using'
                            ' +(?P<memory_usage>[0-9]+) +bytes +of +memory$')
            m = p5_2.match(line)
            if m:
                num_community_entries = int(m.groupdict()['num_community_entries'])
                community_memory_usage = int(m.groupdict()['memory_usage'])
                continue

            # 1/1 BGP path/bestpath attribute entries using 280 bytes of memory
            p6 = re.compile(r'^\s*(?P<attribute_entries>(\S+)) +BGP +(?P<attribute_type>(\S+))'
                            ' +attribute +entries +using +(?P<bytes>[0-9]+) +bytes +of +memory$')
            m = p6.match(line)
            if m:
                attribute_entries = str(m.groupdict()['attribute_entries'])
                attribute_type = str(m.groupdict()['attribute_type'])
                attribute_memory_usage = int(m.groupdict()['bytes'])
                continue

            # 0 BGP route-map cache entries using 0 bytes of memory
            p6_1 = re.compile(r'^\s*(?P<num_cache_entries>([0-9]+)) +BGP +(?P<cache_type>(\S+)) +cache +entries +using'
                            ' +(?P<cache_byte>[0-9]+) +bytes +of +memory$')
            m = p6_1.match(line)
            if m:
                num_cache_entries = int(m.groupdict()['num_cache_entries'])
                cache_type = str(m.groupdict()['cache_type'])
                cache_byte = int(m.groupdict()['cache_byte'])

                cache_dict[cache_type] = {}
                cache_dict[cache_type]['total_entries'] = num_cache_entries
                cache_dict[cache_type]['memory_usage'] = cache_byte
                continue

            # BGP using 10648 total bytes of memory
            p7 = re.compile(r'^\s*BGP +using'
                            ' +(?P<total_memory>[0-9]+) +total +bytes +of +memory$')
            m = p7.match(line)
            if m:
                total_memory = int(m.groupdict()['total_memory'])
                continue

            # BGP activity 47/20 prefixes, 66/39 paths, scan interval 60 secs
            p8 = re.compile(r'^\s*BGP +activity'
                            ' +(?P<activity_prefixes>(\S+)) +prefixes, +(?P<activity_paths>(\S+))'
                            ' +paths, +scan +interval +(?P<scan_interval>[0-9]+) +secs$')
            m = p8.match(line)
            if m:
                activity_prefixes = str(m.groupdict()['activity_prefixes'])
                activity_paths = str(m.groupdict()['activity_paths'])
                scan_interval = str(m.groupdict()['scan_interval'])
                continue


            # Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            # 200.0.1.1       4          100       0       0        1    0    0 01:07:38 Idle
            # 200.0.2.1       4          100       0       0        1    0    0 never    Idle
            # 200.0.4.1       4          100       0       0        1    0    0 01:07:38 Idle

            p9 = re.compile(r'^\s*(?P<neighbor>[a-zA-Z0-9\.\:]+) +(?P<version>[0-9]+)'
                            ' +(?P<as>[0-9]+) +(?P<msg_rcvd>[0-9]+)'
                            ' +(?P<msg_sent>[0-9]+) +(?P<tbl_ver>[0-9]+)'
                            ' +(?P<inq>[0-9]+) +(?P<outq>[0-9]+)'
                            ' +(?P<up_down>[a-zA-Z0-9\:]+)'
                            ' +(?P<state>[a-zA-Z0-9\(\)\s]+)$')
            m = p9.match(line)
            if m:
                # Add neighbor to dictionary
                neighbor = str(m.groupdict()['neighbor'])
                if 'neighbor' not in sum_dict['vrf'][vrf]:
                    sum_dict['vrf'][vrf]['neighbor'] = {}
                if neighbor not in sum_dict['vrf'][vrf]['neighbor']:
                    sum_dict['vrf'][vrf]['neighbor'][neighbor] = {}
                nbr_dict = sum_dict['vrf'][vrf]['neighbor'][neighbor]

                # Add address family to this neighbor
                if 'address_family' not in nbr_dict:
                    nbr_dict['address_family'] = {}
                if address_family not in nbr_dict['address_family']:
                    nbr_dict['address_family'][address_family] = {}
                nbr_af_dict = nbr_dict['address_family'][address_family]

                # Add keys for this address_family
                nbr_af_dict['version'] = int(m.groupdict()['version'])
                nbr_af_dict['as'] = int(m.groupdict()['as'])
                nbr_af_dict['msg_rcvd'] = int(m.groupdict()['msg_rcvd'])
                nbr_af_dict['msg_sent'] = int(m.groupdict()['msg_sent'])
                nbr_af_dict['tbl_ver'] = int(m.groupdict()['tbl_ver'])
                nbr_af_dict['input_queue'] = int(m.groupdict()['inq'])
                nbr_af_dict['output_queue'] = int(m.groupdict()['outq'])
                nbr_af_dict['up_down'] = str(m.groupdict()['up_down'])
                nbr_af_dict['state_pfxrcd'] = str(m.groupdict()['state'])
                nbr_af_dict['route_identifier'] = route_identifier
                nbr_af_dict['local_as'] = local_as
                nbr_af_dict['bgp_table_version'] = bgp_table_version
                nbr_af_dict['routing_table_version'] = routing_table_version

                try:
                # Assign variables
                    if attribute_entries:
                        nbr_af_dict['attribute_entries'] = attribute_entries
                    if num_prefix_entries:
                        nbr_af_dict['prefixes'] = {}
                        nbr_af_dict['prefixes']['total_entries'] = num_prefix_entries
                        nbr_af_dict['prefixes']['memory_usage'] = num_memory_usage

                    if path_total_entries:
                        nbr_af_dict['path'] = {}
                        nbr_af_dict['path']['total_entries'] = path_total_entries
                        nbr_af_dict['path']['memory_usage'] = path_memory_usage

                    if total_memory:
                        nbr_af_dict['total_memory'] = total_memory

                    if activity_prefixes:
                        nbr_af_dict['activity_prefixes'] = activity_prefixes

                    if activity_paths:
                        nbr_af_dict['activity_paths'] = activity_paths

                    if scan_interval:
                        nbr_af_dict['scan_interval'] = int(scan_interval)

                    if len(cache_dict):
                        nbr_af_dict['cache_entries'] = cache_dict

                    if len(entries_dict):
                        nbr_af_dict['entries'] = entries_dict

                    if num_community_entries:
                        nbr_af_dict['community_entries'] = {}
                        nbr_af_dict['community_entries']['total_entries'] = num_community_entries
                        nbr_af_dict['community_entries']['memory_usage'] = community_memory_usage
                except:
                    pass
            else:
                # when neighbor info break down to 2 lines.
                #  Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
                #  2001:DB8:20:4:6::6
                #           4          400      67      73       66    0    0 01:03:11        5

                p10 = re.compile(r'^\s*(?P<neighbor>[a-zA-Z0-9\.\:]+)$')
                m = p10.match(line)
                if m :
                    # Add neighbor to dictionary
                    neighbor = str(m.groupdict()['neighbor'])
                    if 'neighbor' not in sum_dict['vrf'][vrf]:
                        sum_dict['vrf'][vrf]['neighbor'] = {}
                    if neighbor not in sum_dict['vrf'][vrf]['neighbor']:
                        sum_dict['vrf'][vrf]['neighbor'][neighbor] = {}
                    nbr_dict = sum_dict['vrf'][vrf]['neighbor'][neighbor]

                    # Add address family to this neighbor
                    if 'address_family' not in nbr_dict:
                        nbr_dict['address_family'] = {}
                    if address_family not in nbr_dict['address_family']:
                        nbr_dict['address_family'][address_family] = {}
                    nbr_af_dict = nbr_dict['address_family'][address_family]

                p11 = re.compile(r'^\s*(?P<version>[0-9]+)'
                                    ' +(?P<as>[0-9]+) +(?P<msg_rcvd>[0-9]+)'
                                    ' +(?P<msg_sent>[0-9]+) +(?P<tbl_ver>[0-9]+)'
                                    ' +(?P<inq>[0-9]+) +(?P<outq>[0-9]+)'
                                    ' +(?P<up_down>[a-zA-Z0-9\:]+)'
                                    ' +(?P<state>[a-zA-Z0-9\(\)\s]+)$')
                m = p11.match(line)
                if m:
                    # Add keys for this address_family
                    nbr_af_dict['version'] = int(m.groupdict()['version'])
                    nbr_af_dict['as'] = int(m.groupdict()['as'])
                    nbr_af_dict['msg_rcvd'] = int(m.groupdict()['msg_rcvd'])
                    nbr_af_dict['msg_sent'] = int(m.groupdict()['msg_sent'])
                    nbr_af_dict['tbl_ver'] = int(m.groupdict()['tbl_ver'])
                    nbr_af_dict['input_queue'] = int(m.groupdict()['inq'])
                    nbr_af_dict['output_queue'] = int(m.groupdict()['outq'])
                    nbr_af_dict['up_down'] = str(m.groupdict()['up_down'])
                    nbr_af_dict['state_pfxrcd'] = str(m.groupdict()['state'])
                    nbr_af_dict['route_identifier'] = route_identifier
                    nbr_af_dict['local_as'] = local_as
                    nbr_af_dict['bgp_table_version'] = bgp_table_version
                    nbr_af_dict['routing_table_version'] = routing_table_version

                    try:
                        # Assign variables
                        if attribute_entries:
                            nbr_af_dict['attribute_entries'] = attribute_entries
                        if num_prefix_entries:
                            nbr_af_dict['prefixes'] = {}
                            nbr_af_dict['prefixes']['total_entries'] = num_prefix_entries
                            nbr_af_dict['prefixes']['memory_usage'] = num_memory_usage

                        if path_total_entries:
                            nbr_af_dict['path'] = {}
                            nbr_af_dict['path']['total_entries'] = path_total_entries
                            nbr_af_dict['path']['memory_usage'] = path_memory_usage

                        if total_memory:
                            nbr_af_dict['total_memory'] = total_memory

                        if activity_prefixes:
                            nbr_af_dict['activity_prefixes'] = activity_prefixes

                        if activity_paths:
                            nbr_af_dict['activity_paths'] = activity_paths

                        if scan_interval:
                            nbr_af_dict['scan_interval'] = int(scan_interval)

                        if len(cache_dict):
                            nbr_af_dict['cache_entries'] = cache_dict

                        if len(entries_dict):
                            nbr_af_dict['entries'] = entries_dict

                        if num_community_entries:
                            nbr_af_dict['community_entries'] = {}
                            nbr_af_dict['community_entries']['total_entries'] = num_community_entries
                            nbr_af_dict['community_entries']['memory_usage'] = community_memory_usage
                    except:
                        pass

                continue

        return sum_dict


class ShowBgpAllClusterIdsSchema(MetaParser):
    '''
        Schema for show bgp all cluster-ids
    '''
    schema = {
              'vrf':
                    {Any():
                        {
                           Optional('cluster_id'): str,
                           Optional('configured_id'): str,
                           Optional('reflection_all_configured'): str,
                           Optional('reflection_intra_cluster_configured'): str,
                           Optional('reflection_intra_cluster_used'): str,
                           Optional('list_of_cluster_ids'):
                               {Any():
                                    {
                                        Optional('num_neighbors'): int,
                                        Optional('client_to_client_reflection_configured'): str,
                                        Optional('client_to_client_reflection_used'): str,

                                    }

                               }
                        }
                    },

                }

class ShowBgpAllClusterIds(ShowBgpAllClusterIdsSchema):
    '''
       Parser for show bgp all cluster-ids
       Executing 'show vrf detail | inc \(VRF' to collect vrf names.

    '''

    def cli(self):
        # find vrf names
        # show vrf detail | inc \(VRF
        cmd_vrfs = 'show vrf detail | inc \(VRF'
        out_vrf = self.device.execute(cmd_vrfs)
        vrf_dict = {'0':'default'}

        for line in out_vrf.splitlines():
            if not line:
                continue
            else:
                line = line.rstrip()

            # VRF VRF1 (VRF Id = 1); default RD 300:1; default VPNID <not set>
            p = re.compile(r'^\s*VRF +(?P<vrf_name>[0-9a-zA-Z]+)'
                            ' +\(+VRF +Id += +(?P<vrf_id>[0-9]+)+\)+;'
                            ' +default +(?P<other_data>.+)$')
            m = p.match(line)
            if m:
                # Save variables for use later
                vrf_name = str(m.groupdict()['vrf_name'])
                vrf_id = str(m.groupdict()['vrf_id'])
                vrf_dict[vrf_id] = vrf_name.lower()
                continue


        # show bgp all cluster-ids
        cmd = 'show bgp all cluster-ids'
        out = self.device.execute(cmd)

        # Init vars
        sum_dict = {}
        cluster_id = None
        list_of_cluster_ids = dict()
        configured_id = ""
        reflection_all_configured = ""
        reflection_intra_cluster_configured = ""
        reflection_intra_cluster_used = ""


        for line in out.splitlines():
            if line.strip():
                line = line.rstrip()
            else:
                continue

            # Global cluster-id: 4.4.4.4 (configured: 0.0.0.0)
            p1 = re.compile(r'^\s*Global +cluster-id: +(?P<cluster_id>[0-9\.]+)'
                            ' +\(+configured: +(?P<configured>[0-9\.]+)+\)$')
            m = p1.match(line)
            if m:
                # Save variables for use later
                cluster_id = str(m.groupdict()['cluster_id'])
                configured_id = str(m.groupdict()['configured'])

                if 'vrf' not in sum_dict:
                    sum_dict['vrf'] = {}

                continue

            #   all (inter-cluster and intra-cluster): ENABLED
            p3 = re.compile(r'^\s*all +\(+inter-cluster +and +intra-cluster+\):'
                            ' +(?P<all_configured>[a-zA-Z]+)$')
            m = p3.match(line)
            if m:
                reflection_all_configured = m.groupdict()['all_configured'].lower()
                continue

            # intra-cluster:                         ENABLED       ENABLED
            p4 = re.compile(r'^\s*intra-cluster:\s+(?P<intra_cluster_configured>[a-zA-Z]+)'
                            ' +(?P<intra_cluster_used>[a-zA-Z]+)$')
            m = p4.match(line)
            if m:
                reflection_intra_cluster_configured = m.groupdict()['intra_cluster_configured'].lower()
                reflection_intra_cluster_used = m.groupdict()['intra_cluster_used'].lower()
                continue

            # List of cluster-ids
            # Cluster-id  #-neighbors C2C-rfl-CFG C2C-rfl-USE
            # 192.168.1.1                2 DISABLED    DISABLED
            p5 = re.compile(r'^\s*(?P<cluster_ids>[0-9\.]+)'
                        ' +(?P<num_neighbors>[0-9]+)'
                        ' +(?P<client_to_client_ref_configured>[a-zA-Z]+)'
                        ' +(?P<client_to_client_ref_used>[a-zA-Z]+)$')
            m = p5.match(line)
            if m:
                cluster_ids = m.groupdict()['cluster_ids']
                list_of_cluster_ids[cluster_ids] = cluster_ids
                list_of_cluster_ids[cluster_ids] = {}
                list_of_cluster_ids[cluster_ids]['num_neighbors'] = int(m.groupdict()['num_neighbors'])
                list_of_cluster_ids[cluster_ids]['client_to_client_reflection_configured'] = \
                    m.groupdict()['client_to_client_ref_configured'].lower()
                list_of_cluster_ids[cluster_ids]['client_to_client_reflection_used'] = \
                    m.groupdict()['client_to_client_ref_used'].lower()

                continue

        for vrf_id, vrf_name in vrf_dict.items():
            if 'vrf' not in sum_dict:
                sum_dict['vrf'] = {}
            if vrf_name not in sum_dict['vrf']:
                sum_dict['vrf'][vrf_name] = {}
            if 'cluster_id' not in sum_dict['vrf'][vrf_name]:
                if not cluster_id:
                    del sum_dict['vrf']
                if cluster_id:
                    sum_dict['vrf'][vrf_name]['cluster_id'] = cluster_id
                if configured_id:
                    sum_dict['vrf'][vrf_name]['configured_id'] = configured_id
                if reflection_all_configured:
                    sum_dict['vrf'][vrf_name]['reflection_all_configured'] = \
                        reflection_all_configured
                if reflection_intra_cluster_configured:
                    sum_dict['vrf'][vrf_name]['reflection_intra_cluster_configured'] = \
                        reflection_intra_cluster_configured
                if reflection_intra_cluster_used:
                    sum_dict['vrf'][vrf_name]['reflection_intra_cluster_used'] = \
                        reflection_intra_cluster_used
                if list_of_cluster_ids:
                    sum_dict['vrf'][vrf_name]['list_of_cluster_ids'] = list_of_cluster_ids
        return sum_dict


class ShowIpbgpTemplatePeerPolicySchema(MetaParser):
    '''
           Schema show ip bgp template peer-policy
    '''
    schema = {
                'peer_policy':
                    {Any():
                         {
                             Optional('local_policies'): str,
                             Optional('inherited_polices'): str,
                             Optional('local_disable_policies'): str,
                             Optional('inherited_disable_polices'): str,
                             Optional('allowas_in'): bool ,
                             Optional('allowas_in_as_number'): int,
                             Optional('as_override'): bool,
                             Optional('default_originate'): bool,
                             Optional('default_originate_route_map'): str,
                             Optional('route_map_name_in'): str,
                             Optional('route_map_name_out'): str,
                             Optional('maximum_prefix_max_prefix_no'): int,
                             Optional('maximum_prefix_threshold'): int,
                             Optional('maximum_prefix_restart'): int,
                             Optional('maximum_prefix_warning_only'): bool,
                             Optional('next_hop_self'): bool,
                             Optional('route_reflector_client'): bool,
                             Optional('send_community'): str,
                             Optional('soft_reconfiguration'): bool,
                             Optional('soo'): str,
                             Optional('index'): int,
                         },
                    },
                }

class ShowIpBgpTemplatePeerPolicy(ShowIpbgpTemplatePeerPolicySchema):
    '''
        Parser for show ip bgp template peer-policy
    '''

    def cli(self):
        # show ip bgp template peer-policy
        cmd = 'show ip bgp template peer-policy'
        out = self.device.execute(cmd)

        # Init vars
        parsed_dict = {}

        for line in out.splitlines():
            if line.strip():
                line = line.rstrip()
            else:
                continue

            # Template:PEER-POLICY, index:1.
            p1 = re.compile(r'^\s*Template:+(?P<template_id>[0-9\s\S\w]+),'
                            ' +index:(?P<index>[0-9]+).$')
            m = p1.match(line)
            if m:
                template_id = m.groupdict()['template_id'].lower()
                index = int(m.groupdict()['index'])

                if 'peer_policy' not in parsed_dict:
                    parsed_dict['peer_policy'] = {}

                if template_id not in parsed_dict['peer_policy']:
                    parsed_dict['peer_policy'][template_id] = {}

                parsed_dict['peer_policy'][template_id]['index'] = index
                continue

            # Local policies:0x8002069C603, Inherited polices:0x0
            p2 = re.compile(r'^\s*Local +policies:+(?P<local_policies>0x[0-9A-F]+),'
                            ' +Inherited +polices:+(?P<inherited_polices>0x[0-9A-F]+)$')
            m = p2.match(line)
            if m:
                local_policy = m.groupdict()['local_policies']
                inherited_policy = m.groupdict()['inherited_polices']

                parsed_dict['peer_policy'][template_id]['local_policies'] = local_policy
                parsed_dict['peer_policy'][template_id]['inherited_polices'] = inherited_policy
                continue

            # Local disable policies:0x0, Inherited disable policies:0x0
            p3 = re.compile(r'^\s*Local +disable +policies:+(?P<local_disable_policies>0x[0-9A-F]+),'
                            ' +Inherited +disable +policies:+(?P<inherited_disable_polices>0x[0-9A-F]+)$')
            m = p3.match(line)
            if m:
                local_policy = m.groupdict()['local_disable_policies']
                inherited_policy = m.groupdict()['inherited_disable_polices']
                parsed_dict['peer_policy'][template_id]['local_disable_policies'] = local_policy
                parsed_dict['peer_policy'][template_id]['inherited_disable_polices'] = inherited_policy
                continue

            #Locally configured policies:
            p4 = re.compile(r'^\s*Locally +configured +policies:$')
            m = p4.match(line)
            if m:
                continue

            # route-map test in
            p5 = re.compile(r'^\s*route-map +(?P<remote_map_in>[0-9a-zA-Z]+) +in$')
            m = p5.match(line)
            if m:
                route_map_in = m.groupdict()['remote_map_in']
                parsed_dict['peer_policy'][template_id]['route_map_name_in'] = route_map_in
                continue

            # route-map test2 out
            p6 = re.compile(r'^\s*route-map +(?P<route_map_out>[0-9a-zA-Z]+) +out$')
            m = p6.match(line)
            if m:
                route_map_out = m.groupdict()['route_map_out']
                parsed_dict['peer_policy'][template_id]['route_map_name_out'] = route_map_out
                continue

            # default-originate route-map test
            p7 = re.compile(r'^\s*default-originate +route-map'
                            ' +(?P<default_originate_route_map>[0-9a-zA_Z]+)$')
            m = p7.match(line)
            if m:
                default_originate_route_map = m.groupdict()['default_originate_route_map']
                parsed_dict['peer_policy'][template_id]['default_originate'] = True
                parsed_dict['peer_policy'][template_id]['default_originate_route_map'] = \
                    default_originate_route_map
                continue

            # soft-reconfiguration inbound
            p8 = re.compile(r'^\s*soft-reconfiguration'
                            ' +(?P<soft_reconfiguration>[a-zA_Z]+)$')
            m = p8.match(line)
            if m:
                default_originate = m.groupdict()['soft_reconfiguration']
                parsed_dict['peer_policy'][template_id]['soft_reconfiguration'] \
                    = True
                continue

            # maximum-prefix 5555 70 restart 300
            p9 = re.compile(r'^\s*maximum-prefix'
                            ' +(?P<maximum_prefix_max_prefix_no>[0-9]+)'
                            ' +(?P<maximum_prefix_threshold>[0-9]+)'
                            ' +restart +(?P<maximum_prefix_restart>[0-9]+)$')
            m = p9.match(line)
            if m:
                maximum_prefix_max_prefix_no = int(m.groupdict()['maximum_prefix_max_prefix_no'])
                maximum_prefix_restart = int(m.groupdict()['maximum_prefix_restart'])
                maximum_prefix_threshold = int(m.groupdict()['maximum_prefix_threshold'])

                parsed_dict['peer_policy'][template_id]['maximum_prefix_max_prefix_no'] \
                    = maximum_prefix_max_prefix_no
                parsed_dict['peer_policy'][template_id]['maximum_prefix_threshold'] \
                    = maximum_prefix_threshold
                parsed_dict['peer_policy'][template_id]['maximum_prefix_restart'] \
                    = maximum_prefix_restart
                continue

            # as-override
            p10 = re.compile(r'^\s*as-override$')
            m = p10.match(line)
            if m:
                parsed_dict['peer_policy'][template_id]['as_override'] = True
                continue

            # allowas-in 9
            p11 = re.compile(r'^\s*allowas-in +(?P<allowas_in_as_number>[0-9]+)$')
            m = p11.match(line)
            if m:
                parsed_dict['peer_policy'][template_id]['allowas_in'] = True
                parsed_dict['peer_policy'][template_id]['allowas_in_as_number'] = \
                     int(m.groupdict()['allowas_in_as_number'])
                continue

            # route-reflector-client
            p12 = re.compile(r'^\s*route-reflector-client$')
            m = p12.match(line)
            if m:
                parsed_dict['peer_policy'][template_id]['route_reflector_client'] = True
                continue

            # next-hop-self
            p13 = re.compile(r'^\s*next-hop-self$')
            m = p13.match(line)
            if m:
                parsed_dict['peer_policy'][template_id]['next_hop_self'] = True
                continue

            # send-community both
            p14 = re.compile(r'^\s*send-community +(?P<send_community>[\w]+)$')
            m = p14.match(line)
            if m:
                send_community = m.groupdict()['send_community']
                parsed_dict['peer_policy'][template_id]['send_community'] = send_community
                continue

            # soo SoO:100:100
            p15 = re.compile(r'^\s*soo +(?P<soo>[\w\:\d]+)$')
            m = p15.match(line)
            if m:
                soo = m.groupdict()['soo']
                parsed_dict['peer_policy'][template_id]['soo'] = soo
                continue
            # Inherited policies:
            p15 = re.compile(r'^\s*Inherited policies:$')
            m = p15.match(line)
            if m:
                continue

        return parsed_dict