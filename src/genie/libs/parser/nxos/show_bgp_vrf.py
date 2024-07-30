"""show_bgp_vrf.py

* 'show bgp vrf all all'
* 'show bgp vrf all all neighbors'
* 'show bgp vrf all all nexthop-database'
* 'show bgp vrf <WORD> all summary'
* 'show bgp vrf <WORD> all summary | xml'
* 'show bgp vrf <WROD> all dampening parameters'
* 'show bgp vrf <WROD> all dampening parameters | xml'
* 'show bgp vrf all all neighbors <WORD> advertised-routes'
* 'show bgp vrf all all neighbors <WORD> routes'
* 'show bgp vrf all all neighbors <WORD> received-routes'
* 'show bgp vrf <vrf> <address_family>  policy statistics redistribute'
* 'show bgp vrf <vrf> <address_family>  policy statistics redistribute | xml'
* 'show bgp vrf <vrf> <address_family>  policy statistics dampening'
* 'show bgp vrf <vrf> <address_family>  policy statistics dampening | xml'
* 'show bgp vrf <vrf> <address_family>  policy statistics neighbor <neighbor>'
* 'show bgp vrf <vrf> <address_family>  policy statistics neighbor <neighbor> | xml'
"""

# Python
import re
from copy import deepcopy
import xml.etree.ElementTree as ET

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use, ListOf

# Parser
from genie.libs.parser.yang.bgp_openconfig_yang import BgpOpenconfigYang

# import parser utils
from genie.libs.parser.utils.common import Common

# =================================
# Schema for 'show bgp vrf all all'
# =================================
class ShowBgpVrfAllAllSchema(MetaParser):
    """Schema for show bgp vrf all all"""

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'bgp_table_version': int,
                         'local_router_id': str,
                         Optional('route_distinguisher'): str,
                         Optional('default_vrf'): str,
                         Optional('aggregate_address_ipv4_address'): str,
                         Optional('aggregate_address_ipv4_mask'): str,
                         Optional('aggregate_address_as_set'): bool,
                         Optional('aggregate_address_summary_only'): bool,
                         Optional('v6_aggregate_address_ipv6_address'): str,
                         Optional('v6_aggregate_address_as_set'): bool,
                         Optional('v6_aggregate_address_summary_only'): bool,
                         Optional('prefixes'):
                            {Any(): 
                                {'index': 
                                    {Any(): 
                                        {'next_hop': str,
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
        }

# =================================
# Parser for 'show bgp vrf all all'
# =================================
class ShowBgpVrfAllAll(ShowBgpVrfAllAllSchema):
    """Parser for show bgp vrf <vrf>> <address_family>"""

    cli_command = 'show bgp vrf {vrf} {address_family}'
    exclude = [
      'bgp_table_version',
      'status_codes',
      'local_router_id',
      'path_type',
      'weight']

    def cli(self, vrf='all', address_family='all', output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(vrf=vrf,
                                                              address_family=address_family))
        else:
            out = output

        # Init dictionary
        parsed_dict = {}
        af_dict = {}
        prefix_dict = {}

        # Init vars
        index = 1
        data_on_nextline = False
        bgp_table_version = local_router_id = ''

        p = re.compile(r'^\s*Network +Next Hop +Metric +LocPrf +Weight Path$')
        p1 = re.compile(r'^\s*BGP +routing +table +information +for +VRF'
                            ' +(?P<vrf_name>\S+), +address +family'
                            ' +(?P<address_family>[a-zA-Z0-9\s\-\_]+)$')
        p2 = re.compile(r'^\s*BGP +table +version +is'
                            ' +(?P<bgp_table_version>[0-9]+), +(L|l)ocal'
                            ' +(R|r)outer +ID +is +(?P<local_router_id>[0-9\.]+)$')
        p3_4 = re.compile(r'^\s*(?P<next_hop>[a-zA-Z0-9\.\:\/\[\]\,]+)$')
        p3_1 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                            '(?P<path_type>(i|e|c|l|a|r|I))?'
                            '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                            '(?: *(?P<next_hop>[a-zA-Z0-9\.\:\/\[\]\,]+))?$')
        p3_1_2 = re.compile(r'^(?P<status_codes>(s|x|S|d|h|\*|\>)+)(?P<path_type>'
            '(i|e|c|l|a|r|I))(?P<prefix>[\w\.\/]+) +(?P<next_hop>[\w\.\/]+) +'
            '(?P<metric>\d+) +(?P<localprf>\d+) +(?P<weight>\d+) +(?P<path>[\d ]+) +'
            '(?P<origin_codes>(i|e|\?|\||&))$')
        p3_3 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                            '(?P<path_type>(i|e|c|l|a|r|I))?'
                            ' *(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                            '(?: +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}]+))?'
                            ' +(?P<origin_codes>(i|e|\?|\|))$')
        p3_3_1 = re.compile(r'^\s*(?P<status_codes>(\*\>|s|x|S|d|h|\*|\>|\s)+)'
                                '(?P<path_type>(i|e|c|l|a|r|I))?'
                                '( *(?P<origin_codes>(i|e|\?|\&|\|)+))'
                                ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                                ' +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}\?]+)$')
        p4 = re.compile(r'^\s*Route +Distinguisher *:'
                            ' +(?P<route_distinguisher>(\S+))'
                            '(?: +\(((VRF +(?P<default_vrf>\S+))|'
                            '((?P<default_vrf1>\S+)VNI +(?P<vni>\d+)))\))?$')
        p3_2 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)'
                            '(?P<path_type>(i|e|c|l|a|r|I))'
                            '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                            ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                            ' +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}]+)'
                            ' +(?P<origin_codes>(i|e|\?|\&|\|))$')
        p3_2_1 = re.compile(r'^\s*(?P<status_codes>(\*\>|s|x|S|d|h|\*|\>|\s)+)'
                                '(?P<path_type>(i|e|c|l|a|r|I))?'
                                '( *(?P<origin_codes>(i|e|\?|\&|\|)+))'
                                '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                                ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                                ' +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}\?]+)$')

        for line in out.splitlines():
            line = line.rstrip()
            # Network            Next Hop            Metric     LocPrf     Weight Path
            m = p.match(line)
            if m:
                continue

            # BGP routing table information for VRF VRF1, address family IPv4 Unicast
            m = p1.match(line)
            if m:
                # Get values
                vrf_name = str(m.groupdict()['vrf_name'])
                address_family = str(m.groupdict()['address_family']).lower()
                original_address_family = address_family
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf_name not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf_name] = {}
                if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'] = {}
                if address_family not in parsed_dict['vrf'][vrf_name]\
                    ['address_family']:
                    parsed_dict['vrf'][vrf_name]['address_family'][address_family] = {}

                # Set af_dict
                af_dict = parsed_dict['vrf'][vrf_name]['address_family'][address_family]
                continue

            # BGP table version is 35, local router ID is 10.229.11.11
            # BGP table version is 381, Local Router ID is 10.4.1.2
            m = p2.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                local_router_id = str(m.groupdict()['local_router_id'])
                af_dict['bgp_table_version'] = bgp_table_version
                af_dict['local_router_id'] = local_router_id
                continue

            # Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
            # Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist
            # Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath
            # Network            Next Hop         Metric   LocPrf   Weight Path
            
            # *>i[2]:[77][7,0][10.69.9.9,1,151587081][10.135.1.1,22][10.106.101.1,10.76.1.30]/616
            # *>i2001:db8:aaaa:1::/113       ::ffff:10.106.101.1
            m = p3_1.match(line)
            # *>i10.111.8.3/32     10.84.66.66           2000        100          0 200 i
            # *>i10.111.8.4/32     10.84.66.66           2000        100          0 200 i
            m1 = p3_1_2.match(line)

            m = m if m else m1
            if m:
                # New prefix, reset index count
                index = 1
                data_on_nextline = True

                # Get keys
                status_codes = str(m.groupdict()['status_codes'])
                path_type = str(m.groupdict()['path_type'])
                prefix = str(m.groupdict()['prefix'])
                if status_codes == 'None' or path_type == 'None' or prefix == 'None':
                    continue
                # Init dict
                if 'prefixes' not in af_dict:
                    af_dict['prefixes'] = {}
                if prefix not in af_dict['prefixes']:
                    af_dict['prefixes'][prefix] = {}
                if 'index' not in af_dict['prefixes'][prefix]:
                    af_dict['prefixes'][prefix]['index'] = {}
                if index not in af_dict['prefixes'][prefix]['index']:
                    af_dict['prefixes'][prefix]['index'][index] = {}

                # Set keys
                af_dict['prefixes'][prefix]['index'][index]['status_codes'] = status_codes
                af_dict['prefixes'][prefix]['index'][index]['path_type'] = path_type
                if 'next_hop' in m.groupdict():
                    af_dict['prefixes'][prefix]['index'][index]['next_hop'] = str(m.groupdict()['next_hop'])
                if 'metric' in m.groupdict():
                    af_dict['prefixes'][prefix]['index'][index]['metric'] = int(m.groupdict()['metric'])
                if 'localprf' in m.groupdict():
                    af_dict['prefixes'][prefix]['index'][index]['localprf'] = int(m.groupdict()['localprf'])
                if 'weight' in m.groupdict():
                    af_dict['prefixes'][prefix]['index'][index]['weight'] = int(m.groupdict()['weight'])
                if 'path' in m.groupdict():
                    af_dict['prefixes'][prefix]['index'][index]['path'] = m.groupdict()['path'].strip()
                if 'origin_codes' in m.groupdict():                
                    af_dict['prefixes'][prefix]['index'][index]['origin_codes'] = str(m.groupdict()['origin_codes'])
                
                # Check if aggregate_address_ipv4_address
                if 'a' in path_type:
                    address, mask = prefix.split("/")
                    if ':' in prefix:
                        af_dict['v6_aggregate_address_ipv6_address'] = prefix
                        af_dict['v6_aggregate_address_as_set'] = True
                        af_dict['v6_aggregate_address_summary_only'] = True
                        continue
                    else:
                        af_dict['aggregate_address_ipv4_address'] = address
                        af_dict['aggregate_address_ipv4_mask'] = mask
                        af_dict['aggregate_address_as_set'] = True
                        af_dict['aggregate_address_summary_only'] = True
                        continue
                continue


            #                     0.0.0.0               100      32768 i
            #                     10.106.101.1            4444       100 0 3 10 20 30 40 50 60 70 80 90 i
            # *>i                 10.106.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
            m = p3_3.match(line)

            # * e                   10.70.2.2                                      0 100 300 ?
            # *>e                   10.70.1.2                                      0 100 300 ?
            m1 = p3_3_1.match(line)
            m = m if m else m1
            if m:
                # Get keys
                if m.groupdict()['status_codes']:
                    status_codes = str(m.groupdict()['status_codes'])
                if m.groupdict()['path_type']:
                    path_type = str(m.groupdict()['path_type'])
                next_hop = str(m.groupdict()['next_hop'])
                origin_codes = str(m.groupdict()['origin_codes'])

                if data_on_nextline:
                    data_on_nextline =  False
                else:
                    index += 1

                # Init dict
                if 'prefixes' not in af_dict:
                    af_dict['prefixes'] = {}
                if prefix not in af_dict['prefixes']:
                    af_dict['prefixes'][prefix] = {}
                if 'index' not in af_dict['prefixes'][prefix]:
                    af_dict['prefixes'][prefix]['index'] = {}
                if index not in af_dict['prefixes'][prefix]['index']:
                    af_dict['prefixes'][prefix]['index'][index] = {}

                # Set keys
                af_dict['prefixes'][prefix]['index'][index]['next_hop'] = next_hop
                af_dict['prefixes'][prefix]['index'][index]['origin_codes'] = origin_codes

                try:
                    # Set values of status_codes and path_type from prefix line
                    af_dict['prefixes'][prefix]['index'][index]['status_codes'] = status_codes
                    af_dict['prefixes'][prefix]['index'][index]['path_type'] = path_type
                except Exception:
                    pass

                # Parse numbers
                numbers = m.groupdict()['numbers']
                
                # Metric     LocPrf     Weight Path
                #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                 '(?P<space1>\s{5,10})'
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
                    af_dict['prefixes'][prefix]['index'][index]['metric'] = int(m1.groupdict()['metric'])
                    af_dict['prefixes'][prefix]['index'][index]['localprf'] = int(m1.groupdict()['localprf'])
                    af_dict['prefixes'][prefix]['index'][index]['weight'] = int(m1.groupdict()['weight'])
                    # Set path
                    if m1.groupdict()['path']:
                        af_dict['prefixes'][prefix]['index'][index]['path'] = m1.groupdict()['path'].strip()
                        continue
                elif m2:
                    af_dict['prefixes'][prefix]['index'][index]['weight'] = int(m2.groupdict()['weight'])
                    # Set metric or localprf
                    if len(m2.groupdict()['space']) > 10:
                        af_dict['prefixes'][prefix]['index'][index]['metric'] = int(m2.groupdict()['value'])
                    else:
                        af_dict['prefixes'][prefix]['index'][index]['localprf'] = int(m2.groupdict()['value'])
                    # Set path
                    if m2.groupdict()['path']:
                        af_dict['prefixes'][prefix]['index'][index]['path'] = m2.groupdict()['path'].strip()
                        continue
                elif m3:
                    af_dict['prefixes'][prefix]['index'][index]['weight'] = int(m3.groupdict()['weight'])
                    af_dict['prefixes'][prefix]['index'][index]['path'] = m3.groupdict()['path'].strip()
                    continue
                continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # Route Distinguisher: 100:100     (VRF VRF1)
            # Route Distinguisher: 2:100    (VRF vpn2)
            # Route Distinguisher: 10.49.1.0:3    (L3VNI 9100)
            m = p4.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])
                new_address_family = original_address_family + ' RD ' + route_distinguisher
                
                # Init dict
                if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'] = {}
                if new_address_family not in parsed_dict['vrf'][vrf_name]['address_family']:
                    parsed_dict['vrf'][vrf_name]['address_family'][new_address_family] = {}
                
                # Set keys
                parsed_dict['vrf'][vrf_name]['address_family'][new_address_family]['bgp_table_version'] = bgp_table_version
                parsed_dict['vrf'][vrf_name]['address_family'][new_address_family]['local_router_id'] = local_router_id
                parsed_dict['vrf'][vrf_name]['address_family'][new_address_family]['route_distinguisher'] = route_distinguisher


                if m.groupdict()['default_vrf']:
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [new_address_family]['default_vrf'] = \
                            str(m.groupdict()['default_vrf'])
                elif m.groupdict()['default_vrf1']:
                    parsed_dict['vrf'][vrf_name]['address_family']\
                        [new_address_family]['default_vrf'] = \
                            str(m.groupdict()['default_vrf1'])

                # Reset address_family key and af_dict for use in other regex
                address_family = new_address_family
                af_dict = parsed_dict['vrf'][vrf_name]['address_family'][address_family]
                continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # *>a10.121.0.0/8       0.0.0.0                  100      32768 i
            # *>i10.21.33.33/32   10.36.3.3         0        100          0 ?
            # l10.34.34.0/24      0.0.0.0                  100      32768 i
            # *>i2001::33/128     ::ffff:10.36.3.3  0        100          0 ?
            # *>l[2]:[0]:[0]:[48]:[0000.19ff.f320]:[0]:[0.0.0.0]/216
            # *>i                 10.186.0.2        0        100          0 ?
            # *>l10.4.1.0/24        0.0.0.0                            100      32768 i
            # *>r10.16.1.0/24        0.0.0.0                4444        100      32768 ?
            # *>r10.16.2.0/24        0.0.0.0                4444        100      32768 ?
            # *>i10.49.0.0/16     10.106.101.1                            100          0 10 20 30 40 50 60 70 80 90 i
            # *>i10.4.2.0/24     10.106.102.4                            100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
            m = p3_2.match(line)

            # *&i10.145.1.0/24        192.168.151.2                0        100          0 ?
            m1 = p3_2_1.match(line)
            m = m if m else m1
            if m:
                # New prefix, reset index count
                index = 1
                
                # Get keys
                status_codes = str(m.groupdict()['status_codes'])
                path_type = str(m.groupdict()['path_type'])
                prefix = str(m.groupdict()['prefix'])
                next_hop = str(m.groupdict()['next_hop'])
                origin_codes = str(m.groupdict()['origin_codes'])

                # Init dict
                if 'prefixes' not in af_dict:
                    af_dict['prefixes'] = {}
                if prefix not in af_dict['prefixes']:
                    af_dict['prefixes'][prefix] = {}
                if 'index' not in af_dict['prefixes'][prefix]:
                    af_dict['prefixes'][prefix]['index'] = {}
                if index not in af_dict['prefixes'][prefix]['index']:
                    af_dict['prefixes'][prefix]['index'][index] = {}
                if index not in af_dict['prefixes'][prefix]['index']:
                    af_dict['prefixes'][prefix]['index'][index] = {}

                # Set keys
                af_dict['prefixes'][prefix]['index'][index]['status_codes'] = status_codes
                af_dict['prefixes'][prefix]['index'][index]['path_type'] = path_type
                af_dict['prefixes'][prefix]['index'][index]['next_hop'] = next_hop
                af_dict['prefixes'][prefix]['index'][index]['origin_codes'] = origin_codes

                # Parse numbers
                numbers = m.groupdict()['numbers']
                
                # Metric     LocPrf     Weight Path
                #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                 '(?P<space1>\s{5,10})'
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
                    af_dict['prefixes'][prefix]['index'][index]['metric'] = int(m1.groupdict()['metric'])
                    af_dict['prefixes'][prefix]['index'][index]['localprf'] = int(m1.groupdict()['localprf'])
                    af_dict['prefixes'][prefix]['index'][index]['weight'] = int(m1.groupdict()['weight'])
                    # Set path
                    if m1.groupdict()['path']:
                        af_dict['prefixes'][prefix]['index'][index]['path'] = m1.groupdict()['path'].strip()
                elif m2:
                    af_dict['prefixes'][prefix]['index'][index]['weight'] = int(m2.groupdict()['weight'])
                    # Set metric or localprf
                    if len(m2.groupdict()['space']) > 10:
                        af_dict['prefixes'][prefix]['index'][index]['metric'] = int(m2.groupdict()['value'])
                    else:
                        af_dict['prefixes'][prefix]['index'][index]['localprf'] = int(m2.groupdict()['value'])
                    # Set path
                    if m2.groupdict()['path']:
                        af_dict['prefixes'][prefix]['index'][index]['path'] = m2.groupdict()['path'].strip()
                elif m3:
                    af_dict['prefixes'][prefix]['index'][index]['weight'] = int(m3.groupdict()['weight'])
                    af_dict['prefixes'][prefix]['index'][index]['path'] = m3.groupdict()['path'].strip()

                # Check if aggregate_address_ipv4_address
                if 'a' in path_type:
                    address, mask = prefix.split("/")
                    if ':' in prefix:
                        af_dict['v6_aggregate_address_ipv6_address'] = prefix
                        af_dict['v6_aggregate_address_as_set'] = True
                        af_dict['v6_aggregate_address_summary_only'] = True
                        continue
                    else:
                        af_dict['aggregate_address_ipv4_address'] = address
                        af_dict['aggregate_address_ipv4_mask'] = mask
                        af_dict['aggregate_address_as_set'] = True
                        af_dict['aggregate_address_summary_only'] = True
                        continue
                continue

            #                     2001:db8:400:13b1:21a:1ff:fe00:161/128
            m = p3_4.match(line)
            if m:
                # Get keys
                if 'njected' not in line and 'next_hop' in m.groupdict():
                    next_hop = str(m.groupdict()['next_hop'])

                    if data_on_nextline:
                        data_on_nextline =  False
                    else:
                        index += 1

                    # Init dict
                    index_dict = af_dict.setdefault('prefixes', {}).setdefault(prefix, {})\
                      .setdefault('index', {}).setdefault(index, {})

                    # Set keys
                    index_dict['next_hop'] = next_hop
                continue

        # order the af prefixes index
        # return dict when parsed dictionary is empty
        if 'vrf' not in parsed_dict:
            return parsed_dict

        for vrf_name in parsed_dict['vrf']:
            if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                continue
            for af in parsed_dict['vrf'][vrf_name]['address_family']:
                af_dict = parsed_dict['vrf'][vrf_name]['address_family'][af]
                if 'prefixes' in af_dict:
                    for prefixes in af_dict['prefixes']:
                        if len(af_dict['prefixes'][prefixes]['index'].keys()) > 1:                            
                            ind = 1
                            nexthop_dict = {}
                            sorted_list = sorted(af_dict['prefixes'][prefixes]['index'].items(),
                                               key = lambda x:x[1]['next_hop'])
                            for i, j in enumerate(sorted_list):
                                nexthop_dict[ind] = af_dict['prefixes'][prefixes]['index'][j[0]]
                                ind += 1
                            del(af_dict['prefixes'][prefixes]['index'])
                            af_dict['prefixes'][prefixes]['index'] = nexthop_dict

        return parsed_dict


