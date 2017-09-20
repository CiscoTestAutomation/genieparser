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


# ============================================================
# Parser for 'show bgp all neighbors <WORD> advertised-routes'
# ============================================================

class ShowBgpAllNeighborsAdvertisedRoutesSchema(MetaParser):

    '''Schema for show bgp all neighbors <WORD> advertised-routes'''

    schema = {
        'vrf':
            {Any():
                {'neighbor':
                    {Any():
                        {'address_family':
                            {Any():
                                {Optional('bgp_table_version'): int,
                                 Optional('local_router_id'): str,
                                 Optional('route_distinguisher'): str,
                                 Optional('default_vrf'): str,
                                 Optional('advertised'):
                                    {Optional(Any()):
                                        {Optional('index'):
                                            {Optional(Any()):
                                                {Optional('next_hop'): str,
                                                 Optional('status_codes'): str,
                                                 Optional('path_type'): str,
                                                 Optional('metric'): int,
                                                 Optional('localprf'): int,
                                                 Optional('weight'): int,
                                                 Optional('path'): str,
                                                 Optional('origin_codes'): str,
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


class ShowBgpAllNeighborsAdvertisedRoutes(ShowBgpAllNeighborsAdvertisedRoutesSchema):

    '''Parser for show bgp all neighbors <WORD> advertised-routes'''

    def cli(self, neighbor):
        # find vrf names
        # show bgp all neighbors | i BGP neighbor
        cmd_vrfs = 'show bgp all neighbors | i BGP neighbor'
        out_vrf = self.device.execute(cmd_vrfs)
        vrf = 'default'

        for line in out_vrf.splitlines():
            if not line:
                continue
            else:
                line = line.rstrip()

            # BGP neighbor is 2.2.2.2,  remote AS 100, internal link
            p = re.compile(r'^\s*BGP +neighbor +is +(?P<bgp_neighbor>[0-9A-Z\:\.]+)'
                            '(, +vrf +(?P<vrf>[0-9A-Za-z]+))?, +remote AS '
                            '+(?P<remote_as_id>[0-9]+), '
                            '+(?P<internal_external_link>[a-z\s]+)$')
            m = p.match(line)
            if m:
                # Extract the neighbor corresponding VRF name
                bgp_neighbor = str(m.groupdict()['bgp_neighbor'])
                if bgp_neighbor == neighbor:
                    if m.groupdict()['vrf']:
                        vrf = str(m.groupdict()['vrf'])
                else:
                    continue

        # show bgp all neighbors {neighbor} advertised-routes
        cmd  = 'show bgp all neighbors {neighbor} advertised-routes'.format(neighbor=neighbor)
        out = self.device.execute(cmd)

        # Init dictionary
        route_dict = {}
        af_dict = {}

        # Init vars
        data_on_nextline =  False
        index = 1
        bgp_table_version = local_router_id = ''

        for line in out.splitlines():
            line = line.rstrip()

            # For address family: IPv4 Unicast
            p1 = re.compile(r'^\s*For +address +family:'
                             ' +(?P<address_family>[a-zA-Z0-9\s\-\_]+)$')
            m = p1.match(line)
            if m:
                neighbor_id = str(neighbor)
                address_family = str(m.groupdict()['address_family']).lower()
                original_address_family = address_family
                continue

            # BGP table version is 25, Local Router ID is 21.0.101.1
            p2 = re.compile(r'^\s*BGP +table +version +is'
                             ' +(?P<bgp_table_version>[0-9]+), +[Ll]ocal +[Rr]outer'
                             ' +ID +is +(?P<local_router_id>(\S+))$')
            m = p2.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                local_router_id = str(m.groupdict()['local_router_id'])

                # Init dict
                if 'vrf' not in route_dict:
                    route_dict['vrf'] = {}
                if vrf not in route_dict['vrf']:
                    route_dict['vrf'][vrf] = {}
                if 'neighbor' not in route_dict['vrf'][vrf]:
                    route_dict['vrf'][vrf]['neighbor'] = {}
                if neighbor_id not in route_dict['vrf'][vrf]['neighbor']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id] = {}
                if 'address_family' not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'] = {}
                if address_family not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]['address_family']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][address_family] = {}

                # Set af_dict
                af_dict = route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]

                # Init advertised dict
                if 'advertised' not in af_dict:
                    af_dict['advertised'] = {}

                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]['bgp_table_version'] = \
                        bgp_table_version
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]['local_router_id'] = \
                        local_router_id
                continue

            # Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
            # Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
            # Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

            # *>i[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616
            # *>iaaaa:1::/113       ::ffff:19.0.101.1
            # *>  646:22:22::/64   2001:DB8:20:4:6::6
            p3_1 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                             '(?P<path_type>(i|e|c|l|a|r|I))?'
                             '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                             '(?: *(?P<next_hop>[a-zA-Z0-9\.\:\/\[\]\,]+))?$')
            m = p3_1.match(line)
            if m:
                # New prefix, reset index count
                index = 1
                data_on_nextline = True

                # Get keys
                if m.groupdict()['status_codes']:
                    status_codes = str(m.groupdict()['status_codes'].rstrip())
                if m.groupdict()['path_type']:
                    path_type = str(m.groupdict()['path_type'])
                if m.groupdict()['prefix']:
                    prefix = str(m.groupdict()['prefix'])

                # Init dict
                if 'advertised' not in af_dict:
                    af_dict['advertised'] = {}
                if prefix not in af_dict['advertised']:
                    af_dict['advertised'][prefix] = {}
                if 'index' not in af_dict['advertised'][prefix]:
                    af_dict['advertised'][prefix]['index'] = {}
                if index not in af_dict['advertised'][prefix]['index']:
                    af_dict['advertised'][prefix]['index'][index] = {}

                # Set keys
                if m.groupdict()['status_codes']:
                    af_dict['advertised'][prefix]['index'][index]['status_codes'] = status_codes
                if m.groupdict()['path_type']:
                    af_dict['advertised'][prefix]['index'][index]['path_type'] = path_type
                if m.groupdict()['next_hop']:
                    af_dict['advertised'][prefix]['index'][index]['next_hop'] = str(m.groupdict()['next_hop'])
                continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # *>i 15.1.2.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            # *>l1.1.1.0/24         0.0.0.0                           100      32768 i
            # *>r1.3.1.0/24         0.0.0.0               4444        100      32768 ?
            # *>r1.3.2.0/24         0.0.0.0               4444        100      32768 ?
            # *>i1.6.0.0/16         19.0.101.1                        100          0 10 20 30 40 50 60 70 80 90 i
            # *>i1.1.2.0/24         19.0.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
            # Condition placed to handle the situation of a long line that is
            # divided nto two lines while actually it is not another index.
            if not data_on_nextline:
                p3_2 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)'
                                   '(?P<path_type>(i|e|c|l|a|r|I))?(\s)?'
                                   '(?P<prefix>(([0-9]+[\.][0-9]+[\.][0-9]+'
                                   '[\.][0-9]+[\/][0-9]+)|([a-zA-Z0-9]+[\:]'
                                   '[a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:]'
                                   '[a-zA-Z0-9]+[\:][\:][\/][0-9]+)|'
                                   '([a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:]'
                                   '[a-zA-Z0-9]+[\:][\:][\/][0-9]+)))'
                                   ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                                   ' +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}]+)'
                                   ' +(?P<origin_codes>(i|e|\?|\&|\|))$')
                m = p3_2.match(line)
                if m:
                    # New prefix, reset index count
                    index = 1

                    # Get keys
                    if m.groupdict()['status_codes']:
                        status_codes = str(m.groupdict()['status_codes'].rstrip())
                    if m.groupdict()['path_type']:
                        path_type = str(m.groupdict()['path_type'])
                    if m.groupdict()['prefix']:
                        prefix = str(m.groupdict()['prefix'])
                    if m.groupdict()['next_hop']:
                        next_hop = str(m.groupdict()['next_hop'])
                    if m.groupdict()['origin_codes']:
                        origin_codes = str(m.groupdict()['origin_codes'])

                    # Init dict
                    if 'advertised' not in af_dict:
                        af_dict['advertised'] = {}
                    if prefix not in af_dict['advertised']:
                        af_dict['advertised'][prefix] = {}
                    if 'index' not in af_dict['advertised'][prefix]:
                        af_dict['advertised'][prefix]['index'] = {}
                    if index not in af_dict['advertised'][prefix]['index']:
                        af_dict['advertised'][prefix]['index'][index] = {}
                    if index not in af_dict['advertised'][prefix]['index']:
                        af_dict['advertised'][prefix]['index'][index] = {}

                    # Set keys
                    if m.groupdict()['status_codes']:
                        af_dict['advertised'][prefix]['index'][index]['status_codes'] = status_codes
                    if m.groupdict()['path_type']:
                        af_dict['advertised'][prefix]['index'][index]['path_type'] = path_type
                    if m.groupdict()['next_hop']:
                        af_dict['advertised'][prefix]['index'][index]['next_hop'] = next_hop
                    if m.groupdict()['origin_codes']:
                        af_dict['advertised'][prefix]['index'][index]['origin_codes'] = origin_codes

                    # Parse numbers
                    numbers = m.groupdict()['numbers']

                    # Metric     LocPrf     Weight Path
                    #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                    m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                     '(?P<space1>\s{4,10})'
                                     '(?P<localprf>[0-9]+)'
                                     '(?P<space2>\s{5,10})'
                                     '(?P<weight>[0-9]+)'
                                     '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                    #    100        ---          0 10 20 30 40 50 60 70 80 90
                    #    ---        100          0 10 20 30 40 50 60 70 80 90
                    #    100        ---      32788 ---
                    #    ---        100      32788 --- 
                    m2 = re.compile(r'^(?P<value>[0-9]+)'
                                     '(?P<space>\s{2,21})'
                                     '(?P<weight>[0-9]+)'
                                     '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                    #    ---        ---      32788 200 33299 51178 47751 {27016}
                    m3 = re.compile(r'^(?P<weight>[0-9]+)'
                                     ' +(?P<path>[0-9\{\}\s]+)$').match(numbers)

                    if m1:
                        af_dict['advertised'][prefix]['index'][index]['metric'] = int(m1.groupdict()['metric'])
                        af_dict['advertised'][prefix]['index'][index]['localprf'] = int(m1.groupdict()['localprf'])
                        af_dict['advertised'][prefix]['index'][index]['weight'] = int(m1.groupdict()['weight'])
                        # Set path
                        if m1.groupdict()['path']:
                            af_dict['advertised'][prefix]['index'][index]['path'] = m1.groupdict()['path'].strip()
                            continue
                    elif m2:
                        af_dict['advertised'][prefix]['index'][index]['weight'] = int(m2.groupdict()['weight'])
                        # Set metric or localprf
                        if len(m2.groupdict()['space']) > 10:
                            af_dict['advertised'][prefix]['index'][index]['metric'] = int(m2.groupdict()['value'])
                        else:
                            af_dict['advertised'][prefix]['index'][index]['localprf'] = int(m2.groupdict()['value'])
                        # Set path
                        if m2.groupdict()['path']:
                            af_dict['advertised'][prefix]['index'][index]['path'] = m2.groupdict()['path'].strip()
                            continue
                    elif m3:
                        af_dict['advertised'][prefix]['index'][index]['weight'] = int(m3.groupdict()['weight'])
                        af_dict['advertised'][prefix]['index'][index]['path'] = m3.groupdict()['path'].strip()
                        continue

            #                     0.0.0.0               100      32768 i
            #                     19.0.101.1            4444       100 0 3 10 20 30 40 50 60 70 80 90 i
            #*>i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            #                                           2219             0 400 33299 51178 47751 {27016} e
            p3_3 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                               '(?P<path_type>(i|e|c|l|a|r|I))?'
                               ' +(?P<next_hop>(([0-9]+[\.][0-9]+[\.][0-9]'
                               '+[\.][0-9]+)|([a-zA-Z0-9]+[\:][a-zA-Z0-9]+'
                               '[\:][a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:]'
                               '[a-zA-Z0-9]+[\:][\:][a-zA-Z0-9])|'
                               '([a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:][a-zA-Z0-9]+'
                               '[\:][a-zA-Z0-9]+[\:][\:][a-zA-Z0-9])))?'
                               '(?: +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}]+))?'
                               ' +(?P<origin_codes>(i|e|\?|\|))$')
            m = p3_3.match(line)
            if m:
                # Get keys
                if m.groupdict()['next_hop']:
                    next_hop = str(m.groupdict()['next_hop'])
                if m.groupdict()['origin_codes']:
                    origin_codes = str(m.groupdict()['origin_codes'])

                if data_on_nextline:
                    data_on_nextline =  False
                else:
                    index += 1

                # Init dict
                if 'advertised' not in af_dict:
                    af_dict['advertised'] = {}
                if prefix not in af_dict['advertised']:
                    af_dict['advertised'][prefix] = {}
                if 'index' not in af_dict['advertised'][prefix]:
                    af_dict['advertised'][prefix]['index'] = {}
                if index not in af_dict['advertised'][prefix]['index']:
                    af_dict['advertised'][prefix]['index'][index] = {}

                # Set keys
                if m.groupdict()['next_hop']:
                    af_dict['advertised'][prefix]['index'][index]['next_hop'] = next_hop
                if m.groupdict()['origin_codes']:
                    af_dict['advertised'][prefix]['index'][index]['origin_codes'] = origin_codes
                try:
                    # Set values of status_codes and path_type from prefix line
                    af_dict['advertised'][prefix]['index'][index]['status_codes'] = status_codes
                    af_dict['advertised'][prefix]['index'][index]['path_type'] = path_type
                except:
                    pass

                # Parse numbers
                numbers = m.groupdict()['numbers']

                # Metric     LocPrf     Weight Path
                #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                 '(?P<space1>\s{4,10})'
                                 '(?P<localprf>[0-9]+)'
                                 '(?P<space2>\s{5,10})'
                                 '(?P<weight>[0-9]+)'
                                 '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                #    100        ---          0 10 20 30 40 50 60 70 80 90
                #    ---        100          0 10 20 30 40 50 60 70 80 90
                #    100        ---      32788 ---
                #    ---        100      32788 --- 
                m2 = re.compile(r'^(?P<value>[0-9]+)'
                                 '(?P<space>\s{2,21})'
                                 '(?P<weight>[0-9]+)'
                                 '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                #    ---        ---      32788 200 33299 51178 47751 {27016}
                m3 = re.compile(r'^(?P<weight>[0-9]+)'
                                 ' +(?P<path>[0-9\{\}\s]+)$').match(numbers)

                if m1:
                    af_dict['advertised'][prefix]['index'][index]['metric'] = int(m1.groupdict()['metric'])
                    af_dict['advertised'][prefix]['index'][index]['localprf'] = int(m1.groupdict()['localprf'])
                    af_dict['advertised'][prefix]['index'][index]['weight'] = int(m1.groupdict()['weight'])
                    # Set path
                    if m1.groupdict()['path']:
                        af_dict['advertised'][prefix]['index'][index]['path'] = m1.groupdict()['path'].strip()
                        continue
                elif m2:
                    af_dict['advertised'][prefix]['index'][index]['weight'] = int(m2.groupdict()['weight'])
                    # Set metric or localprf
                    if len(m2.groupdict()['space']) > 10:
                        af_dict['advertised'][prefix]['index'][index]['metric'] = int(m2.groupdict()['value'])
                    else:
                        af_dict['advertised'][prefix]['index'][index]['localprf'] = int(m2.groupdict()['value'])
                    # Set path
                    if m2.groupdict()['path']:
                        af_dict['advertised'][prefix]['index'][index]['path'] = m2.groupdict()['path'].strip()
                        continue
                elif m3:
                    af_dict['advertised'][prefix]['index'][index]['weight'] = int(m3.groupdict()['weight'])
                    af_dict['advertised'][prefix]['index'][index]['path'] = m3.groupdict()['path'].strip()
                    continue

            # Route Distinguisher: 200:1
            # Route Distinguisher: 300:1 (default for vrf VRF1) VRF Router ID 44.44.44.44
            p4 = re.compile(r'^\s*Route +Distinguisher *: '
                             '+(?P<route_distinguisher>(\S+))'
                             '( +\(default for vrf +(?P<default_vrf>(\S+))\))?'
                             '( +VRF Router ID (?P<vrf_router_id>(\S+)))?$')
            m = p4.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])
                new_address_family = original_address_family + ' RD ' + route_distinguisher

                # Init dict
                if 'address_family' not in route_dict['vrf'][vrf]['neighbor']\
                        [neighbor_id]:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'] = {}
                if new_address_family not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]['address_family']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][new_address_family] = {}

                # Set keys
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][new_address_family]['bgp_table_version'] = bgp_table_version
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][new_address_family]['local_router_id'] = local_router_id
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][new_address_family]['route_distinguisher'] = route_distinguisher
                if m.groupdict()['default_vrf']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][new_address_family]['default_vrf'] = \
                            str(m.groupdict()['default_vrf'])

                # Reset address_family key and af_dict for use in other regex
                address_family = new_address_family
                af_dict = route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]

                # Init advertised dict
                if 'advertised' not in af_dict:
                    af_dict['advertised'] = {}
                    continue

        return route_dict


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
