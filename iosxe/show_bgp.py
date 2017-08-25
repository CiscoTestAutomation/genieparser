''' show_bgp.py

Example parser class

'''

import re   
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use

#*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

class ShowIpBgpSummarySchema(MetaParser):

    schema = {
        'bgp_summary':
            {'identifier':
                {Any():
                    {'version': str,
                     'autonomous_system_number': str,
                     'table_version': str,
                    },
                },
             'neighbor':
                {Any():
                    {'ver': str,
                     'asn': str,
                     'msgr': str,
                     'msgs': str,
                     'tblv': str,
                     'inq': str,
                     'outq': str,
                     'up_down': str,
                     'state_pfxrcd': str,
                     },
                },
            },
        }

class ShowIpBgpSummary(ShowIpBgpSummarySchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show ip bgp summary'.format()
        out = self.device.execute(cmd)
        bgp_summary_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*BGP +router +identifier +(?P<router_id>[0-9\.]+)\, +local +AS +number +(?P<as_number>[0-9]+)$')
            m = p1.match(line)
            if m:
                router_id = m.groupdict()['router_id']
                autonomous_system_number = m.groupdict()['as_number']
                if 'bgp_summary' not in bgp_summary_dict:
                    bgp_summary_dict['bgp_summary'] = {}
                if 'identifier' not in bgp_summary_dict['bgp_summary']:
                    bgp_summary_dict['bgp_summary']['identifier'] = {}
                if router_id not in bgp_summary_dict['bgp_summary']['identifier']:
                    bgp_summary_dict['bgp_summary']['identifier'][router_id] = {}
                bgp_summary_dict['bgp_summary']['identifier'][router_id]['autonomous_system_number'] = autonomous_system_number
                continue

            p2 = re.compile(r'^\s*BGP +table +version +is +(?P<table_ver>([0-9]+))\, +main +routing +table +version +(?P<r_t_ver>[0-9]+)$')
            m = p2.match(line)
            if m:
                table_version = m.groupdict()['table_ver']
                version = m.groupdict()['r_t_ver']

                bgp_summary_dict['bgp_summary']['identifier'][router_id]['table_version'] = table_version
                bgp_summary_dict['bgp_summary']['identifier'][router_id]['version'] = version
                continue

            p3 = re.compile(r'^\s*Neighbor +V +AS +MsgRcvd +MsgSent +TblVer +InQ +OutQ +Up/Down +State/PfxRcd$')
            m = p3.match(line)
            if m:
                continue

            p4 = re.compile(r'^\s*(?P<neighbor>[0-9\.]+) +(?P<ver>[0-9]+) +(?P<asn>[0-9]+) +(?P<msgr>[0-9]+) +(?P<msgs>[0-9]+) +(?P<tblv>[0-9]+) +(?P<inq>[0-9]+) +(?P<outq>[0-9]+) +(?P<up_down>[a-zA-Z0-9\:]+) +(?P<state_pfxrcd>[a-zA-Z0-9]+)$')
            m = p4.match(line) 
            if m:
                neighbor = m.groupdict()['neighbor']
                if 'neighbor' not in bgp_summary_dict['bgp_summary']:
                    bgp_summary_dict['bgp_summary']['neighbor'] = {}
                if neighbor not in bgp_summary_dict['bgp_summary']['neighbor']:
                    bgp_summary_dict['bgp_summary']['neighbor'][neighbor] = {}
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['ver'] = str(m.groupdict()['ver'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['asn'] = str(m.groupdict()['asn'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['msgr'] = str(m.groupdict()['msgr'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['msgs'] = str(m.groupdict()['msgs'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['tblv'] = str(m.groupdict()['tblv'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['inq'] = str(m.groupdict()['inq'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['outq'] = str(m.groupdict()['outq'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['up_down'] = str(m.groupdict()['up_down'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['state_pfxrcd'] = str(m.groupdict()['state_pfxrcd'])
                continue

        return bgp_summary_dict


class ShowBgpAllSummarySchema(MetaParser):
    ''' Schema for:
            * 'show bgp all summary'
    '''
    schema = {
        'vrf':
            {Any():
                 {Optional('neighbor'):
                      {Any():
                           {'address_family':
                                {Any():
                                     {'v': int,
                                      'as': int,
                                      'msg_rcvd': int,
                                      'msg_sent': int,
                                      'tbl_ver': int,
                                      'inq': int,
                                      'outq': int,
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
    parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """

    def cli(self):
        cmd = 'show bgp all summary'
        out = self.device.execute(cmd)

        # Init vars
        sum_dict = {}
        cache_dict = {}

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

            p9 = re.compile(r'^\s*(?P<neighbor>[a-zA-Z0-9\.\:]+) +(?P<v>[0-9]+)'
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
                nbr_af_dict['v'] = int(m.groupdict()['v'])
                nbr_af_dict['as'] = int(m.groupdict()['as'])
                nbr_af_dict['msg_rcvd'] = int(m.groupdict()['msg_rcvd'])
                nbr_af_dict['msg_sent'] = int(m.groupdict()['msg_sent'])
                nbr_af_dict['tbl_ver'] = int(m.groupdict()['tbl_ver'])
                nbr_af_dict['inq'] = int(m.groupdict()['inq'])
                nbr_af_dict['outq'] = int(m.groupdict()['outq'])
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
                        # nbr_af_dict['as_path_entries'] = as_path_entries
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
                except:
                    pass

                continue

        return sum_dict