# ==============================================
# Schema for 'show bgp vrf <vrf> all neighbors'
# ==============================================
class ShowBgpVrfAllNeighborsSchema(MetaParser):
    """Schema for show bgp vrf <vrf> all neighbors"""

    schema = {
        'neighbor':
            {Any(): 
                {'remote_as': int,
                 Optional('local_as'): str,
                 Optional('peer_fab_type'): str,
                 Optional('link'): str,
                 Optional('peer_index'): int,
                 Optional('description'): str,
                 Optional('bgp_version'): int,
                 Optional('router_id'): str,
                 Optional('session_state'): str,
                 Optional('state_reason'): str,
                 Optional('shutdown'): bool,
                 Optional('up_time'): str,
                 Optional('peer_group'): str,
                 Optional('suppress_four_byte_as_capability'): bool,
                 Optional('retry_time'): str,
                 Optional('update_source'): str,
                 Optional('bfd_live_detection'): bool,
                 Optional('bfd_enabled'): bool,
                 Optional('bfd_state'): str,
                 Optional('nbr_local_as_cmd'): str,
                 Optional('last_read'): str,
                 Optional('holdtime'): int,
                 Optional('keepalive_interval'): int,
                 Optional('bgp_negotiated_keepalive_timers'): 
                    {Optional('last_read'): str,
                     Optional('keepalive_interval'): int,
                     Optional('hold_time'): int,
                     Optional('last_written'): str,
                     Optional('keepalive_timer'): str,
                    },
                 Optional('minimum_advertisement_interval'): int,
                 Optional('disable_connected_check'): bool,
                 Optional('inherit_peer_session'): str,
                 Optional('ebgp_multihop_max_hop'): int,
                 Optional('ebgp_multihop'): bool,
                 Optional('tcp_md5_auth'): str,
                 Optional('tcp_md5_auth_config'): str,
                 Optional('received_messages'): int,
                 Optional('received_notifications'): int,
                 Optional('received_bytes_queue'): int,
                 Optional('sent_messages'): int,
                 Optional('sent_notifications'): int,
                 Optional('sent_bytes_queue'): int,
                 Optional('enabled'): bool,
                 Optional('remove_private_as'): bool,
                 Optional('nbr_ebgp_multihop'): bool,
                 Optional('nbr_ebgp_multihop_max_hop'): int,
                 Optional('route_reflector_cluster_id'): int,
                 Optional('graceful_restart'): bool,
                 Optional('graceful_restart_helper_only'): bool,
                 Optional('graceful_restart_restart_time'): int,
                 Optional('graceful_restart_stalepath_time'): int,
                 Optional('allow_own_as'): int,
                 Optional('send_community'): str,
                 Optional('route_reflector_client'): bool,
                 Optional('bgp_session_transport'):
                    {Optional('connection'): 
                        {Optional('mode'): str,
                         Optional('last_reset'): str,
                         Optional('reset_reason'): str,
                         Optional('reset_by'): str,
                         Optional('attempts'): int,
                         Optional('established'): int,
                         Optional('dropped'): int,
                        },
                     Optional('transport'):
                        {Optional('local_port'): str,
                         Optional('local_host'): str,
                         Optional('foreign_port'): str,
                         Optional('foreign_host'): str,
                         Optional('fd'): str,
                         Optional('passive_mode'): str,
                        },
                    },
                 Optional('bgp_neighbor_counters'):
                    {Optional('messages'):
                        {Optional('sent'): 
                            {Any(): int,
                            },
                         Optional('received'):
                            {Any(): int,
                            },
                        },
                    },
                 Optional('bgp_negotiated_capabilities'): 
                    {Optional('route_refresh'): str,
                     Optional('route_refresh_old'): str,
                     Optional('vpnv4_unicast'): str,
                     Optional('vpnv6_unicast'): str,
                     Optional('ipv4_mvpn'): str,
                     Optional('graceful_restart'): str,
                     Optional('enhanced_refresh'): str,
                     Optional('multisession'): str,
                     Optional('stateful_switchover'): str,
                     Optional('dynamic_capability'): str,
                     Optional('dynamic_capability_old'): str,
                    },
                 Optional('graceful_restart_paramters'): 
                    {Optional('address_families_advertised_to_peer'): str,
                     Optional('address_families_advertised_from_peer'): str,
                     Optional('restart_time_advertised_to_peer_seconds'): int,
                     Optional('restart_time_advertised_by_peer_seconds'): int,
                     Optional('stale_time_advertised_by_peer_seconds'): int,
                    },
                 Optional('address_family'): 
                    {Any(): 
                        {Optional('bgp_table_version'): int,
                         Optional('session_state'): str,
                         Optional('state_reason'): str,
                         Optional('neighbor_version'): int,
                         Optional('send_community'): str,
                         Optional('soo'): str,
                         Optional('soft_configuration'): bool,
                         Optional('next_hop_self'): bool,
                         Optional('third_party_nexthop'): bool,
                         Optional('as_override_count'): int,
                         Optional('as_override'): bool,
                         Optional('maximum_prefix_max_prefix_no'): int,
                         Optional('route_map_name_in'): str,
                         Optional('route_map_name_out'): str,
                         Optional('default_originate'): bool,
                         Optional('default_originate_route_map'): str,
                         Optional('route_reflector_client'): bool,
                         Optional('enabled'): bool,
                         Optional('graceful_restart'): bool,
                         Optional('ipv4_unicast_send_default_route'): bool,
                         Optional('ipv6_unicast_send_default_route'): bool,
                         Optional('path'): 
                            {Optional('total_entries'): int,
                             Optional('memory_usage'): int,
                             Optional('accepted_paths'): int,
                            },
                         Optional('inherit_peer_policy'):
                            {Any():
                                {Optional('inherit_peer_seq'): int,
                                },
                            },
                        },
                    },
                },
            },
        }

# ==============================================
# Parser for 'show bgp vrf <vrf> all neighbors'
# ==============================================
class ShowBgpVrfAllNeighbors(ShowBgpVrfAllNeighborsSchema):
    """Parser for:
        show bgp vrf <vrf> all neighbors
        parser class - implements detail parsing mechanisms for cli and yang output.
        """
    cli_command = ['show bgp vrf {vrf} {address_family} neighbors',
                   'show bgp vrf {vrf} {address_family} neighbors {neighbor}',
                   'show bgp vrf {vrf} all neighbors']
    exclude = [
      'up_time',
      'retry_time',
      'bgp_table_version',
      'bgp_negotiated_keepalive_timers',
      'bgp_session_transport',
      'bgp_neighbor_counters',
      'bgp_negotiated_capabilities',
      'graceful_restart_paramters',
      'path',
      'received_messages',
      'neighbor_version',
      'third_party_nexthop',
      'peer_index',
      'sent_messages',
      'sent_notifications',
      'received_notifications',
      'msg_sent',
      'tbl_ver',
      'msg_rcvd']

    def cli(self, vrf='all', address_family='all', neighbor='', output=None):
        if output is None:
            if neighbor:
                out = self.device.execute(self.cli_command[1].format(vrf=vrf,
                                                              address_family=address_family,
                                                              neighbor=neighbor))
            else:
                if address_family:
                    out = self.device.execute(self.cli_command[0].format(vrf=vrf,
                                                              address_family=address_family))
                else:
                    out = self.device.execute(self.cli_command[0].format(vrf=vrf))
        else:
            out = output

        # Init vars
        parsed_dict = {}
        standard_send_community = False

        p1 = re.compile(r'^\s*BGP +neighbor +is +(?P<neighbor_id>[a-zA-Z0-9\.\:]+),'
                            ' +remote +AS +(?P<remote_as>[0-9]+),'
                            '(?: +local +AS +(?P<local_as>[0-9]+),)?'
                            ' +(?P<link>[a-zA-Z]+) +link,'
                            '( +(?P<peer_fab_type>[fabric\-\S]+),)?'
                            ' +Peer +index +(?P<peer_index>[0-9]+)$')
        p2 = re.compile(r'^\s*Description *: +(?P<description>(\S+))$')
        p3 = re.compile(r'^\s*BGP +version +(?P<bgp_version>[0-9]+),'
                            ' +remote +router +ID +(?P<router_id>[0-9\.]+)$')
        p4 = re.compile(r'^\s*\s*BGP +state += +(?P<session_state>(\S+))'
                            '(?: +\((?P<reason>([a-zA-Z\s\/\-]+))\))?,'
                            ' +(up|down) +for +(?P<up_time>[a-zA-Z0-9\:\.]+)'
                            '(?: *, +retry +in +(?P<retry_time>[0-9\.\:]+))?$')
        p5 = re.compile(r'^\s*Using +(?P<update_source>[a-zA-Z0-9]+)'
                            ' +as +update +source +for +this +peer$')
        p6 = re.compile(r'^\s*BFD live-detection is configured'
                            '(?: +and +(?P<bfd_enabled>(\S+)), +state +is'
                            ' +(?P<bfd_state>(\S+)))?$')
        p7 = re.compile(r'^\s*Neighbor +local-as +command'
                            ' +(?P<nbr_local_as_cmd>[a-zA-Z\s]+)$')
        p8 = re.compile(r'^\s*Last +read +(?P<last_read>[a-zA-Z0-9\:]+),'
                            ' +hold +time += +(?P<holdtime>[0-9]+), +keepalive'
                            ' +interval +is +(?P<keepalive_interval>[0-9]+)'
                            ' +seconds$')
        p9 = re.compile(r'^\s*Last +written'
                            ' +(?P<last_written>[a-zA-Z0-9\:]+), +keepalive'
                            ' +timer +(?P<keepalive_timer>[a-zA-Z0-9\:\s]+)$')
        p10 = re.compile(r'^\s*Inherits +session +configuration +from'
                        ' +session-template +(?P<template>[a-zA-Z\-\_]+)$')
        p11 = re.compile(r'^\s*Connected check is disabled$')
        p11_2 = re.compile(r'^\s*Private +AS +numbers +removed +from +updates +sent +to +this +neighbor$')
        p12_1 = re.compile(r'^\s*External +BGP +peer +might +be +upto'
                            ' +(?P<ebgp_multihop_max_hop>[0-9]+) +hops +away$')
        p12_2 = re.compile(r'^\s*External +BGP +peer +might +be +up to'
                            ' +(?P<ebgp_multihop_max_hop>[0-9]+) +hops +away$')
        p13 = re.compile(r'^\s*TCP +MD5 +authentication +is'
                            ' +(?P<tcp_md5_auth>[a-zA-Z\(\)\s]+)$')
        p14 = re.compile(r'^\s*Only +passive +connection +setup +allowed$')
        p15 = re.compile(r'^\s*Received +(?P<received_messages>[0-9]+)'
                            ' +messages, +(?P<received_notifications>[0-9]+)'
                            ' +notifications, +(?P<received_bytes>[0-9]+)'
                            ' +bytes +in +queue$')
        p16 = re.compile(r'^\s*Sent +(?P<sent_messages>[0-9]+)'
                            ' +messages, +(?P<sent_notifications>[0-9]+)'
                            ' +notifications, +(?P<sent_bytes_queue>[0-9]+)'
                            ' +bytes +in +queue$')
        p17 = re.compile(r'^\s*Connections +established'
                            ' +(?P<esablished>[0-9]+), +dropped'
                            ' +(?P<dropped>[0-9]+)$')
        p17_1 = re.compile(r'^\s*Connections +attempts'
                            ' +(?P<attemps>[0-9]+)$')
        p18 = re.compile(r'^\s*Last +reset +by (?P<reset_by>[a-zA-Z]+)'
                            ' +(?P<last_reset>[a-zA-Z0-9\:\s]+), +due +to'
                            ' +(?P<reset_reason>[a-zA-Z\-\s]+)$')
        p19 = re.compile(r'^\s*Neighbor +capabilities *:$')
        p20_1 = re.compile(r'^\s*Dynamic +capability *:'
                            ' +(?P<dynamic_capability>[a-zA-Z\,\(\)\s]+)$')
        p20_2 = re.compile(r'^\s*Dynamic +capability +\(old\) *:'
                            ' +(?P<dynamic_capability_old>[a-zA-Z\s]+)$')
        p21 = re.compile(r'^\s*Route +refresh +capability +\(new\) *:'
                            ' +(?P<route_refresh>[a-zA-Z\s]+)$')
        p21_1 = re.compile(r'^\s*Route +refresh +capability +\(old\) *:'
                            ' +(?P<route_refresh_old>[a-zA-Z\s]+)$')
        p22 = re.compile(r'^\s*4-Byte AS capability: +(?P<capability>[\w\s]+)$')
        p23 = re.compile(r'^\s*Address +family +VPNv4 +Unicast *:'
                            ' +(?P<vpnv4_unicast>[a-zA-Z\s]+)$')
        p24 = re.compile(r'^\s*Address +family +VPNv6 +Unicast *:'
                            ' +(?P<vpnv6_unicast>[a-zA-Z\s]+)$')
        p24_1 = re.compile(r'^\s*Address +family +IPv4 +MVPN:'
                            ' +(?P<ipv4_mvpn>[\w\s]+)$')
        p25 = re.compile(r'^\s*Graceful +Restart +capability *:'
                            ' +(?P<graceful_restart>[a-zA-Z\s]+)$')
        p26 = re.compile(r'^\s*Graceful +Restart +Parameters *:$')
        p27_1 = re.compile(r'^\s*$')
        p27_2 = re.compile(r'^\s*$')
        p28_1 = re.compile(r'^\s*Restart +time +advertised +to +peer *:'
                            ' +(?P<time>[0-9]+) +seconds$')
        p28_2 = re.compile(r'^\s*Restart +time +advertised +by +peer *:'
                            ' +(?P<time>[0-9]+) +seconds$')
        p28 = re.compile(r'^\s*Stale +time +for +routes +advertised +by'
                            ' +peer *: +(?P<time>[0-9]+) +seconds$')
        p30 = re.compile(r'^\s*(?P<message_stat>[a-zA-Z\s]+) *:'
                            ' +(?P<sent>[0-9]+) +(?P<received>[0-9]+)$')
        p31 = re.compile(r'^\s*For +address +family *:'
                            ' +(?P<af>[a-zA-Z0-9\s]+)$')
        p32 = re.compile(r'^\s*BGP +table +version'
                            ' +(?P<af_bgp_table_version>[0-9]+), +neighbor'
                            ' +version +(?P<nbr_version>[0-9]+)$')
        p33 = re.compile(r'^\s*(?P<accepted_paths>[0-9]+) +accepted'
                            ' +paths +consume +(?P<bytes_consumed>[0-9]+)'
                            ' +bytes +of +memory$')
        p34 = re.compile(r'^\s*(?P<num_sent_paths>[0-9]+) +sent +paths$')
        p35 = re.compile(r'^\s*Community +attribute +sent +to +this'
                            ' +neighbor$')
        p36 = re.compile(r'^\s*Extended +community +attribute +sent +to'
                            ' +this +neighbor$')
        p37 = re.compile(r'^\s*Maximum +prefixes +allowed +(?P<num>[0-9]+)$')
        p38 = re.compile(r'^\s*Inbound +route-map +configured +is'
                            ' +(?P<route_map_name_in>(\S+)), +handle'
                            ' +obtained$')
        p39 = re.compile(r'^\s*Outbound +route-map +configured +is'
                            ' +(?P<route_map_name_out>(\S+)), +handle'
                            ' +obtained$')
        p40 = re.compile(r'^\s*Third-party +Nexthop +will +not +be'
                            ' +computed.$')
        p41 = re.compile(r'^\s*SOO +Extcommunity *:'
                            ' +(?P<soo>[a-zA-Z0-9\:]+)$')
        p42 = re.compile(r'^\s*Inbound +soft +reconfiguration +allowed$')
        p43 = re.compile(r'\s*Nexthop(?: +always)? +set +to +local +peering'
                            ' +address, +(?P<ip>[\w\.\:]+)$')
        p44 = re.compile(r'^\s*Allow +my +ASN +(?P<num>[0-9]+) +times$')
        p45 = re.compile(r'^\s*ASN override is enabled$')
        p46 = re.compile(r'^\s*Default +information +originate,'
                            '(?: +route-map +(?P<route_map>(\S+)),)?'
                            ' +default(?: +not)? +sent$')
        p48 = re.compile(r'^\s*(?P<inherit_peer_seq>[0-9]+)'
                            ' +(?P<policy_name>[a-zA-Z0-9\-\_]+)$')
        p49 = re.compile(r'^\s*Local +host *: +(?P<local_host>[0-9\.\:]+),'
                            ' +Local +port *: +(?P<local_port>[0-9]+)$')
        p50 = re.compile(r'^\s*Foreign +host *:'
                            ' +(?P<foreign_host>[0-9\.\:]+), +Foreign'
                            ' +port *: +(?P<foreign_port>[0-9]+)$')
        p51 = re.compile(r'^\s*fd += +(?P<fd>[0-9]+)$')
        p52 = re.compile(r'^\s*Route reflector client$')
            
        for line in out.splitlines():
            line = line.rstrip()

            # BGP neighbor is 10.16.2.2,  remote AS 100, ibgp link,  Peer index 1
            # BGP neighbor is 10.16.2.5,  remote AS 200, local AS 333, ebgp link,  Peer index 2
            # BGP neighbor is 10.186.0.4, remote AS 1, ibgp link, fabric-internal, Peer index 2
            m = p1.match(line)
            if m:
                standard_send_community = False
                if 'neighbor' not in parsed_dict:
                    parsed_dict['neighbor'] = {}
                neighbor_id = str(m.groupdict()['neighbor_id'])
                if neighbor_id not in parsed_dict['neighbor']:
                    parsed_dict['neighbor'][neighbor_id] = {}
                    remote_as = m.groupdict()['remote_as']
                    peer_fab_type = m.groupdict()['peer_fab_type']
                    if remote_as != None:
                        parsed_dict['neighbor'][neighbor_id]['remote_as'] = \
                            int(m.groupdict()['remote_as'])
                    if peer_fab_type != None:
                        parsed_dict['neighbor'][neighbor_id]['peer_fab_type'] = \
                            peer_fab_type
                    parsed_dict['neighbor'][neighbor_id]['local_as'] = \
                        str(m.groupdict()['local_as'])
                    parsed_dict['neighbor'][neighbor_id]['link'] = \
                        str(m.groupdict()['link'])
                    parsed_dict['neighbor'][neighbor_id]['peer_index'] = \
                        int(m.groupdict()['peer_index'])
                    continue

            # Description: nei_desc
            m = p2.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['description'] = \
                        str(m.groupdict()['description'])
                continue

            # BGP version 4, remote router ID 10.16.2.2
            m = p3.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['bgp_version'] = \
                        int(m.groupdict()['bgp_version'])
                parsed_dict['neighbor'][neighbor_id]['router_id'] = \
                        str(m.groupdict()['router_id'])
                continue

            # BGP state = Established, up for 5w0d
            # BGP state = Idle, down for 4w6d, retry in 0.000000
            # BGP state = Shut (Admin), down for 5w0d
            # BGP state = Idle (Update-source i/f down/unresolved), down for 00:01:24
            m = p4.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['session_state'] = \
                        str(m.groupdict()['session_state']).lower()
                if m.groupdict()['reason']:
                    parsed_dict['neighbor'][neighbor_id]['state_reason'] = \
                        str(m.groupdict()['reason']).lower()
                parsed_dict['neighbor'][neighbor_id]['up_time'] = \
                        str(m.groupdict()['up_time'])
                parsed_dict['neighbor'][neighbor_id]['retry_time'] = \
                        str(m.groupdict()['retry_time'])
                session_state = str(m.groupdict()['session_state'])
                if 'Shut' in session_state or 'shut' in session_state:
                    parsed_dict['neighbor'][neighbor_id]['shutdown'] = True
                else:
                    parsed_dict['neighbor'][neighbor_id]['shutdown'] = False
                    continue

            # Using loopback0 as update source for this peer
            m = p5.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['update_source'] = \
                        str(m.groupdict()['update_source'])
                continue

            # BFD live-detection is configured
            # BFD live-detection is configured and enabled, state is Up
            m = p6.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['bfd_live_detection'] = \
                    True
                if m.groupdict()['bfd_enabled'] and \
                   m.groupdict()['bfd_enabled'].lower() == 'enabled':
                    parsed_dict['neighbor'][neighbor_id]['bfd_enabled'] = True
                if m.groupdict()['bfd_state']:
                    parsed_dict['neighbor'][neighbor_id]['bfd_state'] = \
                        m.groupdict()['bfd_state'].lower()
                continue

            # Neighbor local-as command not active
            m = p7.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['nbr_local_as_cmd'] = \
                        str(m.groupdict()['nbr_local_as_cmd'])
                continue

            # Last read 00:00:24, hold time = 99, keepalive interval is 33 seconds
            # Last read never, hold time = 180, keepalive interval is 60 seconds
            # Last read never, hold time = 45, keepalive interval is 15 seconds
            m = p8.match(line)
            if m:
                if 'bgp_negotiated_keepalive_timers' not in \
                    parsed_dict['neighbor'][neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_negotiated_keepalive_timers'] = {}
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_keepalive_timers']['last_read'] = \
                        str(m.groupdict()['last_read'])
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_keepalive_timers']['keepalive_interval'] = \
                        int(m.groupdict()['keepalive_interval'])
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_keepalive_timers']['hold_time'] = \
                        int(m.groupdict()['holdtime'])
                continue

            # Last written 00:00:02, keepalive timer expiry due 00:00:30
            # Last written never, keepalive timer not running
            m = p9.match(line)
            if m:
                if 'bgp_negotiated_keepalive_timers' not in \
                    parsed_dict['neighbor'][neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_negotiated_keepalive_timers'] = {}
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_keepalive_timers']['last_written'] = \
                        str(m.groupdict()['last_written'])
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_keepalive_timers']['keepalive_timer'] = \
                        str(m.groupdict()['keepalive_timer'])
                continue

            # Inherits session configuration from session-template PEER-SESSION
            m = p10.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['inherit_peer_session'] = \
                    str(m.groupdict()['template'])
                continue

            # Connected check is disabled
            m = p11.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['disable_connected_check'] = True
                continue

            # Private AS numbers removed from updates sent to this neighbor
            m = p11_2.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['remove_private_as'] = True
                continue

            # External BGP peer might be upto 255 hops away
            m = p12_1.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['ebgp_multihop'] = True
                parsed_dict['neighbor'][neighbor_id]['ebgp_multihop_max_hop'] =\
                    int(m.groupdict()['ebgp_multihop_max_hop'])
                continue

            # External BGP peer might be up to 5 hops away
            m = p12_2.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['ebgp_multihop'] = True
                parsed_dict['neighbor'][neighbor_id]['ebgp_multihop_max_hop'] =\
                    int(m.groupdict()['ebgp_multihop_max_hop'])
                continue

            # TCP MD5 authentication is enabled
            # TCP MD5 authentication is set (disabled)
            m = p13.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['tcp_md5_auth'] = \
                    str(m.groupdict()['tcp_md5_auth'])
                parsed_dict['neighbor'][neighbor_id]['tcp_md5_auth_config'] = \
                    str(line).strip()
                continue
            
            # Only passive connection setup allowed
            m = p14.match(line)
            if m:
                if 'bgp_session_transport' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport'] = {}
                if 'connection' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_session_transport']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['connection'] = {}
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['connection']['mode'] = 'passive'
                continue

            # Received 92717 messages, 3 notifications, 0 bytes in queue
            m = p15.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['received_messages'] = \
                    int(m.groupdict()['received_messages'])
                parsed_dict['neighbor'][neighbor_id]['received_notifications'] = \
                    int(m.groupdict()['received_notifications'])
                parsed_dict['neighbor'][neighbor_id]['received_bytes_queue'] = \
                    int(m.groupdict()['received_bytes'])
                continue

            # Sent 92730 messages, 5 notifications, 0 bytes in queue
            m = p16.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['sent_messages'] = \
                    int(m.groupdict()['sent_messages'])
                parsed_dict['neighbor'][neighbor_id]['sent_notifications'] = \
                    int(m.groupdict()['sent_notifications'])
                parsed_dict['neighbor'][neighbor_id]['sent_bytes_queue'] = \
                    int(m.groupdict()['sent_bytes_queue'])
                continue

            # Connections established 9, dropped 8
            m = p17.match(line)
            if m:
                if 'bgp_session_transport' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport'] = {}
                if 'connection' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_session_transport']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['connection'] = {}
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['connection']['established'] = \
                        int(m.groupdict()['esablished'])
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['connection']['dropped'] = int(m.groupdict()['dropped'])
                continue

            # Connections attempts 0
            m = p17.match(line)
            if m:
                if 'bgp_session_transport' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport'] = {}
                if 'connection' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_session_transport']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['connection'] = {}
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['connection']['attemps'] = int(m.groupdict()['attemps'])
                continue

            # Last reset by us 5w0d, due to session cleared
            # Last reset by peer 5w0d, due to session cleared
            # Last reset by us never, due to No error
            m = p18.match(line)
            if m:
                if 'bgp_session_transport' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport'] = {}
                if 'connection' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_session_transport']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['connection'] = {}
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['connection']['last_reset'] = \
                        str(m.groupdict()['last_reset']).lower()
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['connection']['reset_reason'] = \
                        str(m.groupdict()['reset_reason']).lower()
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['connection']['reset_by'] = \
                        str(m.groupdict()['reset_by']).lower()
                continue

            # Neighbor capabilities:
            m = p19.match(line)
            if m:
                if 'bgp_negotiated_capabilities' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_negotiated_capabilities'] = {}
                continue

            # Dynamic capability: advertised (mp, refresh, gr) received (mp, refresh, gr)
            m = p20_1.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['dynamic_capability'] = \
                        str(m.groupdict()['dynamic_capability'])
                continue

            # Dynamic capability (old): advertised received
            m = p20_2.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['dynamic_capability_old'] = \
                        str(m.groupdict()['dynamic_capability_old'])
                continue

            # Route refresh capability (new): advertised received
            m = p21.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['route_refresh'] = \
                        str(m.groupdict()['route_refresh'])
                continue

            # Route refresh capability (old): advertised received 
            m = p21_1.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['route_refresh_old'] = \
                        str(m.groupdict()['route_refresh_old'])
                continue

            # 4-Byte AS capability: disabled
            # 4-Byte AS capability: disabled received
            m = p22.match(line)
            if m:
                if 'disabled' in m.groupdict()['capability']:
                    parsed_dict['neighbor'][neighbor_id]['suppress_four_byte_as_capability'] = True
                continue

            # Address family VPNv4 Unicast: advertised received
            m = p23.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['vpnv4_unicast'] = \
                        str(m.groupdict()['vpnv4_unicast'])
                continue

            # Address family VPNv6 Unicast: advertised received 
            m = p24.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['vpnv6_unicast'] = \
                        str(m.groupdict()['vpnv6_unicast'])
                continue

            # Address family IPv4 MVPN: advertised received
            m = p24_1.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id] \
                    ['bgp_negotiated_capabilities']['ipv4_mvpn'] = \
                    str(m.groupdict()['ipv4_mvpn'])
                continue

            # Graceful Restart capability: advertised received
            m = p25.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['graceful_restart'] = \
                        str(m.groupdict()['graceful_restart'])
                continue

            # Graceful Restart Parameters:
            m = p26.match(line)
            if m:
                if 'graceful_restart_paramters' not in \
                    parsed_dict['neighbor'][neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['graceful_restart_paramters'] = {}
                    continue

            # Address families advertised to peer:
            # VPNv4 Unicast  VPNv6 Unicast 
            m = p27_1.match(line)
            if m:
                continue

            # Address families received from peer:
            # VPNv4 Unicast  VPNv6 Unicast  
            m = p27_2.match(line)
            if m:
                continue

            # Forwarding state preserved by peer for:
            # Restart time advertised to peer: 240 seconds
            m = p28_1.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['graceful_restart_paramters']\
                        ['restart_time_advertised_to_peer_seconds'] = \
                            int(m.groupdict()['time'])
                continue

            # Restart time advertised by peer: 120 seconds
            m = p28_2.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['graceful_restart_paramters']\
                        ['restart_time_advertised_by_peer_seconds'] = \
                            int(m.groupdict()['time'])
                continue

            # Stale time for routes advertised by peer: 600 seconds
            m = p28.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]\
                    ['graceful_restart_paramters']\
                        ['stale_time_advertised_by_peer_seconds'] = \
                            int(m.groupdict()['time'])
                continue

            # Message statistics:
            #                         Sent               Rcvd
            # Opens:                         9                  9  
            # Notifications:                 5                  3  
            # Updates:                      50                 38  
            # Keepalives:                92663              92661  
            # Route Refresh:                 2                  5  
            # Capability:                    1                  1  
            # Total:                     92730              92717  
            # Total bytes:             1763812            1763099  
            # Bytes in queue:                0                  0
            m = p30.match(line)
            if m:
                if 'bgp_neighbor_counters' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_neighbor_counters'] = {}
                if 'messages' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_neighbor_counters']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_neighbor_counters']['messages'] = {}
                if 'sent' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_neighbor_counters']['messages']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_neighbor_counters']['messages']['sent'] = {}
                if 'received' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_neighbor_counters']['messages']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_neighbor_counters']['messages']['received'] = {}
                message_stat = str(m.groupdict()['message_stat']).lower()
                message_stat = message_stat.replace(" ", "_")
                sent = int(m.groupdict()['sent'])
                received = int(m.groupdict()['received'])
                if message_stat not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_neighbor_counters']['messages']['sent']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_neighbor_counters']['messages']['sent']\
                        [message_stat] = sent
                if message_stat not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_neighbor_counters']['messages']['received']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_neighbor_counters']['messages']['received']\
                        [message_stat] = received
                continue

            # For address family: VPNv4 Unicast
            m = p31.match(line)
            if m:
                if 'address_family' not in  parsed_dict['neighbor'][neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]['address_family'] = {}
                address_family = str(m.groupdict()['af']).lower()
                
                if address_family not in parsed_dict['neighbor'][neighbor_id]\
                    ['address_family']:
                    parsed_dict['neighbor'][neighbor_id]['address_family']\
                        [address_family] = {}
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['session_state'] = session_state.lower()
                if 'state_reason' in parsed_dict['neighbor'][neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['state_reason'] = \
                        parsed_dict['neighbor'][neighbor_id]['state_reason']
                continue

            # BGP table version 48, neighbor version 48
            m = p32.match(line)
            if m:
                standard_send_community = False
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['bgp_table_version'] = \
                        int(m.groupdict()['af_bgp_table_version'])
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['neighbor_version'] = \
                        int(m.groupdict()['nbr_version'])
                continue

            # 1 accepted paths consume 48 bytes of memory
            m = p33.match(line)
            if m:
                if 'path' not in parsed_dict['neighbor'][neighbor_id]\
                    ['address_family'][address_family]:
                    parsed_dict['neighbor'][neighbor_id]['address_family']\
                        [address_family]['path'] = {}
                accepted_paths = int(m.groupdict()['accepted_paths'])
                memory_usage = int(m.groupdict()['bytes_consumed'])
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['path']['accepted_paths'] = accepted_paths
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['path']['memory_usage'] = memory_usage
                continue

            # 2 sent paths
            m = p34.match(line)
            if m:
                if 'path' not in parsed_dict['neighbor'][neighbor_id]\
                    ['address_family'][address_family]:
                    parsed_dict['neighbor'][neighbor_id]['address_family']\
                        [address_family]['path'] = {}
                total_entries = int(m.groupdict()['num_sent_paths'])
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['path']['total_entries'] = total_entries
                continue
            
            # Community attribute sent to this neighbor
            m = p35.match(line)
            if m:
                standard_send_community = True
                parsed_dict['neighbor'][neighbor_id]['address_family'] \
                    [address_family]['send_community'] = 'standard'
                continue

            # Extended community attribute sent to this neighbor
            m = p36.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family'] \
                    [address_family]['send_community'] = 'extended'

                if standard_send_community:
                    parsed_dict['neighbor'][neighbor_id]['address_family'] \
                        [address_family]['send_community'] = 'both'
                continue

            # Maximum prefixes allowed 300000
            m = p37.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['maximum_prefix_max_prefix_no'] = \
                        int(m.groupdict()['num'])
                continue

            # Inbound route-map configured is genie_redistribution, handle obtained
            m = p38.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['route_map_name_in'] = \
                        str(m.groupdict()['route_map_name_in'])
                continue

            # Outbound route-map configured is genie_redistribution, handle obtained
            m = p39.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['route_map_name_out'] = \
                        str(m.groupdict()['route_map_name_out'])
                continue

            # Third-party Nexthop will not be computed.
            m = p40.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['third_party_nexthop'] = True
                continue
            
            # SOO Extcommunity: SOO:100:100
            m = p41.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['soo'] = str(m.groupdict()['soo'])
                continue

            # Inbound soft reconfiguration allowed
            m = p42.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['soft_configuration'] = True
                continue

            # Nexthop always set to local peering address, 0.0.0.0
            # Nexthop set to local peering address, 0.0.0.0
            m = p43.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['next_hop_self'] = True
                continue

            # Allow my ASN 9 times
            m = p44.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['as_override_count'] = \
                        int(m.groupdict()['num'])
                continue

            # ASN override is enabled
            m = p45.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['as_override'] = True
                continue

            # Default information originate, default not sent
            # Default information originate, default sent
            # Default information originate, route-map SOMENAME, default not sent
            m = p46.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['default_originate'] = True
                if m.groupdict()['route_map']:
                    parsed_dict['neighbor'][neighbor_id]['address_family']\
                        [address_family]['default_originate_route_map'] = \
                            m.groupdict()['route_map']
                continue

            # Inherited policy-templates:
            # Preference    Name
            #         10    PEER-POLICY                                                 
            #         20    PEER-POLICY2
            m = p48.match(line)
            if m:
                policy_name = str(m.groupdict()['policy_name'])
                inherit_peer_seq = int(m.groupdict()['inherit_peer_seq'])
                if 'inherit_peer_policy' not in parsed_dict['neighbor']\
                    [neighbor_id]['address_family'][address_family]:
                    parsed_dict['neighbor'][neighbor_id]['address_family']\
                        [address_family]['inherit_peer_policy'] = {}
                if policy_name not in parsed_dict['neighbor'][neighbor_id]\
                    ['address_family'][address_family]\
                        ['inherit_peer_policy']:
                    parsed_dict['neighbor'][neighbor_id]['address_family']\
                        [address_family]['inherit_peer_policy']\
                        [policy_name] = {}
                    parsed_dict['neighbor'][neighbor_id]['address_family']\
                        [address_family]['inherit_peer_policy']\
                        [policy_name]['inherit_peer_seq'] = inherit_peer_seq
                    continue

            # Local host: 10.4.1.1, Local port: 179
            m = p49.match(line)
            if m:
                if 'bgp_session_transport' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport'] = {}
                if 'transport' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_session_transport']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['transport'] = {}
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['transport']['local_host'] = \
                        str(m.groupdict()['local_host'])
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['transport']['local_port'] = \
                        str(m.groupdict()['local_port'])
                continue

            # Foreign host: 10.16.2.2, Foreign port: 4466
            m = p50.match(line)
            if m:
                if 'bgp_session_transport' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport'] = {}
                if 'transport' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_session_transport']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['transport'] = {}
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['transport']['foreign_host'] = \
                        str(m.groupdict()['foreign_host'])
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['transport']['foreign_port'] = \
                        str(m.groupdict()['foreign_port'])
                continue
            
            # fd = 44
            m = p51.match(line)
            if m:
                if 'bgp_session_transport' not in parsed_dict['neighbor']\
                    [neighbor_id]:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport'] = {}
                if 'transport' not in parsed_dict['neighbor'][neighbor_id]\
                    ['bgp_session_transport']:
                    parsed_dict['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['transport'] = {}
                parsed_dict['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['transport']['fd'] = str(m.groupdict()['fd'])
                continue

            # Route reflector client
            m = p52.match(line)
            if m:
                parsed_dict['neighbor'][neighbor_id]['address_family']\
                    [address_family]['route_reflector_client'] = True
                continue

        return parsed_dict

    def yang(self, vrf, address_family='', neighbor=''):
        # Initialize empty dictionary
        map_dict = {}

        # Execute YANG 'get' operational state RPC and parse the XML
        bgpOC = BgpOpenconfigYang(self.device)
        yang_dict = bgpOC.yang()

        if 'vrf' in yang_dict:
            for vrf_name in yang_dict['vrf']:
                if vrf_name == vrf:
                    if 'neighbor' in yang_dict['vrf'][vrf_name]:
                        for neighbor in yang_dict['vrf'][vrf_name]['neighbor']:
                            if 'neighbor' not in map_dict:
                                map_dict['neighbor'] = {}
                            if neighbor not in map_dict['neighbor']:
                                map_dict['neighbor'][neighbor] = {}
                            for key in yang_dict['vrf'][vrf_name]['neighbor'][neighbor]:
                                if key == 'ebgp_multihop':
                                    map_dict['neighbor'][neighbor]['link'] = 'ebgp'
                                map_dict['neighbor'][neighbor][key] = \
                                    yang_dict['vrf'][vrf_name]['neighbor'][neighbor][key]
                                continue

        # Return to caller
        return map_dict


# ==================================================
# Schema for 'show bgp vrf all all nexthop-database'
# ==================================================
class ShowBgpVrfAllAllNextHopDatabaseSchema(MetaParser):
    """Schema for show bgp vrf all all nexthop-database"""

    schema = {
        'vrf': 
            {Any():
                {'address_family':
                    {Any():
                        {'af_nexthop_trigger_enable': bool,
                         'nexthop_trigger_delay_critical': int,
                         'nexthop_trigger_delay_non_critical': int,
                         Optional('next_hop'): {
                            Any(): {                                
                                 Optional('refcount'): int,
                                 Optional('flags'): str,
                                 Optional('multipath'): str,
                                 Optional('igp_cost'): int,
                                 Optional('igp_route_type'): int,
                                 Optional('igp_preference'): int,
                                 Optional('attached'): bool,
                                 Optional('local'): bool,
                                 Optional('reachable'): bool,
                                 Optional('labeled'): bool,
                                 Optional('filtered'): bool,
                                 Optional('pending_update'): bool,
                                 Optional('resolve_time'): str,
                                 Optional('rib_route'): str,
                                 Optional('metric_next_advertise'): str,
                                 Optional('rnh_epoch'): int,
                                 Optional('attached_nexthop'): {
                                    Any(): {
                                        'attached_nexthop_interface': str,
                                        },
                                    },
                                },
                            }
                         }
                        },
                    },
                },
            }

# ==================================================
# Parser for 'show bgp vrf all all nexthop-database'
# ==================================================
class ShowBgpVrfAllAllNextHopDatabase(ShowBgpVrfAllAllNextHopDatabaseSchema):
    """Parser for show bgp vrf all all nexthop-database"""

    cli_command = ['show bgp vrf all all nexthop-database', 'show bgp vrf {vrf} {address_family} nexthop-database']
    exclude = [
      'nexthop_last_resolved',
      'rnh_epoch',
      'metric_next_advertise',
      'resolve_time',
      'flags',
      'rib_route',
      'refcount']

    def cli(self, vrf='all', address_family='all', cmd = "", output=None):
        if output is None:
            if not cmd:
                if address_family != 'all' or vrf != 'all':
                    cmd = self.cli_command[1].format(vrf=vrf, address_family=address_family)
                else:
                    cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output
        
        # Init vars
        nh_dict = {}

        p1 = re.compile(r'^\s*Next +Hop +table +for +VRF'
                            ' +(?P<vrf_name>\S+), +address +family'
                            ' +(?P<af>[a-zA-Z0-9\s\-]+) *:$')
        p2 = re.compile(r'^\s*Critical *:'
                            ' +(?P<nexthop_trigger_delay_critical>[0-9]+)'
                            ' +Non-critical *:'
                            ' +(?P<nexthop_trigger_delay_non_critical>[0-9]+)$')
        p3 = re.compile(r'^\s*Nexthop *: +(?P<nh>[a-zA-Z0-9\.\:]+),'
                            '( +Flags *: +(?P<flags>\w+),)?'
                            ' +Refcount *: +(?P<refcount>[0-9]+), +IGP'
                            ' +cost *: +(?P<igp_cost>[0-9\-]+)'
                            '(?:, +Multipath: +(?P<multipath>(\S+)))?$')
        p4 = re.compile(r'^\s*IGP +Route +type *:'
                            ' +(?P<igp_route_type>[0-9]+), +IGP +preference *:'
                            ' +(?P<igp_preference>[0-9]+)$')
        p5 = re.compile(r'^\s*Nexthop +is +(?P<attached>[\w\-]+) +'
                            '(?P<local>[\w\-]+) +(?P<reachable>[\w\-]+) +'
                            '(?P<labeled>[\w\-]+)$')
        p6 = re.compile(r'^\s*Nexthop +last +resolved *:'
                            ' +(?P<nexthop_last_resolved>[a-zA-Z0-9\:\.\s]+),'
                            ' +using +(?P<nexthop_resolved_using>[\w\:\-\.\/]+)$')
        p7 = re.compile(r'^\s*Metric +next +advertise *:'
                            ' +(?P<metric_next_advertise>[a-zA-Z0-9\:]+)$')
        p8 = re.compile(r'^\s*RNH +epoch *: +(?P<rnh_epoch>[0-9]+)$')
        p9 = re.compile(r'^\s*Attached +nexthop *:'
                            ' +(?P<attached_nexthop>[\w\.\:]+), +Interface *:'
                            ' +(?P<attached_nexthop_interface>[\w\-\.\/]+)$')
        for line in out.splitlines():
            line = line.rstrip()

            # Next Hop table for VRF VRF1, address family IPv4 Unicast:
            # Next Hop table for VRF Tenant-1, address family IPv6 Unicast:
            m = p1.match(line)
            if m:
                if 'vrf' not in nh_dict:
                    nh_dict['vrf'] = {}
                vrf = str(m.groupdict()['vrf_name'])
                if vrf not in nh_dict['vrf']:
                    nh_dict['vrf'][vrf] = {}
                if 'address_family' not in nh_dict['vrf'][vrf]:
                    nh_dict['vrf'][vrf]['address_family'] = {}
                af = str(m.groupdict()['af']).lower()

                if af not in nh_dict['vrf'][vrf]['address_family']:
                    nh_dict['vrf'][vrf]['address_family'][af] = {}
                    af_dict = nh_dict['vrf'][vrf]['address_family'][af]
                    af_dict['af_nexthop_trigger_enable'] = True
                    continue

            # Next-hop trigger-delay(miliseconds)
            # Critical: 2222 Non-critical: 3333
            m = p2.match(line)
            if m:
                af_dict['nexthop_trigger_delay_critical'] = \
                    int(m.groupdict()['nexthop_trigger_delay_critical'])
                af_dict['nexthop_trigger_delay_non_critical'] = \
                    int(m.groupdict()['nexthop_trigger_delay_non_critical'])
                continue

            # Nexthop: 0.0.0.0, Refcount: 4, IGP cost: 0
            # Nexthop: 192.168.154.1, Flags: 0x41, Refcount: 1, IGP cost: 3
            # Nexthop: 2001:db8:1900:1::1:101, Flags: 0x5, Refcount: 3, IGP cost: 0, Multipath: No
            m = p3.match(line)
            if m:
                nexthop = m.groupdict()['nh']
                if 'next_hop' not in af_dict:
                    af_dict['next_hop'] = {}
                if nexthop not in af_dict['next_hop']:
                    af_dict['next_hop'][nexthop] = {}

                af_dict['next_hop'][nexthop]['refcount'] = int(m.groupdict()['refcount'])
                af_dict['next_hop'][nexthop]['igp_cost'] = int(m.groupdict()['igp_cost'])
                if m.groupdict()['flags']:
                    af_dict['next_hop'][nexthop]['flags'] = m.groupdict()['flags']
                if m.groupdict()['multipath']:
                    af_dict['next_hop'][nexthop]['multipath'] = m.groupdict()['multipath']
                continue

            # IGP Route type: 0, IGP preference: 0
            m = p4.match(line)
            if m:
                af_dict['next_hop'][nexthop]['igp_route_type'] = int(m.groupdict()['igp_route_type'])
                af_dict['next_hop'][nexthop]['igp_preference'] = int(m.groupdict()['igp_preference'])
                continue

            # Nexthop is not-attached local unreachable not-labeled
            # Nexthop is not-attached not-local reachable labeled
            m = p5.match(line)
            if m:
                if m.groupdict()['attached'] == 'not-attached':
                    af_dict['next_hop'][nexthop]['attached'] = False
                else:
                    af_dict['next_hop'][nexthop]['attached'] = True

                if m.groupdict()['local'] == 'not-local':
                    af_dict['next_hop'][nexthop]['local'] = False
                else:
                    af_dict['next_hop'][nexthop]['local'] = True

                if m.groupdict()['reachable'] == 'unreachable':
                    af_dict['next_hop'][nexthop]['reachable'] = False
                else:
                    af_dict['next_hop'][nexthop]['reachable'] = True

                if m.groupdict()['labeled'] == 'not-labeled':
                    af_dict['next_hop'][nexthop]['labeled'] = False
                else:
                    af_dict['next_hop'][nexthop]['labeled'] = True

                af_dict['next_hop'][nexthop]['filtered'] = False
                af_dict['next_hop'][nexthop]['pending_update'] = False

                continue

            # Nexthop last resolved: never, using 0.0.0.0/0
            # Nexthop last resolved: 00:00:39, using 10.36.1.0/32
            # Nexthop last resolved: 0.596958, using 10.36.1.0/32
            m = p6.match(line)
            if m:
                af_dict['next_hop'][nexthop]['resolve_time'] = \
                    str(m.groupdict()['nexthop_last_resolved'])
                af_dict['next_hop'][nexthop]['rib_route'] = \
                    str(m.groupdict()['nexthop_resolved_using'])
                continue

            # Metric next advertise: Never
            # Metric next advertise: 00:06:11
            m = p7.match(line)
            if m:
                af_dict['next_hop'][nexthop]['metric_next_advertise'] = \
                    str(m.groupdict()['metric_next_advertise']).lower()
                continue

            # RNH epoch: 0
            m = p8.match(line)
            if m:
                af_dict['next_hop'][nexthop]['rnh_epoch'] = int(m.groupdict()['rnh_epoch'])
                continue

            # Attached nexthop: 10.1.3.3, Interface: Ethernet4/2
            m = p9.match(line)
            if m:
                if 'attached_nexthop' not in af_dict['next_hop'][nexthop]:
                    af_dict['next_hop'][nexthop]['attached_nexthop'] = {}

                at_nexthop = m.groupdict()['attached_nexthop']

                if at_nexthop not in af_dict['next_hop'][nexthop]['attached_nexthop']:
                    af_dict['next_hop'][nexthop]['attached_nexthop'][at_nexthop] = {}
                af_dict['next_hop'][nexthop]['attached_nexthop'][at_nexthop]\
                    ['attached_nexthop_interface'] = \
                        m.groupdict()['attached_nexthop_interface']
                continue

        return nh_dict


# =========================================
# Schema for 'show bgp vrf <WORD> all summary'
# =========================================
class ShowBgpVrfAllAllSummarySchema(MetaParser):
    """Schema for show bgp vrf <WORD> all summary"""

    schema = {
        'vrf':
            {Any():
                {Optional('neighbor'):
                    {Any():
                        {'address_family':
                            {Any():
                                {'neighbor_table_version': int,
                                'as': Or(int,float),
                                'msg_rcvd': int,
                                'msg_sent': int,
                                'tbl_ver': int,
                                'inq': int,
                                'outq': int,
                                'up_down': str,
                                'state_pfxrcd': str,
                                'state': str,
                                Optional('prefix_received'): str,
                                Optional('route_identifier'): str,
                                Optional('local_as'): int,
                                Optional('bgp_table_version'): int,
                                Optional('config_peers'): int,
                                Optional('capable_peers'): int,
                                Optional('prefixes'):
                                    {'total_entries': int,
                                    'memory_usage': int,
                                },
                                Optional('path'):
                                    {'total_entries': int,
                                    'memory_usage': int,
                                },
                                Optional('attribute_entries'): str,
                                Optional('as_path_entries'): str,
                                Optional('community_entries'): str,
                                Optional('clusterlist_entries'): str,
                                Optional('dampening'): bool,
                                Optional('history_paths'): int,
                                Optional('dampened_paths'): int,
                                Optional('soft_reconfig_recvd_paths'): int,
                                Optional('soft_reconfig_identical_paths'): int,
                                Optional('soft_reconfig_combo_paths'): int,
                                Optional('soft_reconfig_filtered_recvd'): int,
                                Optional('soft_reconfig_bytes'): int
                                },
                            },
                        },
                    },
                },
            },
        }

# =========================================
# Parser for 'show bgp vrf <WORD> all summary'
# =========================================
class ShowBgpVrfAllAllSummary(ShowBgpVrfAllAllSummarySchema):
    """Parser for show bgp vrf <WORD> all summary"""

    cli_command = [ 'show bgp vrf all all summary',
                    'show bgp vrf {vrf} all summary',
                    'show bgp vrf {vrf} {address_family} summary']

    xml_command = 'show bgp vrf {vrf} all summary | xml'
    exclude = [
      'tbl_ver',
      'up_down',
      'bgp_table_version',
      'state_pfxrcd',
      'memory_usage',
      'msg_rcvd',
      'msg_sent',
      'nexthop_last_resolved',
      'attribute_entries',
      'route_identifier',
      'clusterlist_entries',
      'total_entries',
      'as_path_entries']

    def cli(self, vrf='all', address_family='all', output=None):
        if output is None:
            if address_family == 'all':
                if vrf == 'all':
                    out = self.device.execute(self.cli_command[0])

                else:
                    out = self.device.execute(self.cli_command[1].format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[2].format(vrf=vrf,
                                                                     address_family=address_family))
        else:
            out = output
        
        # Init vars
        sum_dict = {}
        data_on_nextline = False
        p1 = re.compile(r'^\s*BGP +summary +information +for +VRF'
                            ' +(?P<vrf_name>\S+), +address +family'
                            ' +(?P<address_family>[a-zA-Z0-9\s\-\_]+)$')
        p2 = re.compile(r'^\s*BGP +router +identifier'
                            ' +(?P<route_identifier>[0-9\.\:]+), +local +AS'
                            ' +number +(?P<local_as>[0-9]+)$')
        p3 = re.compile(r'^\s*BGP +table +version +is'
                            ' +(?P<bgp_table_version>[0-9]+),'
                            ' +(?P<address_family>[a-zA-Z0-9\-\s]+) +config'
                            ' +peers +(?P<config_peers>[0-9]+), +capable'
                            ' +peers +(?P<capable_peers>[0-9]+)$')
        p4 = re.compile(r'^\s*(?P<networks>[0-9]+) +network +entries +and'
                            ' +(?P<paths>[0-9]+) +paths +using'
                            ' +(?P<bytes>[0-9]+) +bytes +of +memory$')
        p5 = re.compile(r'^\s*BGP +attribute +entries'
                            ' +(?P<attribute_entries>(\S+)), +BGP +AS +path'
                            ' +entries +(?P<as_path_entries>(\S+))$')
        p6 = re.compile(r'^\s*BGP +community +entries'
                            ' +(?P<community_entries>(\S+)), +BGP +clusterlist'
                            ' +entries +(?P<clusterlist_entries>(\S+))$')
        p7 = re.compile(r'^\s*Dampening +configured,'
                            ' +(?P<history_paths>[0-9]+) +history +paths,'
                            ' +(?P<dampened_paths>[0-9]+) +dampened +paths$')
        p9 = re.compile(r'^\s*(?P<val>[0-9]+) +received +paths +for +inbound +soft +reconfiguration$')
        p10 = re.compile(r'^\s*(?P<val1>[0-9]+) +identical, +'
                            '(?P<val2>[0-9]+) +modified, +'
                            '(?P<val3>[0-9]+) +filtered +received +paths +'
                            'using +(?P<val4>[0-9]+) +bytes$')
        p8 = re.compile(r'^\s*(?P<neighbor>[a-zA-Z0-9\.\:]+)\s+(?P<v>[0-9]+)'
                            '\s+(?P<as>[0-9.]+)\s+(?P<msg_rcvd>[0-9]+)'
                            '\s+(?P<msg_sent>[0-9]+)\s+(?P<tbl_ver>[0-9]+)'
                            '\s+(?P<inq>[0-9]+)\s+(?P<outq>[0-9]+)'
                            '\s+(?P<up_down>[a-zA-Z0-9\:]+)'
                            '\s+(?P<state_pfxrcd>(?P<state>[a-zA-Z\s\(\)]+)?'
                            '\s*(?P<prx_rcd>\d+)?([\w\(\)\s]+)?)$')
        p8_1 = re.compile(r'^\s*(?P<neighbor>[a-zA-Z0-9\.\:]+)$')
        p8_2 = re.compile(r'^\s*(?P<v>[0-9]+) +(?P<as>[0-9]+)'
                            ' +(?P<msg_rcvd>[0-9]+) +(?P<msg_sent>[0-9]+)'
                            ' +(?P<tbl_ver>[0-9]+) +(?P<inq>[0-9]+)'
                            ' +(?P<outq>[0-9]+) +(?P<up_down>[a-zA-Z0-9\:]+)'
                            ' +(?P<state_pfxrcd>(?P<state>[a-zA-Z\s\(\)]+)?(?P<prx_rcd>\d+)?([\w\(\)\s]+)?)$')
        # Neighbor        V             AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        # 10.10.10.10     4 4211111111
        p8_3 = re.compile(r'^\s*(?P<neighbor>[a-zA-Z0-9\.\:]+) +(?P<v>[0-9]+) +(?P<as>[0-9]+)$')
        # Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        #                                                  0              0           0      0        0       5w6d   Idle 
        p8_4 = re.compile(r'^\s*(?P<msg_rcvd>[0-9]+) +(?P<msg_sent>[0-9]+)'
                          r' +(?P<tbl_ver>[0-9]+) +(?P<inq>[0-9]+)'
                          r' +(?P<outq>[0-9]+) +(?P<up_down>[a-zA-Z0-9\:]+)'
                          r' +(?P<state_pfxrcd>(?P<state>[a-zA-Z\s\(\)]+)?(?P<prx_rcd>\d+)?([\w\(\)\s]+)?)$')                            

        for line in out.splitlines():
            line = line.rstrip()

            # BGP summary information for VRF VRF1, address family IPv4 Unicast
            # BGP summary information for VRF core_vrf, address family IPv4 Unicast
            # BGP summary information for VRF vrf-9100, address family IPv4 Unicast
            m = p1.match(line)
            if m:
                # Save variables for use later
                address_family = str(m.groupdict()['address_family']).lower()
                vrf = str(m.groupdict()['vrf_name'])
                # Delete variables in preparation for next neighbor
                try:
                    del route_identifier; del local_as; del bgp_table_version;
                    del config_peers; del capable_peers; del attribute_entries;
                    del as_path_entries; del community_entries;
                    del clusterlist_entries; del dampening; del history_paths;
                    del dampened_paths; del soft_reconfig_recvd_paths;
                    del soft_reconfig_identical_paths; del soft_reconfig_combo_paths;
                    del soft_reconfig_filtered_recvd; del soft_reconfig_bytes
                except Exception:
                    pass

                continue

            # BGP router identifier 10.64.4.4, local AS number 100
            m = p2.match(line)
            if m:
                route_identifier = str(m.groupdict()['route_identifier'])
                local_as = int(m.groupdict()['local_as'])
                if 'vrf' not in sum_dict:
                    sum_dict['vrf'] = {}
                if vrf not in sum_dict['vrf']:
                    sum_dict['vrf'][vrf] = {}
                continue

            # BGP table version is 40, IPv4 Unicast config peers 1, capable peers 0
            m = p3.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                config_peers = int(m.groupdict()['config_peers'])
                capable_peers = int(m.groupdict()['capable_peers'])
                continue

            # 5 network entries and 5 paths using 620 bytes of memory
            m = p4.match(line)
            if m:
                num_prefix_entries = int(m.groupdict()['networks'])
                memory_usage = int(m.groupdict()['bytes'])
                num_path_entries = int(m.groupdict()['paths'])
                continue

            # BGP attribute entries [3/384], BGP AS path entries [0/0]
            m = p5.match(line)
            if m:
                attribute_entries = str(m.groupdict()['attribute_entries'])
                as_path_entries = str(m.groupdict()['as_path_entries'])
                continue

            # BGP community entries [0/0], BGP clusterlist entries [1/4]
            m = p6.match(line)
            if m:
                community_entries = str(m.groupdict()['community_entries'])
                clusterlist_entries = str(m.groupdict()['clusterlist_entries'])
                continue

            # Dampening configured, 0 history paths, 0 dampened paths
            m = p7.match(line)
            if m:
                dampening = True
                history_paths = int(m.groupdict()['history_paths'])
                dampened_paths = int(m.groupdict()['dampened_paths'])
                continue

            # 10 received paths for inbound soft reconfiguration
            m = p9.match(line)
            if m:
                soft_reconfig_recvd_paths = int(m.groupdict()['val'])
                continue

            # 10 identical, 0 modified, 0 filtered received paths using 0 bytes
            m = p10.match(line)
            if m:
                soft_reconfig_identical_paths = int(m.groupdict()['val1'])
                soft_reconfig_combo_paths = int(m.groupdict()['val2'])
                soft_reconfig_filtered_recvd = int(m.groupdict()['val3'])
                soft_reconfig_bytes = int(m.groupdict()['val4'])
                continue

            # Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            # 10.16.2.10        4     0       0       0        0    0    0     5w6d Idle 
            
            # Neighbor        V    AS    MsgRcvd    MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            # 2.2.2.2    4 1.57920      29146      29136      152    0    0 04:52:49 12   
            m = p8.match(line)
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
                nbr_af_dict['neighbor_table_version'] = int(m.groupdict()['v'])
                try:
                    nbr_af_dict['as'] = int(m.groupdict()['as'])
                except:
                    nbr_af_dict['as'] = float(m.groupdict()['as'])
                nbr_af_dict['msg_rcvd'] = int(m.groupdict()['msg_rcvd'])
                nbr_af_dict['msg_sent'] = int(m.groupdict()['msg_sent'])
                nbr_af_dict['tbl_ver'] = int(m.groupdict()['tbl_ver'])
                nbr_af_dict['inq'] = int(m.groupdict()['inq'])
                nbr_af_dict['outq'] = int(m.groupdict()['outq'])
                nbr_af_dict['up_down'] = str(m.groupdict()['up_down'])
                nbr_af_dict['state_pfxrcd'] = str(m.groupdict()['state_pfxrcd']).lower().strip()
                if m.groupdict()['state']:
                    nbr_af_dict['state'] = m.groupdict()['state_pfxrcd'].lower()
                if m.groupdict()['prx_rcd']:
                    nbr_af_dict['prefix_received'] = m.groupdict()['prx_rcd']
                    nbr_af_dict['state'] = 'established'
                try:
                    # Assign variables
                    nbr_af_dict['route_identifier'] = route_identifier
                    nbr_af_dict['local_as'] = local_as
                    nbr_af_dict['bgp_table_version'] = bgp_table_version
                    nbr_af_dict['config_peers'] = config_peers
                    nbr_af_dict['capable_peers'] = capable_peers
                    nbr_af_dict['attribute_entries'] = attribute_entries
                    nbr_af_dict['as_path_entries'] = as_path_entries
                    nbr_af_dict['community_entries'] = community_entries
                    nbr_af_dict['clusterlist_entries'] = clusterlist_entries
                    nbr_af_dict['dampening'] = dampening
                    nbr_af_dict['history_paths'] = history_paths
                    nbr_af_dict['dampened_paths'] = dampened_paths
                except Exception:
                    pass
                try:
                    nbr_af_dict['soft_reconfig_recvd_paths'] = soft_reconfig_recvd_paths
                    nbr_af_dict['soft_reconfig_identical_paths'] = soft_reconfig_identical_paths
                    nbr_af_dict['soft_reconfig_combo_paths'] = soft_reconfig_combo_paths
                    nbr_af_dict['soft_reconfig_filtered_recvd'] = soft_reconfig_filtered_recvd
                    nbr_af_dict['soft_reconfig_bytes'] = soft_reconfig_bytes
                except Exception:
                    pass

                if num_prefix_entries or num_prefix_entries == 0:
                    nbr_af_dict['prefixes'] = {}
                    nbr_af_dict['prefixes']['total_entries'] = num_prefix_entries
                    nbr_af_dict['prefixes']['memory_usage'] = memory_usage
                if num_path_entries or num_path_entries == 0:
                    nbr_af_dict['path'] = {}
                    nbr_af_dict['path']['total_entries'] = num_path_entries
                    nbr_af_dict['path']['memory_usage'] = memory_usage
                    continue

            # Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            # 10.16.2.10
            m = p8_1.match(line)
            if m:
                data_on_nextline = True
                # Add neighbor to dictionary
                neighbor = str(m.groupdict()['neighbor'])
                if 'neighbor' not in sum_dict['vrf'][vrf]:
                    sum_dict['vrf'][vrf]['neighbor'] = {}
                if neighbor not in sum_dict['vrf'][vrf]['neighbor']:
                    sum_dict['vrf'][vrf]['neighbor'][neighbor] = {}
                nbr_dict = sum_dict['vrf'][vrf]['neighbor'][neighbor]
                continue

            # Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            #                 4     0       0       0        0    0    0     5w6d Idle 
            m = p8_2.match(line)
            if m and data_on_nextline:
                data_on_nextline = False
                # Add address family to this neighbor
                if 'address_family' not in nbr_dict:
                    nbr_dict['address_family'] = {}
                if address_family not in nbr_dict['address_family']:
                    nbr_dict['address_family'][address_family] = {}
                nbr_af_dict = nbr_dict['address_family'][address_family]

                # Add keys for this address_family
                nbr_af_dict['neighbor_table_version'] = int(m.groupdict()['v'])
                nbr_af_dict['as'] = int(m.groupdict()['as'])
                nbr_af_dict['msg_rcvd'] = int(m.groupdict()['msg_rcvd'])
                nbr_af_dict['msg_sent'] = int(m.groupdict()['msg_sent'])
                nbr_af_dict['tbl_ver'] = int(m.groupdict()['tbl_ver'])
                nbr_af_dict['inq'] = int(m.groupdict()['inq'])
                nbr_af_dict['outq'] = int(m.groupdict()['outq'])
                nbr_af_dict['up_down'] = str(m.groupdict()['up_down'])
                nbr_af_dict['state_pfxrcd'] = str(m.groupdict()['state_pfxrcd']).lower().strip()
                if m.groupdict()['state']:
                    nbr_af_dict['state'] = m.groupdict()['state_pfxrcd'].lower()
                if m.groupdict()['prx_rcd']:
                    nbr_af_dict['prefix_received'] = m.groupdict()['prx_rcd']
                    nbr_af_dict['state'] = 'established'

                try:
                    # Assign variables
                    nbr_af_dict['route_identifier'] = route_identifier
                    nbr_af_dict['local_as'] = local_as
                    nbr_af_dict['bgp_table_version'] = bgp_table_version
                    nbr_af_dict['config_peers'] = config_peers
                    nbr_af_dict['capable_peers'] = capable_peers
                    nbr_af_dict['attribute_entries'] = attribute_entries
                    nbr_af_dict['as_path_entries'] = as_path_entries
                    nbr_af_dict['community_entries'] = community_entries
                    nbr_af_dict['clusterlist_entries'] = clusterlist_entries
                    nbr_af_dict['dampening'] = dampening
                    nbr_af_dict['history_paths'] = history_paths
                    nbr_af_dict['dampened_paths'] = dampened_paths
                except Exception:
                    pass
                try:
                    nbr_af_dict['soft_reconfig_recvd_paths'] = soft_reconfig_recvd_paths
                    nbr_af_dict['soft_reconfig_identical_paths'] = soft_reconfig_identical_paths
                    nbr_af_dict['soft_reconfig_combo_paths'] = soft_reconfig_combo_paths
                    nbr_af_dict['soft_reconfig_filtered_recvd'] = soft_reconfig_filtered_recvd
                    nbr_af_dict['soft_reconfig_bytes'] = soft_reconfig_bytes
                except Exception:
                    pass

                if num_prefix_entries or num_prefix_entries == 0:
                    nbr_af_dict['prefixes'] = {}
                    nbr_af_dict['prefixes']['total_entries'] = num_prefix_entries
                    nbr_af_dict['prefixes']['memory_usage'] = memory_usage
                if num_path_entries or num_path_entries == 0:
                    nbr_af_dict['path'] = {}
                    nbr_af_dict['path']['total_entries'] = num_path_entries
                    nbr_af_dict['path']['memory_usage'] = memory_usage
                    continue

            # Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            # 10.10.10.10     4 4211111111
            m = p8_3.match(line)
            if m:
                data_on_nextline = True
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
                nbr_af_dict['neighbor_table_version'] = int(m.groupdict()['v'])
                nbr_af_dict['as'] = int(m.groupdict()['as'])
                continue

            # Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            #                               0       0        0    0    0     5w6d Idle 
            m = p8_4.match(line)
            if m and data_on_nextline:
                data_on_nextline = False
                # Add keys for this address_family
                nbr_af_dict['msg_rcvd'] = int(m.groupdict()['msg_rcvd'])
                nbr_af_dict['msg_sent'] = int(m.groupdict()['msg_sent'])
                nbr_af_dict['tbl_ver'] = int(m.groupdict()['tbl_ver'])
                nbr_af_dict['inq'] = int(m.groupdict()['inq'])
                nbr_af_dict['outq'] = int(m.groupdict()['outq'])
                nbr_af_dict['up_down'] = str(m.groupdict()['up_down'])
                nbr_af_dict['state_pfxrcd'] = str(m.groupdict()['state_pfxrcd']).lower().strip()
                if m.groupdict()['state']:
                    nbr_af_dict['state'] = m.groupdict()['state_pfxrcd'].lower()
                if m.groupdict()['prx_rcd']:
                    nbr_af_dict['prefix_received'] = m.groupdict()['prx_rcd']
                    nbr_af_dict['state'] = 'established'

                try:
                    # Assign variables
                    nbr_af_dict['route_identifier'] = route_identifier
                    nbr_af_dict['local_as'] = local_as
                    nbr_af_dict['bgp_table_version'] = bgp_table_version
                    nbr_af_dict['config_peers'] = config_peers
                    nbr_af_dict['capable_peers'] = capable_peers
                    nbr_af_dict['attribute_entries'] = attribute_entries
                    nbr_af_dict['as_path_entries'] = as_path_entries
                    nbr_af_dict['community_entries'] = community_entries
                    nbr_af_dict['clusterlist_entries'] = clusterlist_entries
                    nbr_af_dict['dampening'] = dampening
                    nbr_af_dict['history_paths'] = history_paths
                    nbr_af_dict['dampened_paths'] = dampened_paths
                except Exception:
                    pass
                try:
                    nbr_af_dict['soft_reconfig_recvd_paths'] = soft_reconfig_recvd_paths
                    nbr_af_dict['soft_reconfig_identical_paths'] = soft_reconfig_identical_paths
                    nbr_af_dict['soft_reconfig_combo_paths'] = soft_reconfig_combo_paths
                    nbr_af_dict['soft_reconfig_filtered_recvd'] = soft_reconfig_filtered_recvd
                    nbr_af_dict['soft_reconfig_bytes'] = soft_reconfig_bytes
                except Exception:
                    pass

                if num_prefix_entries or num_prefix_entries == 0:
                    nbr_af_dict['prefixes'] = {}
                    nbr_af_dict['prefixes']['total_entries'] = num_prefix_entries
                    nbr_af_dict['prefixes']['memory_usage'] = memory_usage
                if num_path_entries or num_path_entries == 0:
                    nbr_af_dict['path'] = {}
                    nbr_af_dict['path']['total_entries'] = num_path_entries
                    nbr_af_dict['path']['memory_usage'] = memory_usage
                    continue                    

        return sum_dict

    def xml(self, vrf='all', address_family='all'):

        out = self.device.execute(self.xml_command.format(vrf=vrf))

        etree_dict = {}

        # Remove junk characters returned by the device
        out = out.replace("]]>]]>", "")
        root = ET.fromstring(out)

        # top table root
        show_root = Common.retrieve_xml_child(root=root, key='show')
        # get xml namespace
        # {http://www.cisco.com/nxos:7.0.3.I7.1.:bgp}
        try:
            m = re.compile(r'(?P<name>\{[\S]+\})').match(show_root.tag)
            namespace = m.groupdict()['name']
        except Exception:
            return etree_dict

        # compare cli command
        Common.compose_compare_command(root=root, namespace=namespace,
                                       expect_command=self.cli_command[2].format(vrf=vrf,
                                                                              address_family=address_family))

        # find Vrf root
        root = Common.retrieve_xml_child(root=root, key='TABLE_vrf')

        if not root:
            return etree_dict

        # -----   loop vrf  -----
        for vrf_tree in root.findall('{}ROW_vrf'.format(namespace)):
            # vrf
            try:
                vrf = vrf_tree.find('{}vrf-name-out'.format(namespace)).text
            except Exception:
                break

            # <vrf-router-id>10.106.0.6</vrf-router-id>
            try:
                route_identifier = vrf_tree.find('{}vrf-router-id'.format(namespace)).text
            except Exception:
                route_identifier = None

            # <vrf-local-as>333</vrf-local-as>
            try:
                local_as = vrf_tree.find('{}vrf-local-as'.format(namespace)).text
            except Exception:
                local_as = None

            # Address family table
            af_tree = vrf_tree.find('{}TABLE_af'.format(namespace))
            if not af_tree:
                continue
            for af_root in af_tree.findall('{}ROW_af'.format(namespace)):
                # Address family table
                saf_tree = af_root.find('{}TABLE_saf'.format(namespace))
                if not saf_tree:
                    continue
                # -----   loop address_family  -----
                for saf_root in saf_tree.findall('{}ROW_saf'.format(namespace)):
                    # neighbor
                    try:
                        af = saf_root.find('{}af-name'.format(namespace)).text
                        af = af.lower()
                        # initial af dictionary
                        af_dict = {}
                        if route_identifier:
                            af_dict['route_identifier'] = route_identifier
                        if local_as:
                            af_dict['local_as'] = int(local_as)
                    except Exception:
                        continue

                    # <tableversion>7</tableversion>
                    try:
                        af_dict['bgp_table_version'] = int(
                            saf_root.find('{}tableversion'.format(namespace)).text)
                    except Exception:
                        # for valide entry, table version should be there
                        continue

                    # <configuredpeers>3</configuredpeers>
                    af_dict['config_peers'] = \
                        int(saf_root.find('{}configuredpeers'.format(namespace)).text)
                        
                    # <capablepeers>2</capablepeers>
                    af_dict['capable_peers'] = \
                        int(saf_root.find('{}capablepeers'.format(namespace)).text)

                    # <totalnetworks>5</totalnetworks>
                    try:
                        total_prefix_entries = \
                            int(saf_root.find('{}totalnetworks'.format(namespace)).text)
                        if 'prefixes' not in af_dict:
                            af_dict['prefixes'] = {}
                        af_dict['prefixes']['total_entries'] = total_prefix_entries
                    except Exception:
                        pass
                        
                    # <totalpaths>10</totalpaths>
                    try:
                        total_path_entries = \
                            int(saf_root.find('{}totalpaths'.format(namespace)).text)
                        if 'path' not in af_dict:
                            af_dict['path'] = {}
                        af_dict['path']['total_entries'] = total_path_entries
                    except Exception:
                        pass
                        
                    # <memoryused>1820</memoryused>
                    try:
                        memory_usage = \
                            int(saf_root.find('{}memoryused'.format(namespace)).text)
                        af_dict['path']['memory_usage'] = memory_usage
                        af_dict['prefixes']['memory_usage'] = memory_usage
                    except Exception:
                        pass

                    try:
                        # <numberattrs>1</numberattrs>
                        entries_1 = \
                            saf_root.find('{}numberattrs'.format(namespace)).text
                            
                        # <bytesattrs>160</bytesattrs>
                        entries_2 = \
                            saf_root.find('{}bytesattrs'.format(namespace)).text

                        af_dict['attribute_entries'] = '[{0}/{1}]'.format(entries_1, entries_2)
                    except Exception:
                        pass
                        
                    try:
                        # <numberpaths>1</numberpaths>
                        entries_1 = \
                            saf_root.find('{}numberpaths'.format(namespace)).text

                        # <bytespaths>34</bytespaths>
                        entries_2 = \
                            saf_root.find('{}bytespaths'.format(namespace)).text

                        af_dict['as_path_entries'] = '[{0}/{1}]'.format(entries_1, entries_2)
                    except Exception:
                        pass
                        
                    try:
                        # <numbercommunities>0</numbercommunities>
                        entries_1 = \
                            saf_root.find('{}numbercommunities'.format(namespace)).text

                        # <bytescommunities>0</bytescommunities>
                        entries_2 = \
                            saf_root.find('{}bytescommunities'.format(namespace)).text

                        af_dict['community_entries'] = '[{0}/{1}]'.format(entries_1, entries_2)
                    except Exception:
                        pass
                        
                    try:
                        # <numberclusterlist>0</numberclusterlist>
                        entries_1 = \
                            saf_root.find('{}numberclusterlist'.format(namespace)).text

                        # <bytesclusterlist>0</bytesclusterlist>
                        entries_2 = \
                            saf_root.find('{}bytesclusterlist'.format(namespace)).text

                        af_dict['clusterlist_entries'] = '[{0}/{1}]'.format(entries_1, entries_2)
                    except Exception:
                        pass

                    # <dampening>Enabled</dampening>
                    dampening = saf_root.find('{}dampening'.format(namespace)).text.lower()
                    if 'enabled' in dampening or 'true' in dampening:
                        af_dict['dampening'] = True

                    # <historypaths>0</historypaths>
                    try:
                        af_dict['history_paths'] = int(saf_root.find('{}historypaths'.format(namespace)).text)
                    except Exception:
                        pass

                    # <dampenedpaths>0</dampenedpaths>
                    try:
                        af_dict['dampened_paths'] = int(saf_root.find('{}dampenedpaths'.format(namespace)).text)
                    except Exception:
                        pass

                    # <softreconfigrecvdpaths>10</softreconfigrecvdpaths>
                    try:
                        af_dict['soft_reconfig_recvd_paths'] = int(
                                saf_root.find('{}softreconfigrecvdpaths'.format(namespace)).text)
                    except Exception:
                        pass
                        
                    # <softreconfigidenticalpaths>10</softreconfigidenticalpaths>
                    try:
                        af_dict['soft_reconfig_identical_paths'] = int(
                                saf_root.find('{}softreconfigidenticalpaths'.format(namespace)).text)
                    except Exception:
                        pass

                    # <softreconfigcombopaths>0</softreconfigcombopaths>
                    try:
                        af_dict['soft_reconfig_combo_paths'] = int(
                                saf_root.find('{}softreconfigcombopaths'.format(namespace)).text)
                    except Exception:
                        pass

                    # <softreconfigfilteredrecvd>0</softreconfigfilteredrecvd>
                    try:
                        af_dict['soft_reconfig_filtered_recvd'] = int(
                                saf_root.find('{}softreconfigfilteredrecvd'.format(namespace)).text)
                    except Exception:
                        pass
                        
                    # <softreconfigbytes>0</softreconfigbytes>
                    try:
                        af_dict['soft_reconfig_bytes'] = int(
                                saf_root.find('{}softreconfigbytes'.format(namespace)).text)
                    except Exception:
                        pass
                        
                     # Neighbor table
                    nei_tree = saf_root.find('{}TABLE_neighbor'.format(namespace))
                    if not nei_tree:
                        continue

                    # -----   loop neighbors  -----
                    for nei_root in nei_tree.findall('{}ROW_neighbor'.format(namespace)):
                        # neighbor
                        try:
                            nei = nei_root.find('{}neighborid'.format(namespace)).text
                        except Exception:
                            continue

                        if 'vrf' not in etree_dict:
                            etree_dict['vrf'] = {}
                        if vrf not in etree_dict['vrf']:
                            etree_dict['vrf'][vrf] = {}

                        if 'neighbor' not in etree_dict['vrf'][vrf]:
                            etree_dict['vrf'][vrf]['neighbor'] = {}
                        if nei not in etree_dict['vrf'][vrf]['neighbor']:
                            etree_dict['vrf'][vrf]['neighbor'][nei] = {}

                        if 'address_family' not in etree_dict['vrf'][vrf]['neighbor'][nei]:
                            etree_dict['vrf'][vrf]['neighbor'][nei]['address_family'] = {}

                        if af not in etree_dict['vrf'][vrf]['neighbor'][nei]['address_family']:
                            etree_dict['vrf'][vrf]['neighbor'][nei]['address_family'][af] = {}
                    
                        sub_dict = etree_dict['vrf'][vrf]['neighbor'][nei]['address_family'][af]

                        #  ---   AF attributes -------
                        update_dict = deepcopy(af_dict)
                        sub_dict.update(update_dict)

                        #  ---   Neighbors attributes -------
                        # <neighborversion>4</neighborversion>
                        sub_dict['neighbor_table_version'] = int(
                            nei_root.find('{}neighborversion'.format(namespace)).text)

                        # <msgrecvd>5471</msgrecvd>
                        sub_dict['msg_rcvd'] = int(
                            nei_root.find('{}msgrecvd'.format(namespace)).text)
                        
                        # <msgsent>5459</msgsent>
                        sub_dict['msg_sent'] = int(
                            nei_root.find('{}msgsent'.format(namespace)).text)
                        
                        # <neighbortableversion>7</neighbortableversion>
                        sub_dict['tbl_ver'] = int(
                            nei_root.find('{}neighbortableversion'.format(namespace)).text)
                        
                        # <inq>0</inq>
                        sub_dict['inq'] = int(
                            nei_root.find('{}inq'.format(namespace)).text)
                        
                        # <outq>0</outq>
                        sub_dict['outq'] = int(
                            nei_root.find('{}outq'.format(namespace)).text)
                        
                        # <neighboras>333</neighboras>
                        sub_dict['as'] = int(
                            nei_root.find('{}neighboras'.format(namespace)).text)
                        
                        # <time>3d18h</time>
                        sub_dict['up_down'] = \
                            nei_root.find('{}time'.format(namespace)).text
                        
                        # <state>Established</state>
                        state = nei_root.find('{}state'.format(namespace)).text.lower()

                        # <prefixreceived>5</prefixreceived>
                        prefix_received = \
                            nei_root.find('{}prefixreceived'.format(namespace)).text

                        if 'established' in state:
                            sub_dict['state'] = state
                            sub_dict['prefix_received'] = prefix_received
                            sub_dict['state_pfxrcd'] = prefix_received
                        else:
                            sub_dict['state'] = state
                            sub_dict['state_pfxrcd'] = state
                
        return etree_dict


# ==================================================
# Schema for 'show bgp vrf <WROD> all dampening parameters'
# ==================================================
class ShowBgpVrfAllAllDampeningParametersSchema(MetaParser):
    """Schema for 'show bgp vrf <WROD> all dampening parameters"""
    
    schema = {
        'vrf':
            {Any():
                {'address_family':
                    {Any():
                        {Optional('dampening'): str,
                        Optional('dampening_route_map'): str,
                        Optional('dampening_half_life_time'): str,
                        Optional('dampening_reuse_time'): str,
                        Optional('dampening_suppress_time'): str,
                        Optional('dampening_max_suppress_time'): str,
                        Optional('dampening_max_suppress_penalty'): str,
                        Optional('route_distinguisher'):
                            {Optional(Any()): {
                                Optional('rd_vrf'): str,
                                Optional('rd_vni_id'): str,
                                Optional('dampening_route_map'): str,
                                Optional('dampening_half_life_time'): str,
                                Optional('dampening_reuse_time'): str,
                                Optional('dampening_suppress_time'): str,
                                Optional('dampening_max_suppress_time'): str,
                                Optional('dampening_max_suppress_penalty'): str,
                                },
                            },
                        },
                    },
                },
            },
        }

# ==================================================
# Parser for 'show bgp vrf <WROD> all dampening parameters'
# ==================================================
class ShowBgpVrfAllAllDampeningParameters(ShowBgpVrfAllAllDampeningParametersSchema):
    """Parser for 'show bgp vrf <WROD> all dampening parameters"""

    cli_command = ['show bgp vrf {vrf} all dampening parameters',
                   'show bgp vrf {vrf} {address_family} dampening parameters']
    xml_command = 'show bgp vrf {vrf} all dampening parameters | xml'

    def cli(self, vrf='all', address_family='all', output=None):
        if output is None:
            if address_family == 'all':
                out = self.device.execute(self.cli_command[0].format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[1].format(vrf=vrf, address_family=address_family))
        else:
            out = output

        bgp_dict = {}
        sub_dict = {}
        p1 = re.compile(r'^Route +(?P<route>\w+) +Dampening +Parameters '
                            '+for +VRF +(?P<vrf>\w+) +Address +family '
                            '+(?P<af_name>[a-zA-Z0-9 ]+):$')
        p9 = re.compile(r'^Route +Distinguisher: +(?P<rd>[0-9\.:]+) +'
                        '\(VRF +(?P<rd_vrf>\w+)\)$')
        p10 = re.compile(r'^Route +Distinguisher: +(?P<rd>[0-9\.:]+) +'
                            '\((?P<rd_vrf>\w+)( *VNI +(?P<vni>\w+))\)')
        p2 = re.compile(r'^Dampening +policy +configured: '
                            '+(?P<route_map>\w+)$')
        p3 = re.compile(r'^Half-life +time +: +'
                            '(?P<half_time>\d+)( *(?P<unit>\w+))?$')
        p4 = re.compile(r'^Suppress +penalty +: +'
                            '(?P<suppress_pen>\d+)( *(?P<unit>\w+))?$')
        p5 = re.compile(r'^Reuse +penalty +: +'
                            '(?P<reuse_pen>\d+)( *(?P<unit>\w+))?$')
        p6 = re.compile(r'^Max +suppress +time +: +'
                            '(?P<max_sup_time>\d+)( *(?P<unit>\w+))?$')
        p7 = re.compile(r'^Max +suppress +penalty +: '
                            '+(?P<max_sup_pen>\d+)( *(?P<unit>\w+))?$')

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                if 'vrf' not in bgp_dict:
                    bgp_dict['vrf'] = {}

                vrf = m.groupdict()['vrf']
                if vrf not in bgp_dict['vrf']:
                    bgp_dict['vrf'][vrf] = {}
                    bgp_dict['vrf'][vrf]['address_family'] = {}

                af_name = m.groupdict()['af_name'].lower()
                if af_name not in bgp_dict['vrf'][vrf]['address_family']:
                    bgp_dict['vrf'][vrf]['address_family'][af_name] = {}
                    # trim the coding lines for adopting pep8
                    sub_dict = bgp_dict['vrf'][vrf]['address_family'][af_name]
                    sub_dict['dampening'] = 'True'
                continue

            m = p9.match(line)
            if m:
                if 'route_distinguisher' not in \
                  bgp_dict['vrf'][vrf]['address_family'][af_name]:
                   bgp_dict['vrf'][vrf]['address_family']\
                     [af_name]['route_distinguisher'] = {}
                rd = m.groupdict()['rd']
                if rd and rd not in bgp_dict['vrf'][vrf]['address_family']\
                  [af_name]['route_distinguisher']:
                    sub_dict = bgp_dict['vrf'][vrf]['address_family']\
                      [af_name]['route_distinguisher'][rd] = {}

                rd_vrf = m.groupdict()['rd_vrf']
                if rd_vrf:
                    sub_dict['rd_vrf'] = rd_vrf
                continue

            # Route Distinguisher: 500:1    (L3VNI 2)
            # rd_vrf = L3, vni = 2
            m = p10.match(line)
            if m:
                if 'route_distinguisher' not in \
                  bgp_dict['vrf'][vrf]['address_family'][af_name]:
                   bgp_dict['vrf'][vrf]['address_family']\
                     [af_name]['route_distinguisher'] = {}
                rd = m.groupdict()['rd']
                vni = m.groupdict()['vni']
                if rd and rd not in bgp_dict['vrf'][vrf]['address_family']\
                  [af_name]['route_distinguisher']:
                    sub_dict = bgp_dict['vrf'][vrf]['address_family']\
                      [af_name]['route_distinguisher'][rd] = {}

                rd_vrf = m.groupdict()['rd_vrf']
                if rd_vrf:
                    sub_dict['rd_vrf'] = rd_vrf
                if vni:
                    sub_dict['rd_vni_id'] = vni
                continue


            m = p2.match(line)
            if m:
                sub_dict['dampening_route_map'] = m.groupdict()['route_map']
                continue

            m = p3.match(line)
            if m:
                sub_dict['dampening_half_life_time'] =\
                   m.groupdict()['half_time']
                continue

            m = p4.match(line)
            if m:
                sub_dict['dampening_suppress_time'] =\
                  m.groupdict()['suppress_pen']
                continue

            m = p5.match(line)
            if m:
                sub_dict['dampening_reuse_time'] =\
                  m.groupdict()['reuse_pen']
                continue

            m = p6.match(line)
            if m:
                sub_dict['dampening_max_suppress_time'] =\
                  m.groupdict()['max_sup_time']
                continue

            m = p7.match(line)
            if m:
                sub_dict['dampening_max_suppress_penalty'] =\
                  m.groupdict()['max_sup_pen']
                continue
        return bgp_dict

    def xml(self, vrf='all', address_family='all'):
        out = self.device.execute(self.xml_command.format(vrf=vrf))
        etree_dict = {}

        # Remove junk characters returned by the device
        out = out.replace("]]>]]>", "")
        root = ET.fromstring(out)

        # top table root
        show_root = Common.retrieve_xml_child(root=root, key='show')
        # get xml namespace
        # {http://www.cisco.com/nxos:7.0.3.I7.1.:bgp}
        try:
            m = re.compile(r'(?P<name>\{[\S]+\})').match(show_root.tag)
            namespace = m.groupdict()['name']
        except Exception:
            return etree_dict

        # compare cli command
        Common.compose_compare_command(root=root, namespace=namespace,
                                       expect_command=self.cli_command[1].format(vrf=vrf,
                                                                              address_family=address_family))

        root = Common.retrieve_xml_child(
                root=root,
                key='TABLE_vrf')

        if not root:
            return etree_dict

        # -----   loop vrf  -----
        for vrf_tree in root.findall('{}ROW_vrf'.format(namespace)):
            # vrf
            try:
                vrf = vrf_tree.find('{}vrf-name-out'.format(namespace)).text
            except Exception:
                break

            # Address family table
            af_tree = vrf_tree.find('{}TABLE_afi'.format(namespace))
            if not af_tree:
                continue
            for af_root in af_tree.findall('{}ROW_afi'.format(namespace)):
                # Address family table
                saf_tree = af_root.find('{}TABLE_safi'.format(namespace))
                if not saf_tree:
                    continue
                # -----   loop address_family  -----
                for saf_root in saf_tree.findall('{}ROW_safi'.format(namespace)):
                    # neighbor
                    try:
                        af = saf_root.find('{}af-name'.format(namespace)).text
                        af = af.lower()
                    except Exception:
                        continue

                     # RD table
                    rd_tree = saf_root.find('{}TABLE_rd'.format(namespace))
                    if not rd_tree:
                        continue

                    # -----   loop rd  -----
                    for rd_root in rd_tree.findall('{}ROW_rd'.format(namespace)):

                        # neighbor
                        try:
                            rd = rd_root.find('{}rd_val'.format(namespace)).text
                        except Exception:
                            rd = None

                        if 'vrf' not in etree_dict:
                            etree_dict['vrf'] = {}
                        if vrf not in etree_dict['vrf']:
                            etree_dict['vrf'][vrf] = {}

                        if 'address_family' not in etree_dict['vrf'][vrf]:
                            etree_dict['vrf'][vrf]['address_family'] = {}

                        if af not in etree_dict['vrf'][vrf]['address_family']:
                            etree_dict['vrf'][vrf]['address_family'][af] = {}

                        # dampening
                        etree_dict['vrf'][vrf]['address_family'][af]['dampening'] = 'True'

                        if rd:
                            if 'route_distinguisher' not in etree_dict['vrf'][vrf]:
                                etree_dict['vrf'][vrf]['address_family'][af]\
                                    ['route_distinguisher'] = {}

                            if rd not in etree_dict['vrf'][vrf]['address_family']:
                                etree_dict['vrf'][vrf]['address_family'][af]\
                                    ['route_distinguisher'][rd] = {}
                            sub_dict = etree_dict['vrf'][vrf]['address_family'][af]\
                                    ['route_distinguisher'][rd]
                        else:
                            sub_dict = etree_dict['vrf'][vrf]['address_family'][af]
                                    

                        # <dampconfigured>Configured</dampconfigured>
                        # cli does not have this key

                        # <rpmname>test</rpmname>
                        try:
                            sub_dict['dampening_route_map'] = \
                                rd_root.find('{}rpmname'.format(namespace)).text
                        except Exception:
                            pass

                        # <rd_vrf>vpn2</rd_vrf>
                        try:
                            sub_dict['rd_vrf'] = \
                                rd_root.find('{}rd_vrf'.format(namespace)).text
                        except Exception:
                            pass

                        # <rd_vniid>2</rd_vniid>
                        try:
                            sub_dict['rd_vni_id'] = \
                                rd_root.find('{}rd_vniid'.format(namespace)).text
                        except Exception:
                            pass

                        # <damphalflife>1</damphalflife>
                        try:
                            sub_dict['dampening_half_life_time'] = \
                                rd_root.find('{}damphalflife'.format(namespace)).text
                        except Exception:
                            pass

                        # <dampsuppress>30</dampsuppress>
                        try:
                            sub_dict['dampening_suppress_time'] = \
                                rd_root.find('{}dampsuppress'.format(namespace)).text
                        except Exception:
                            pass

                        # <dampreuse>10</dampreuse>
                        try:
                            sub_dict['dampening_reuse_time'] = \
                                rd_root.find('{}dampreuse'.format(namespace)).text
                        except Exception:
                            pass

                        # <dampsuppresstime>2</dampsuppresstime>
                        try:
                            sub_dict['dampening_max_suppress_time'] = \
                                rd_root.find('{}dampsuppresstime'.format(namespace)).text
                        except Exception:
                            pass

                        # <dampmaxpenalty>40</dampmaxpenalty>
                        try:
                            sub_dict['dampening_max_suppress_penalty'] = \
                                rd_root.find('{}dampmaxpenalty'.format(namespace)).text
                        except Exception:
                            pass

                        # TABLE_rpm
                        rpm_tree = rd_root.find('{}TABLE_rpm'.format(namespace))
                        if not rpm_tree:
                            continue

                        # ROW_rpm
                        for rpm_root in rpm_tree.findall('{}ROW_rpm'.format(namespace)):

                            # <rpmdamphalflife>1</rpmdamphalflife>
                            try:
                                sub_dict['dampening_half_life_time'] = \
                                    rpm_root.find('{}rpmdamphalflife'.format(namespace)).text
                            except Exception:
                                pass

                            # <rpmdampsuppress>30</rpmdampsuppress>
                            try:
                                sub_dict['dampening_suppress_time'] = \
                                    rpm_root.find('{}rpmdampsuppress'.format(namespace)).text
                            except Exception:
                                pass

                            # <rpmdampreuse>10</rpmdampreuse>
                            try:
                                sub_dict['dampening_reuse_time'] = \
                                    rpm_root.find('{}rpmdampreuse'.format(namespace)).text
                            except Exception:
                                pass

                            # <rpmdampsuppresstime>2</rpmdampsuppresstime>
                            try:
                                sub_dict['dampening_max_suppress_time'] = \
                                    rpm_root.find('{}rpmdampsuppresstime'.format(namespace)).text
                            except Exception:
                                pass

                            # <rpmdampmaxpenalty>40</rpmdampmaxpenalty>
                            try:
                                sub_dict['dampening_max_suppress_penalty'] = \
                                    rpm_root.find('{}rpmdampmaxpenalty'.format(namespace)).text
                            except Exception:
                                pass

        return etree_dict


# ==========================================================================
# Schema for 'show bgp vrf <vrf> all neighbors <neighbor> advertised-routes'
# ==========================================================================
class ShowBgpVrfAllNeighborsAdvertisedRoutesSchema(MetaParser):
    """Schema for show bgp vrf <vrf> all neighbors <neighbor> advertised-routes"""

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
                                 Optional('rd_l2vni'): int,
                                 Optional('rd_l3vni'): int,
                                 Optional('advertised'): 
                                    {Optional(Any()):
                                        {Optional('index'):
                                            {Optional(Any()):
                                                {Optional('next_hop'): str,
                                                 Optional('status_codes'): str,
                                                 Optional('path_type'): str,
                                                 Optional('metric'): int,
                                                 Optional('locprf'): int,
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

# ==========================================================================
# Parser for 'show bgp vrf <vrf> all neighbors <neighbor> advertised-routes'
# ==========================================================================
class ShowBgpVrfAllNeighborsAdvertisedRoutes(ShowBgpVrfAllNeighborsAdvertisedRoutesSchema):
    """Parser for show bgp vrf <vrf> all neighbors <neighbor> advertised-routes"""

    cli_command = ['show bgp vrf {vrf} all neighbors {neighbor} advertised-routes',
                   'show bgp vrf {vrf} {address_family} neighbors {neighbor} advertised-routes']

    def cli(self, neighbor, vrf='all', address_family='all', output=None):
        if vrf == 'all':
            vrf = 'default'

        if output is None:
            if address_family == 'all':

                out = self.device.execute(
                        self.cli_command[0].format(neighbor=neighbor, vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[1].format(vrf=vrf,
                                                              address_family=address_family,
                                                              neighbor=neighbor))
        else:
            out = output

        # Init dictionary
        route_dict = {}

        p1 = re.compile(r'^\s*Peer +(?P<neighbor_id>(\S+)) +routes +for'
                        r' +address +family'
                        r' +(?P<address_family>[a-zA-Z0-9\s\-\_]+) *:$')
        p2 = re.compile(r'^\s*BGP +table +version +is'
                        r' +(?P<bgp_table_version>[0-9]+), +[Ll]ocal +[Rr]outer'
                        r' +ID +is +(?P<local_router_id>(\S+))$')
        p3 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                            r'(?P<path_type>(i|e|c|l|a|r|I))?'
                            r'(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                            r'(?: *(?P<next_hop>[a-zA-Z0-9\.\:\/\[\]\,]+))?$')
        p4 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                            r'(?P<path_type>(i|e|c|l|a|r|I))?'
                            r' *(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                            r'(?: +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}]+))?'
                            r' +(?P<origin_codes>(i|e|\?|\|))$')
        p5 = re.compile(r'^\s*(?P<status_codes>(\*\>|s|x|S|d|h|\*|\>|\s)+)'
                            r'(?P<path_type>(i|e|c|l|a|r|I))?'
                            r'( *(?P<origin_codes>(i|e|\?|\&|\|)+))'
                            r' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                            r' +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}\?]+)$')
        p6 = re.compile(r'^(?P<metric>[0-9]+)'
                        r'(?P<space1>\s{5,10})'
                        r'(?P<localprf>[0-9]+)'
                        r'(?P<space2>\s{5,10})'
                        r'(?P<weight>[0-9]+)'
                        r'(?: *(?P<path>[0-9\{\}\s]+))?$')
        p7 = re.compile(r'^(?P<value>[0-9]+)'
                        r'(?P<space>\s{2,21})'
                        r'(?P<weight>[0-9]+)'
                        r'(?: *(?P<path>[0-9\{\}\s]+))?$')
        p8 = re.compile(r'^(?P<weight>[0-9]+)'
                            r' +(?P<path>[0-9\{\}\s]+)$')
        p9 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)'
                            r'(?P<path_type>(i|e|c|l|a|r|I))'
                            r'(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                            r' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                            r' +(?P<numbers>[a-zA-Z0-9\.\s\(\)\{\}]+)'
                            r' +(?P<origin_codes>(i|e|\?|\&|\|))$')
        p10 = re.compile(r'^\s*(?P<status_codes>(\*\>|s|x|S|d|h|\*|\>|\s)+)'
                            r'(?P<path_type>(i|e|c|l|a|r|I))?'
                            r'( *(?P<origin_codes>(i|e|\?|\&|\|)+))'
                            r'(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                            r' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                            r' +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}\?]+)$')
        p11 = re.compile(r'^(?P<metric>[0-9]+)'
                        r'(?P<space1>\s{5,10})'
                        r'(?P<localprf>[0-9]+)'
                        r'(?P<space2>\s{5,10})'
                        r'(?P<weight>[0-9]+)'
                        r'(?: *(?P<path>[0-9\{\}\s]+))?$')
        p12 = re.compile(r'^(?P<value>[0-9]+)'
                        r'(?P<space>\s{2,21})'
                        r'(?P<weight>[0-9]+)'
                        r'(?: *(?P<path>[0-9\{\}\s]+))?$')
        p13 = re.compile(r'^(?P<weight>[0-9]+)'
                        r' +(?P<path>[0-9\.\{\}\s]+)$')
        p14 = re.compile(r'^\s*Route +Distinguisher *: +(?P<route_distinguisher>'
                        r'(\S+))(?: +\((?:VRF +(?P<default_vrf>\w+)|L2VNI +'
                        r'(?P<rd_l2vni>\d+)|L3VNI +(?P<rd_l3vni>\d+))\))?$')
        # Init vars
        data_on_nextline =  False
        index = 1
        bgp_table_version = local_router_id = ''

        # Peer 10.186.0.2 routes for address family IPv4 Unicast:

        # BGP table version is 25, Local Router ID is 10.186.101.1

        # Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
        # Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
        # Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

        # *>i[2]:[77][7,0][10.69.9.9,1,151587081][10.135.1.1,22][10.106.101.1,10.76.1.30]/616
        # *>i2001:db8:aaaa:1::/113       ::ffff:10.106.101.1

        #                     0.0.0.0               100      32768 i
        #                     10.106.101.1            4444       100 0 3 10 20 30 40 50 60 70 80 90 i

        # * e                   10.70.2.2                                      0 100 300 ?
        # *>e                   10.70.1.2                                      0 100 300 ?

        # Metric     LocPrf     Weight Path
        #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90

        #    100        ---          0 10 20 30 40 50 60 70 80 90
        #    ---        100          0 10 20 30 40 50 60 70 80 90
        #    100        ---      32788 ---
        #    ---        100      32788 --- 

        #    ---        ---      32788 200 33299 51178 47751 {27016}

        # Network            Next Hop            Metric     LocPrf     Weight Path
        # *>l10.4.1.0/24         0.0.0.0                           100      32768 i
        # *>r10.16.1.0/24         0.0.0.0               4444        100      32768 ?
        # *>r10.16.2.0/24         0.0.0.0               4444        100      32768 ?
        # *>i10.49.0.0/16         10.106.101.1                        100          0 10 20 30 40 50 60 70 80 90 i
        # *>i10.4.2.0/24         10.106.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i

        # *&i10.145.1.0/24        192.168.151.2                0        100          0 ?

        # Metric     LocPrf     Weight Path
        #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90

        #    100        ---          0 10 20 30 40 50 60 70 80 90
        #    ---        100          0 10 20 30 40 50 60 70 80 90
        #    100        ---      32788 ---
        #    ---        100      32788 --- 

        #    ---        ---      32788 200 33299 51178 47751 {27016}

        # Network            Next Hop            Metric     LocPrf     Weight Path
        # Route Distinguisher: 100:100     (VRF VRF1)
        # Route Distinguisher: 2:100    (VRF vpn2)
        # Route Distinguisher: 10.16.2.2:4    (L3VNI 10200)
        # Route Distinguisher: 10.16.2.2:2    (L2VNI 10400)

        for line in out.splitlines():
            line = line.rstrip()

            # Peer 10.186.0.2 routes for address family IPv4 Unicast:
            m = p1.match(line)
            if m:
                neighbor_id = m.groupdict()['neighbor_id']
                address_family = m.groupdict()['address_family'].lower()
                original_address_family = address_family
                continue

            # BGP table version is 25, Local Router ID is 10.186.101.1
            m = p2.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                local_router_id = str(m.groupdict()['local_router_id'])

                if 'vrf' not in route_dict:
                    afs_dict = route_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('neighbor', {}).\
                                        setdefault(neighbor_id, {}).setdefault('address_family', {})

                af_dict = afs_dict.setdefault(address_family, {})
                advertised_dict = af_dict.setdefault('advertised', {})

                af_dict.update({'bgp_table_version': bgp_table_version})
                af_dict.update({'local_router_id': local_router_id})
                continue

            # Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
            # Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
            # Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

            # *>i[2]:[77][7,0][10.69.9.9,1,151587081][10.135.1.1,22][10.106.101.1,10.76.1.30]/616
            # *>i2001:db8:aaaa:1::/113       ::ffff:10.106.101.1
            m = p3.match(line)
            if m:
                # New prefix, reset index count
                index = 1
                data_on_nextline = True

                # Get keys
                status_codes = str(m.groupdict()['status_codes'])
                path_type = str(m.groupdict()['path_type'])
                prefix = str(m.groupdict()['prefix'])

                # Init dicts
                prefix_dict = advertised_dict.setdefault(prefix, {})
                indexes_dict = prefix_dict.setdefault('index', {})
                index_dict = indexes_dict.setdefault(index, {})

                # Set keys
                index_dict.update({'status_codes': status_codes})
                index_dict.update({'path_type': path_type})

                if m.groupdict()['next_hop']:
                    index_dict.update({'next_hop': str(m.groupdict()['next_hop'])})
                    
                continue

            #                     0.0.0.0               100      32768 i
            #                     10.106.101.1            4444       100 0 3 10 20 30 40 50 60 70 80 90 i
            m = p4.match(line)
            # * e                   10.70.2.2                                      0 100 300 ?
            # *>e                   10.70.1.2                                      0 100 300 ?
            m1 = p5.match(line)

            m = m if m else m1
            if m:
                # Get keys
                next_hop = str(m.groupdict()['next_hop'])
                origin_codes = str(m.groupdict()['origin_codes'])

                if data_on_nextline:
                    data_on_nextline =  False
                else:
                    index += 1

                # Init dict
                index_dict = indexes_dict.setdefault(index, {})

                # Set keys
                index_dict.update({'next_hop': next_hop})
                index_dict.update({'origin_codes': origin_codes})
                try:
                    index_dict.update({'status_codes': status_codes})
                    index_dict.update({'path_type': path_type})
                except Exception:
                    pass

                # Parse numbers
                numbers = m.groupdict()['numbers']

                # Metric     LocPrf     Weight Path
                #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                m = p6.match(numbers)
                if m:
                    index_dict.update({'metric': int(m.groupdict()['metric'])})
                    index_dict.update({'locprf': int(m.groupdict()['localprf'])})
                    index_dict.update({'weight': int(m.groupdict()['weight'])})

                    # Set path
                    if m.groupdict()['path']:
                        index_dict.update({'path': m.groupdict()['path'].strip()})

                    continue

                #    100        ---          0 10 20 30 40 50 60 70 80 90
                #    ---        100          0 10 20 30 40 50 60 70 80 90
                #    100        ---      32788 ---
                #    ---        100      32788 --- 
                m = p7.match(numbers)
                if m:
                    index_dict.update({'weight': int(m.groupdict()['weight'])})

                    # Set metric or localprf
                    if len(m.groupdict()['space']) > 10:
                        index_dict.update({'metric': int(m.groupdict()['value'])})
                    else:
                        index_dict.update({'locprf': int(m.groupdict()['value'])})

                    # Set path
                    if m.groupdict()['path']:
                        index_dict.update({'path': m.groupdict()['path'].strip()})

                    continue

                #    ---        ---      32788 200 33299 51178 47751 {27016}
                m = p8.match(numbers)
                if m:
                    index_dict.update({'weight': int(m.groupdict()['weight'])})
                    index_dict.update({'path': m.groupdict()['path'].strip()})
                    continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # *>l10.4.1.0/24         0.0.0.0                           100      32768 i
            # *>r10.16.1.0/24         0.0.0.0               4444        100      32768 ?
            # *>r10.16.2.0/24         0.0.0.0               4444        100      32768 ?
            # *>i10.49.0.0/16         10.106.101.1                        100          0 10 20 30 40 50 60 70 80 90 i
            # *>i10.4.2.0/24         10.106.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
            # *>e100.100.100.120/30 10.10.2.1                                      0 {64102.333 64201 64202} 64203 64500.2345 i
            m = p9.match(line)
            # *&i10.145.1.0/24        192.168.151.2                0        100          0 ?
            m1 = p10.match(line)
            
            m = m if m else m1
            if m:
                # New prefix, reset index count
                index = 1
                
                # Get keys
                status_codes = str(m.groupdict()['status_codes'])
                path_type = str(m.groupdict()['path_type'])
                prefix = str(m.groupdict()['prefix'])
                next_hop = str(m.groupdict()['next_hop'])
                origin_codes = str(m.groupdict()['origin_codes'])

                # Init dicts
                prefix_dict = advertised_dict.setdefault(prefix, {})
                indexes_dict = prefix_dict.setdefault('index', {})
                index_dict = indexes_dict.setdefault(index, {})

                # Set keys
                index_dict.update({'status_codes': status_codes})
                index_dict.update({'path_type': path_type})
                index_dict.update({'next_hop': next_hop})
                index_dict.update({'origin_codes': origin_codes})

                # Parse numbers
                numbers = m.groupdict()['numbers']

                # Metric     LocPrf     Weight Path
                #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                m = p11.match(numbers)
                if m:
                    index_dict.update({'metric': int(m.groupdict()['metric'])})
                    index_dict.update({'locprf': int(m.groupdict()['localprf'])})
                    index_dict.update({'weight': int(m.groupdict()['weight'])})

                    # Set path
                    if m.groupdict()['path']:
                        index_dict.update({'path': m.groupdict()['path'].strip()})
                        
                    continue

                #    100        ---          0 10 20 30 40 50 60 70 80 90
                #    ---        100          0 10 20 30 40 50 60 70 80 90
                #    100        ---      32788 ---
                #    ---        100      32788 --- 
                m = p12.match(numbers)
                if m:
                    index_dict.update({'weight': int(m.groupdict()['weight'])})

                    # Set metric or localprf
                    if len(m.groupdict()['space']) > 10:
                        index_dict.update({'metric': int(m.groupdict()['value'])})
                    else:
                        index_dict.update({'locprf': int(m.groupdict()['value'])})

                    # Set path
                    if m.groupdict()['path']:
                        index_dict.update({'path': m.groupdict()['path'].strip()})

                    continue

                #    ---        ---      32788 200 33299 51178 47751 {27016}
                m = p13.match(numbers)
                if m:
                    index_dict.update({'weight': int(m.groupdict()['weight'])})
                    index_dict.update({'path': m.groupdict()['path'].strip()})
                    continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # Route Distinguisher: 100:100     (VRF VRF1)
            # Route Distinguisher: 2:100    (VRF vpn2)
            m = p14.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])
                new_address_family = original_address_family + ' RD ' + route_distinguisher
                
                # Init dict
                af_dict = afs_dict.setdefault(new_address_family, {})
                
                # Set keys
                af_dict.update({'bgp_table_version': bgp_table_version})
                af_dict.update({'local_router_id': local_router_id})
                af_dict.update({'route_distinguisher': route_distinguisher})

                if m.groupdict()['default_vrf']: 
                    af_dict.update({'default_vrf': str(m.groupdict()['default_vrf'])})

                if m.groupdict()['rd_l2vni']:
                    af_dict.update({'rd_l2vni': int(m.groupdict()['rd_l2vni'])})

                if m.groupdict()['rd_l3vni']:
                    af_dict.update({'rd_l3vni': int(m.groupdict()['rd_l3vni'])})

                # Reset address_family key and af_dict for use in other regex
                address_family = new_address_family

                # Init advertised dict
                if 'advertised' not in af_dict:
                    advertised_dict = af_dict.setdefault('advertised', {})
                    continue

        # order the af prefixes index
        # return dict when parsed dictionary is empty
        if 'vrf' not in route_dict:
            return route_dict

        for vrf in route_dict['vrf']:
            if 'neighbor' not in route_dict['vrf'][vrf]:
                continue
            for nei in route_dict['vrf'][vrf]['neighbor']:
                for af in route_dict['vrf'][vrf]['neighbor'][nei]['address_family']:
                    af_dict = route_dict['vrf'][vrf]['neighbor'][nei]['address_family'][af]
                    if 'advertised' in af_dict:
                        for routes in af_dict['advertised']:
                            if len(af_dict['advertised'][routes]['index'].keys()) > 1:                            
                                ind = 1
                                nexthop_dict = {}
                                sorted_list = sorted(af_dict['advertised'][routes]['index'].items(),
                                                   key = lambda x:x[1]['next_hop'])
                                for i, j in enumerate(sorted_list):
                                    nexthop_dict[ind] = af_dict['advertised'][routes]['index'][j[0]]
                                    ind += 1
                                del(af_dict['advertised'][routes]['index'])
                                af_dict['advertised'][routes]['index'] = nexthop_dict

        return route_dict

# ===============================================================
# Schema for 'show bgp vrf <vrf> all neighbors <neighbor> routes'
# ===============================================================
class ShowBgpVrfAllNeighborsRoutesSchema(MetaParser):
    """Schema for show bgp vrf <vrf> all neighbors <neighbor> routes"""

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
                                 Optional('routes'): 
                                    {Optional(Any()):
                                        {Optional('index'):
                                            {Optional(Any()):
                                                {Optional('next_hop'): str,
                                                 Optional('status_codes'): str,
                                                 Optional('path_type'): str,
                                                 Optional('metric'): int,
                                                 Optional('locprf'): int,
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

# ===============================================================
# Parser for 'show bgp vrf <vrf> all neighbors <neighbor> routes'
# ===============================================================
class ShowBgpVrfAllNeighborsRoutes(ShowBgpVrfAllNeighborsRoutesSchema):
    """Parser for show bgp vrf <vrf> all neighbors <neighbor> routes"""

    cli_command = ['show bgp vrf {vrf} all neighbors {neighbor} routes',
                   'show bgp vrf {vrf} {address_family} neighbors {neighbor} routes']

    def cli(self, neighbor, vrf='all', address_family='all', output=None):
        if vrf == 'all':
            vrf = 'default'

        if output is None:
            if address_family == 'all':

                out = self.device.execute(
                        self.cli_command[0].format(neighbor=neighbor, vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[1].format(vrf=vrf,
                                                                     address_family=address_family,
                                                                     neighbor=neighbor))

        else:
            out = output
        
        # Init dictionary
        route_dict = {}
        af_dict = {}

        p = re.compile(r'^\s*Network +Next Hop +Metric +LocPrf +Weight Path$')
        p1 = re.compile(r'^\s*Peer +(?P<neighbor_id>(\S+)) +routes +for'
                            ' +address +family'
                            ' +(?P<address_family>[a-zA-Z0-9\s\-\_]+) *:$')
        p2 = re.compile(r'^\s*BGP +table +version +is'
                            ' +(?P<bgp_table_version>[0-9]+), +[Ll]ocal +[Rr]outer'
                            ' +ID +is +(?P<local_router_id>(\S+))$')
        p3_1 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                            '(?P<path_type>(i|e|c|l|a|r|I))?'
                            '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                            '(?: *(?P<next_hop>[a-zA-Z0-9\.\:\/\[\]\,]+))?$')
        p3_3 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                            '(?P<path_type>(i|e|c|l|a|r|I))?'
                            ' *(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                            '(?: +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}]+))?'
                            ' +(?P<origin_codes>(i|e|\?|\|))$')
        p3_3_1 = re.compile(r'^\s*(?P<status_codes>(\*\>|s|x|S|d|h|\*|\>|\s)+)'
                                '(?P<path_type>(i|e|c|l|a|r|I))?'
                                '( *(?P<origin_codes>(i|e|\?|\&|\|)+))'
                                ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                                ' +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}\?]+)$')
        # *>e100.100.100.118/30 10.10.2.1                                      0 64102.444 {64201 64202} 64203 64500.2345 i
        p3_2 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)'
                            '(?P<path_type>(i|e|c|l|a|r|I))'
                            '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                            ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                            ' +(?P<numbers>[a-zA-Z0-9\.\s\(\)\{\}]+)'
                            ' +(?P<origin_codes>(i|e|\?|\&|\|))$')
        p3_2_1 = re.compile(r'^\s*(?P<status_codes>(\*\>|s|x|S|d|h|\*|\>|\s)+)'
                                '(?P<path_type>(i|e|c|l|a|r|I))?'
                                '( *(?P<origin_codes>(i|e|\?|\&|\|)+))'
                                '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                                ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                                ' +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}\?]+)$')
        p4 = re.compile(r'^\s*Route +Distinguisher *:'
                            ' +(?P<route_distinguisher>(\S+))'
                            '(?: +\(((VRF +(?P<default_vrf>\S+))|'
                            '((?P<default_vrf1>\S+)VNI +(?P<vni>\d+)))\))?$')
        # Init vars
        data_on_nextline = False
        index = 1
        bgp_table_version = local_router_id = ''

        for line in out.splitlines():
            line = line.rstrip()

            # Network            Next Hop            Metric     LocPrf     Weight Path
            m = p.match(line)
            if m:
                continue

            # Peer 10.186.0.2 routes for address family IPv4 Unicast:
            m = p1.match(line)
            if m:
                neighbor_id = str(m.groupdict()['neighbor_id'])
                address_family = str(m.groupdict()['address_family']).lower()
                original_address_family = address_family
                continue

            # BGP table version is 25, Local Router ID is 10.186.101.1
            # BGP table version is 381, Local Router ID is 10.4.1.2
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
                
                # Init routes dict
                if 'routes' not in af_dict:
                    af_dict['routes'] = {}

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

            # *>i[2]:[77][7,0][10.69.9.9,1,151587081][10.135.1.1,22][10.106.101.1,10.76.1.30]/616
            # *>i2001:db8:aaaa:1::/113       ::ffff:10.106.101.1
            m = p3_1.match(line)
            if m:
                # New prefix, reset index count
                index = 1
                data_on_nextline = True

                # Get keys
                status_codes = str(m.groupdict()['status_codes'])
                path_type = str(m.groupdict()['path_type'])
                prefix = str(m.groupdict()['prefix'])

                # Init dict
                if 'routes' not in af_dict:
                    af_dict['routes'] = {}
                if prefix not in af_dict['routes']:
                    af_dict['routes'][prefix] = {}
                if 'index' not in af_dict['routes'][prefix]:
                    af_dict['routes'][prefix]['index'] = {}
                if index not in af_dict['routes'][prefix]['index']:
                    af_dict['routes'][prefix]['index'][index] = {}

                # Set keys
                af_dict['routes'][prefix]['index'][index]['status_codes'] = status_codes
                af_dict['routes'][prefix]['index'][index]['path_type'] = path_type
                if m.groupdict()['next_hop']:
                    af_dict['routes'][prefix]['index'][index]['next_hop'] = str(m.groupdict()['next_hop'])
                continue

            #                     0.0.0.0               100      32768 i
            #                     10.106.101.1            4444       100 0 3 10 20 30 40 50 60 70 80 90 i
            # *>i                 10.106.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
            m = p3_3.match(line)

            # * e                   10.70.2.2                                      0 100 300 ?
            # *>e                   10.70.1.2                                      0 100 300 ?
            m1 = p3_3_1.match(line)
            m = m if m else m1
            if m:
                # Get keys
                next_hop = str(m.groupdict()['next_hop'])
                origin_codes = str(m.groupdict()['origin_codes'])

                if data_on_nextline:
                    data_on_nextline =  False
                else:
                    index += 1

                # Init dict
                if 'routes' not in af_dict:
                    af_dict['routes'] = {}
                if prefix not in af_dict['routes']:
                    af_dict['routes'][prefix] = {}
                if 'index' not in af_dict['routes'][prefix]:
                    af_dict['routes'][prefix]['index'] = {}
                if index not in af_dict['routes'][prefix]['index']:
                    af_dict['routes'][prefix]['index'][index] = {}

                # Set keys
                af_dict['routes'][prefix]['index'][index]['next_hop'] = next_hop
                af_dict['routes'][prefix]['index'][index]['origin_codes'] = origin_codes
                try:
                    # Set values of status_codes and path_type from prefix line
                    af_dict['routes'][prefix]['index'][index]['status_codes'] = status_codes
                    af_dict['routes'][prefix]['index'][index]['path_type'] = path_type
                except Exception:
                    pass

                # Parse numbers
                numbers = m.groupdict()['numbers']
                
                # Metric     LocPrf     Weight Path
                #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                 '(?P<space1>\s{5,10})'
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
                    af_dict['routes'][prefix]['index'][index]['metric'] = int(m1.groupdict()['metric'])
                    af_dict['routes'][prefix]['index'][index]['locprf'] = int(m1.groupdict()['localprf'])
                    af_dict['routes'][prefix]['index'][index]['weight'] = int(m1.groupdict()['weight'])
                    # Set path
                    if m1.groupdict()['path']:
                        af_dict['routes'][prefix]['index'][index]['path'] = m1.groupdict()['path'].strip()
                        continue
                elif m2:
                    af_dict['routes'][prefix]['index'][index]['weight'] = int(m2.groupdict()['weight'])
                    # Set metric or localprf
                    if len(m2.groupdict()['space']) > 10:
                        af_dict['routes'][prefix]['index'][index]['metric'] = int(m2.groupdict()['value'])
                    else:
                        af_dict['routes'][prefix]['index'][index]['locprf'] = int(m2.groupdict()['value'])
                    # Set path
                    if m2.groupdict()['path']:
                        af_dict['routes'][prefix]['index'][index]['path'] = m2.groupdict()['path'].strip()
                        continue
                elif m3:
                    af_dict['routes'][prefix]['index'][index]['weight'] = int(m3.groupdict()['weight'])
                    af_dict['routes'][prefix]['index'][index]['path'] = m3.groupdict()['path'].strip()
                    continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # *>l10.4.1.0/24         0.0.0.0                           100      32768 i
            # *>r10.16.1.0/24         0.0.0.0               4444        100      32768 ?
            # *>r10.16.2.0/24         0.0.0.0               4444        100      32768 ?
            # *>i10.49.0.0/16         10.106.101.1                        100          0 10 20 30 40 50 60 70 80 90 i
            # *>i10.4.2.0/24         10.106.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
            # *>e100.100.100.118/30 10.10.2.1                                      0 64102.444 {64201 64202} 64203 64500.2345 i
            m = p3_2.match(line)

            # *&i10.145.1.0/24        192.168.151.2                0        100          0 ?
            m1 = p3_2_1.match(line)
            m = m if m else m1
            if m:
                # New prefix, reset index count
                index = 1
                
                # Get keys
                status_codes = str(m.groupdict()['status_codes'])
                path_type = str(m.groupdict()['path_type'])
                prefix = str(m.groupdict()['prefix'])
                next_hop = str(m.groupdict()['next_hop'])
                origin_codes = str(m.groupdict()['origin_codes'])

                # Init dict
                if 'routes' not in af_dict:
                    af_dict['routes'] = {}
                if prefix not in af_dict['routes']:
                    af_dict['routes'][prefix] = {}
                if 'index' not in af_dict['routes'][prefix]:
                    af_dict['routes'][prefix]['index'] = {}
                if index not in af_dict['routes'][prefix]['index']:
                    af_dict['routes'][prefix]['index'][index] = {}
                if index not in af_dict['routes'][prefix]['index']:
                    af_dict['routes'][prefix]['index'][index] = {}

                # Set keys
                af_dict['routes'][prefix]['index'][index]['status_codes'] = status_codes
                af_dict['routes'][prefix]['index'][index]['path_type'] = path_type
                af_dict['routes'][prefix]['index'][index]['next_hop'] = next_hop
                af_dict['routes'][prefix]['index'][index]['origin_codes'] = origin_codes

                # Parse numbers
                numbers = m.groupdict()['numbers']
                
                # Metric     LocPrf     Weight Path
                #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                 '(?P<space1>\s{5,10})'
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
                # *>e100.100.100.118/30 10.10.2.1                                      0 64102.444 {64201 64202} 64203 64500.2345 i
                m3 = re.compile(r'^(?P<weight>[0-9]+)'
                                 ' +(?P<path>[0-9\.\{\}\s]+)$').match(numbers)

                if m1:
                    af_dict['routes'][prefix]['index'][index]['metric'] = int(m1.groupdict()['metric'])
                    af_dict['routes'][prefix]['index'][index]['locprf'] = int(m1.groupdict()['localprf'])
                    af_dict['routes'][prefix]['index'][index]['weight'] = int(m1.groupdict()['weight'])
                    # Set path
                    if m1.groupdict()['path']:
                        af_dict['routes'][prefix]['index'][index]['path'] = m1.groupdict()['path'].strip()
                        continue
                elif m2:
                    af_dict['routes'][prefix]['index'][index]['weight'] = int(m2.groupdict()['weight'])
                    # Set metric or localprf
                    if len(m2.groupdict()['space']) > 10:
                        af_dict['routes'][prefix]['index'][index]['metric'] = int(m2.groupdict()['value'])
                    else:
                        af_dict['routes'][prefix]['index'][index]['locprf'] = int(m2.groupdict()['value'])
                    # Set path
                    if m2.groupdict()['path']:
                        af_dict['routes'][prefix]['index'][index]['path'] = m2.groupdict()['path'].strip()
                        continue
                elif m3:
                    af_dict['routes'][prefix]['index'][index]['weight'] = int(m3.groupdict()['weight'])
                    af_dict['routes'][prefix]['index'][index]['path'] = m3.groupdict()['path'].strip()
                    continue


            # Network            Next Hop            Metric     LocPrf     Weight Path
            # Route Distinguisher: 100:100     (VRF VRF1)
            # Route Distinguisher: 2:100    (VRF vpn2)
            # Route Distinguisher: 10.49.1.0:3    (L3VNI 9100)
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
                
                # Init routes dict
                if 'routes' not in af_dict:
                    af_dict['routes'] = {}
                    continue

        # order the af prefixes index
        # return dict when parsed dictionary is empty
        if 'vrf' not in route_dict:
            return route_dict

        for vrf in route_dict['vrf']:
            if 'neighbor' not in route_dict['vrf'][vrf]:
                continue
            for nei in route_dict['vrf'][vrf]['neighbor']:
                for af in route_dict['vrf'][vrf]['neighbor'][nei]['address_family']:
                    af_dict = route_dict['vrf'][vrf]['neighbor'][nei]['address_family'][af]
                    if 'routes' in af_dict:
                        for routes in af_dict['routes']:
                            if len(af_dict['routes'][routes]['index'].keys()) > 1:                            
                                ind = 1
                                nexthop_dict = {}
                                sorted_list = sorted(af_dict['routes'][routes]['index'].items(),
                                                   key = lambda x:x[1]['next_hop'])
                                for i, j in enumerate(sorted_list):
                                    nexthop_dict[ind] = af_dict['routes'][routes]['index'][j[0]]
                                    ind += 1
                                del(af_dict['routes'][routes]['index'])
                                af_dict['routes'][routes]['index'] = nexthop_dict

        return route_dict


# =====================================================================
# Schema for 'show bgp vrf <WORD> all neighbors <WORD> received-routes'
# =====================================================================
class ShowBgpVrfAllNeighborsReceivedRoutesSchema(MetaParser):
    """Schema for show bgp vrf <vrf> all neighbors <neighbor> received-routes"""

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
                                 Optional('received_routes'): 
                                    {Optional(Any()):
                                        {Optional('index'):
                                            {Optional(Any()):
                                                {Optional('next_hop'): str,
                                                 Optional('status_codes'): str,
                                                 Optional('path_type'): str,
                                                 Optional('metric'): int,
                                                 Optional('locprf'): int,
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

# =====================================================================
# Parser for 'show bgp vrf <WORD> all neighbors <WORD> received-routes'
# =====================================================================
class ShowBgpVrfAllNeighborsReceivedRoutes(ShowBgpVrfAllNeighborsReceivedRoutesSchema):
    """Parser for show bgp vrf <vrf> all neighbors <neighbor> received-routes"""

    cli_command =['show bgp vrf {vrf} all neighbors {neighbor} received-routes',
                  'show bgp vrf {vrf} {address_family} neighbors {neighbor} received-routes']

    def cli(self, neighbor, vrf='all', address_family='all', output=None):
        if vrf == 'all':
            vrf = 'default'
        if output is None:
            if address_family == 'all':
                out = self.device.execute(
                        self.cli_command[0].format(neighbor=neighbor, vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[1].format(vrf=vrf,
                                                                     address_family=address_family,
                                                                     neighbor=neighbor))
        else:
            out = output
        
        # Init dictionary
        route_dict = {}
        af_dict = {}

        p = re.compile(r'^\s*Network +Next Hop +Metric +LocPrf +Weight Path$')
        p1 = re.compile(r'^\s*Peer +(?P<neighbor_id>(\S+)) +routes +for'
                            ' +address +family'
                            ' +(?P<address_family>[a-zA-Z0-9\s\-\_]+) *:$')
        p2 = re.compile(r'^\s*BGP +table +version +is'
                            ' +(?P<bgp_table_version>[0-9]+), +[Ll]ocal +[Rr]outer'
                            ' +ID +is +(?P<local_router_id>(\S+))$')
        p3_1 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                            '(?P<path_type>(i|e|c|l|a|r|I))?'
                            '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                            '(?: *(?P<next_hop>[a-zA-Z0-9\.\:\/\[\]\,]+))?$')
        p3_3 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                            '(?P<path_type>(i|e|c|l|a|r|I))?'
                            ' *(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                            '(?: +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}]+))?'
                            ' +(?P<origin_codes>(i|e|\?|\|))$')
        p3_3_1 = re.compile(r'^\s*(?P<status_codes>(\*\>|s|x|S|d|h|\*|\>|\s)+)'
                                '(?P<path_type>(i|e|c|l|a|r|I))?'
                                '( *(?P<origin_codes>(i|e|\?|\&|\|)+))'
                                ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                                ' +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}\?]+)$')
        # *>e100.100.100.118/30 10.10.2.1                                      0 64102.444 {64201 64202} 64203 64500.2345 i
        p3_2 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)'
                            '(?P<path_type>(i|e|c|l|a|r|I))'
                            '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                            ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                            ' +(?P<numbers>[a-zA-Z0-9\.\s\(\)\{\}]+)'
                            ' +(?P<origin_codes>(i|e|\?|\&|\|))$')
        p3_2_1 = re.compile(r'^\s*(?P<status_codes>(\*\>|s|x|S|d|h|\*|\>|\s)+)'
                                '(?P<path_type>(i|e|c|l|a|r|I))?'
                                '( *(?P<origin_codes>(i|e|\?|\&|\|)+))'
                                '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                                ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                                ' +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}\?]+)$')
        p4 = re.compile(r'^\s*Route +Distinguisher *:'
                            ' +(?P<route_distinguisher>(\S+))'
                            '(?: +\(((VRF +(?P<default_vrf>\S+))|'
                            '((?P<default_vrf1>\S+)VNI +(?P<vni>\d+)))\))?$')
        # Init vars
        data_on_nextline =  False
        index = 1
        bgp_table_version = local_router_id = ''

        for line in out.splitlines():
            line = line.rstrip()

            # Network            Next Hop            Metric     LocPrf     Weight Path
            m = p.match(line)
            if m:
                continue

            # Peer 10.186.0.2 routes for address family IPv4 Unicast:
            m = p1.match(line)
            if m:
                neighbor_id = str(m.groupdict()['neighbor_id'])
                address_family = str(m.groupdict()['address_family']).lower()
                original_address_family = address_family
                continue

            # BGP table version is 25, Local Router ID is 10.186.101.1
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
                
                # Init received_routes dict
                if 'received_routes' not in af_dict:
                    af_dict['received_routes'] = {}
                    
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

            # *>i[2]:[77][7,0][10.69.9.9,1,151587081][10.135.1.1,22][10.106.101.1,10.76.1.30]/616
            # *>i2001:db8:aaaa:1::/113       ::ffff:10.106.101.1
            m = p3_1.match(line)
            if m:
                # New prefix, reset index count
                index = 1
                data_on_nextline = True

                # Get keys
                status_codes = str(m.groupdict()['status_codes'])
                path_type = str(m.groupdict()['path_type'])
                prefix = str(m.groupdict()['prefix'])

                # Init dict
                if 'received_routes' not in af_dict:
                    af_dict['received_routes'] = {}
                if prefix not in af_dict['received_routes']:
                    af_dict['received_routes'][prefix] = {}
                if 'index' not in af_dict['received_routes'][prefix]:
                    af_dict['received_routes'][prefix]['index'] = {}
                if index not in af_dict['received_routes'][prefix]['index']:
                    af_dict['received_routes'][prefix]['index'][index] = {}

                # Set keys
                af_dict['received_routes'][prefix]['index'][index]['status_codes'] = status_codes
                af_dict['received_routes'][prefix]['index'][index]['path_type'] = path_type
                if m.groupdict()['next_hop']:
                    af_dict['received_routes'][prefix]['index'][index]['next_hop'] = str(m.groupdict()['next_hop'])
                continue

            #                     0.0.0.0               100      32768 i
            #                     10.106.101.1            4444       100 0 3 10 20 30 40 50 60 70 80 90 i
            # *>i                 10.106.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
            m = p3_3.match(line)

            # * e                   10.70.2.2                                      0 100 300 ?
            # *>e                   10.70.1.2                                      0 100 300 ?
            m1 = p3_3_1.match(line)
            m = m if m else m1
            if m:
                # Get keys
                next_hop = str(m.groupdict()['next_hop'])
                origin_codes = str(m.groupdict()['origin_codes'])

                if data_on_nextline:
                    data_on_nextline =  False
                else:
                    index += 1

                # Init dict
                if 'received_routes' not in af_dict:
                    af_dict['received_routes'] = {}
                if prefix not in af_dict['received_routes']:
                    af_dict['received_routes'][prefix] = {}
                if 'index' not in af_dict['received_routes'][prefix]:
                    af_dict['received_routes'][prefix]['index'] = {}
                if index not in af_dict['received_routes'][prefix]['index']:
                    af_dict['received_routes'][prefix]['index'][index] = {}

                # Set keys
                af_dict['received_routes'][prefix]['index'][index]['next_hop'] = next_hop
                af_dict['received_routes'][prefix]['index'][index]['origin_codes'] = origin_codes
                try:
                    # Set values of status_codes and path_type from prefix line
                    af_dict['received_routes'][prefix]['index'][index]['status_codes'] = status_codes
                    af_dict['received_routes'][prefix]['index'][index]['path_type'] = path_type
                except Exception:
                    pass

                # Parse numbers
                numbers = m.groupdict()['numbers']
                
                # Metric     LocPrf     Weight Path
                #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                 '(?P<space1>\s{5,10})'
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
                    af_dict['received_routes'][prefix]['index'][index]['metric'] = int(m1.groupdict()['metric'])
                    af_dict['received_routes'][prefix]['index'][index]['locprf'] = int(m1.groupdict()['localprf'])
                    af_dict['received_routes'][prefix]['index'][index]['weight'] = int(m1.groupdict()['weight'])
                    # Set path
                    if m1.groupdict()['path']:
                        af_dict['received_routes'][prefix]['index'][index]['path'] = m1.groupdict()['path'].strip()
                        continue
                elif m2:
                    af_dict['received_routes'][prefix]['index'][index]['weight'] = int(m2.groupdict()['weight'])
                    # Set metric or localprf
                    if len(m2.groupdict()['space']) > 10:
                        af_dict['received_routes'][prefix]['index'][index]['metric'] = int(m2.groupdict()['value'])
                    else:
                        af_dict['received_routes'][prefix]['index'][index]['locprf'] = int(m2.groupdict()['value'])
                    # Set path
                    if m2.groupdict()['path']:
                        af_dict['received_routes'][prefix]['index'][index]['path'] = m2.groupdict()['path'].strip()
                        continue
                elif m3:
                    af_dict['received_routes'][prefix]['index'][index]['weight'] = int(m3.groupdict()['weight'])
                    af_dict['received_routes'][prefix]['index'][index]['path'] = m3.groupdict()['path'].strip()
                    continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # *>l10.4.1.0/24         0.0.0.0                           100      32768 i
            # *>r10.16.1.0/24         0.0.0.0               4444        100      32768 ?
            # *>r10.16.2.0/24         0.0.0.0               4444        100      32768 ?
            # *>i10.49.0.0/16         10.106.101.1                        100          0 10 20 30 40 50 60 70 80 90 i
            # *>i10.4.2.0/24         10.106.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
            # *>e100.100.100.118/30 10.10.2.1                                      0 64102.444 {64201 64202} 64203 64500.2345 i
            m = p3_2.match(line)

            # *&i10.145.1.0/24        192.168.151.2                0        100          0 ?
            m1 = p3_2_1.match(line)
            m = m if m else m1
            if m:
                # New prefix, reset index count
                index = 1
                
                # Get keys
                status_codes = str(m.groupdict()['status_codes'])
                path_type = str(m.groupdict()['path_type'])
                prefix = str(m.groupdict()['prefix'])
                next_hop = str(m.groupdict()['next_hop'])
                origin_codes = str(m.groupdict()['origin_codes'])

                # Init dict
                if 'received_routes' not in af_dict:
                    af_dict['received_routes'] = {}
                if prefix not in af_dict['received_routes']:
                    af_dict['received_routes'][prefix] = {}
                if 'index' not in af_dict['received_routes'][prefix]:
                    af_dict['received_routes'][prefix]['index'] = {}
                if index not in af_dict['received_routes'][prefix]['index']:
                    af_dict['received_routes'][prefix]['index'][index] = {}
                if index not in af_dict['received_routes'][prefix]['index']:
                    af_dict['received_routes'][prefix]['index'][index] = {}

                # Set keys
                af_dict['received_routes'][prefix]['index'][index]['status_codes'] = status_codes
                af_dict['received_routes'][prefix]['index'][index]['path_type'] = path_type
                af_dict['received_routes'][prefix]['index'][index]['next_hop'] = next_hop
                af_dict['received_routes'][prefix]['index'][index]['origin_codes'] = origin_codes

                # Parse numbers
                numbers = m.groupdict()['numbers']
                
                # Metric     LocPrf     Weight Path
                #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                 '(?P<space1>\s{5,10})'
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
                                 ' +(?P<path>[0-9\.\{\}\s]+)$').match(numbers)

                if m1:
                    af_dict['received_routes'][prefix]['index'][index]['metric'] = int(m1.groupdict()['metric'])
                    af_dict['received_routes'][prefix]['index'][index]['locprf'] = int(m1.groupdict()['localprf'])
                    af_dict['received_routes'][prefix]['index'][index]['weight'] = int(m1.groupdict()['weight'])
                    # Set path
                    if m1.groupdict()['path']:
                        af_dict['received_routes'][prefix]['index'][index]['path'] = m1.groupdict()['path'].strip()
                        continue
                elif m2:
                    af_dict['received_routes'][prefix]['index'][index]['weight'] = int(m2.groupdict()['weight'])
                    # Set metric or localprf
                    if len(m2.groupdict()['space']) > 10:
                        af_dict['received_routes'][prefix]['index'][index]['metric'] = int(m2.groupdict()['value'])
                    else:
                        af_dict['received_routes'][prefix]['index'][index]['locprf'] = int(m2.groupdict()['value'])
                    # Set path
                    if m2.groupdict()['path']:
                        af_dict['received_routes'][prefix]['index'][index]['path'] = m2.groupdict()['path'].strip()
                        continue
                elif m3:
                    af_dict['received_routes'][prefix]['index'][index]['weight'] = int(m3.groupdict()['weight'])
                    af_dict['received_routes'][prefix]['index'][index]['path'] = m3.groupdict()['path'].strip()
                    continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # Route Distinguisher: 100:100     (VRF VRF1)
            # Route Distinguisher: 2:100    (VRF vpn2)
            # Route Distinguisher: 10.49.1.0:3    (L3VNI 9100)
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
                
                # Init received_routes dict
                if 'received_routes' not in af_dict:
                    af_dict['received_routes'] = {}
                    continue

        # order the af prefixes index
        # return dict when parsed dictionary is empty
        if 'vrf' not in route_dict:
            return route_dict

        for vrf in route_dict['vrf']:
            if 'neighbor' not in route_dict['vrf'][vrf]:
                continue
            for nei in route_dict['vrf'][vrf]['neighbor']:
                for af in route_dict['vrf'][vrf]['neighbor'][nei]['address_family']:
                    af_dict = route_dict['vrf'][vrf]['neighbor'][nei]['address_family'][af]
                    if 'received_routes' in af_dict:
                        for routes in af_dict['received_routes']:
                            if len(af_dict['received_routes'][routes]['index'].keys()) > 1:                            
                                ind = 1
                                nexthop_dict = {}
                                sorted_list = sorted(af_dict['received_routes'][routes]['index'].items(),
                                                   key = lambda x:x[1]['next_hop'])
                                for i, j in enumerate(sorted_list):
                                    nexthop_dict[ind] = af_dict['received_routes'][routes]['index'][j[0]]
                                    ind += 1
                                del(af_dict['received_routes'][routes]['index'])
                                af_dict['received_routes'][routes]['index'] = nexthop_dict
        return route_dict

# ============================================
# Parser for 'show bgp vrf <vrf> ipv4 unicast'
# ============================================
class ShowBgpVrfIpv4Unicast(ShowBgpVrfAllAll):
    """Parser for show bgp vrf <vrf> ipv4 unicast"""
    cli_command = 'show bgp vrf {vrf} ipv4 unicast'

    def cli(self, vrf, output=None):
        if output is None:      
            show_output = self.device.execute(self.cli_command.format(vrf=vrf))
        else:
            show_output = output
        return super().cli(output=show_output)
