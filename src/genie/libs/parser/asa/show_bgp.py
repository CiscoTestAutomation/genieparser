''' show_bgp.py

ASA BGP parsers for the following show commands:
    * show bgp summary
    * show bgp {address_family} unicast summary
'''
#Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# =====================================================
# Schema for:
#   * 'show bgp summary'
#   * 'show bgp {address_family} unicast summary'
# =====================================================
class ShowBgpSummarySchema(MetaParser):

    ''' Schema for
        * 'show bgp summary'
        * 'show bgp ipv4 unicast summary'
    '''


schema = {
      	"type": "object",
      	"properties": {
      		"bgp_id": { "type": "integer" },
      		"neighbor": {
      			"type": "object",
      			"patternProperties": {
      				"^.+$": {
      					"type": "object",
      					"properties": {
      						"address_family": {
      							"type": "object",
      							"patternProperties": {
      								"^.+$": {
      									"type": "object",
      									"properties": {
      										"version": { "type": "integer" },
      										"as": { "type": "integer" },
      										"msg_rcvd": { "type": "integer" },
      										"msg_sent": { "type": "integer" },
      										"tbl_ver": { "type": "integer" },
      										"input_queue": { "type": "integer" },
      										"output_queue": { "type": "integer" },
      										"up_down": { "type": "string" },
      										"state_pfxrcd": { "type": "string" },
      										"route_identifier": { "type": "string" },
      										"local_as": { "type": "integer" },
      										"bgp_table_version": { "type": "integer" },
      										"routing_table_version": { "type": "integer" },
      										"attribute_entries": { "type": "string" },
      										"prefixes": {
      											"type": "object",
      											"properties": {
      												"total_entries": { "type": "integer" },
      												"memory_usage": { "type": "integer" }
      											},
      											"required": ["total_entries", "memory_usage"]
      										},
      										"path": {
      											"type": "object",
      											"properties": {
      												"total_entries": { "type": "integer" },
      												"memory_usage": { "type": "integer" }
      											},
      											"required": ["total_entries", "memory_usage"]
      										},
      										"total_memory": { "type": "integer" },
      										"activity_prefixes": { "type": "string" },
      										"activity_paths": { "type": "string" },
      										"scan_interval": { "type": "integer" },
      										"cache_entries": {
      											"type": "object",
      											"patternProperties": {
      												"^.+$": {
      													"type": "object",
      													"properties": {
      														"total_entries": { "type": "integer" },
      														"memory_usage": { "type": "integer" }
      													},
      													"required": ["total_entries", "memory_usage"]
      												}
      											}
      										},
      										"filter-list": {
      											"type": "object",
      											"patternProperties": {
      												"^.+$": {
      													"type": "object",
      													"properties": {
      														"total_entries": { "type": "integer" },
      														"memory_usage": { "type": "integer" }
      													},
      													"required": ["total_entries", "memory_usage"]
      												}
      											}
      										},
      										"entries": {
      											"type": "object",
      											"patternProperties": {
      												"^.+$": {
      													"type": "object",
      													"properties": {
      														"total_entries": { "type": "integer" },
      														"memory_usage": { "type": "integer" }
      													},
      													"required": ["total_entries", "memory_usage"]
      												}
      											}
      										}
      									},
      									"required": ["version", "as", "msg_rcvd", "msg_sent", "tbl_ver", "input_queue", "output_queue", "up_down", "state_pfxrcd"]
      								}
      							}
      						}
      					},
      					"required": ["address_family"]
      				}
      			}
      		}
      	},
      	"required": ["bgp_id", "neighbor"]
      }

# ==================================================
# Super Parser for:
#   * 'show bgp summary'
#   * 'show bgp {address_family} summary'
# ==================================================
class ShowBgpSummarySuperParser(ShowBgpSummarySchema):

    ''' Parser for:
        * 'show bgp summary'
        * 'show bgp {address_family} summary'
    '''

    def cli(self, address_family='',  cmd='', output=None):

        # Init vars
        sum_dict = {}
        cache_dict = {}
        entries_dict = {}
        bgp_config_dict = {}

        # For address family: IPv4 Unicast
        p1 = re.compile(r'^For address family: +(?P<address_family>[a-zA-Z0-9\s\-\_]+)$')

        # BGP router identifier 192.168.111.1, local AS number 100
        # BGP router identifier 30.1.107.78, local AS number 304.304
        p2 = re.compile(r'^BGP +router +identifier'
                         ' +(?P<route_identifier>[0-9\.\:]+), +local +AS'
                         ' +number +(?P<local_as>[0-9\.]+)$')

        # BGP table version is 28, main routing table version 28
        p3 = re.compile(r'^BGP +table +version +is'
                         ' +(?P<bgp_table_version>[0-9]+),'
                         ' +main +routing +table +version'
                         ' +(?P<routing_table_version>[0-9]+)$')

        # 27 network entries using 6696 bytes of memory
        p4 = re.compile(r'^(?P<networks>[0-9]+) +network +entries +using'
                         ' +(?P<bytes>[0-9]+) +bytes +of +memory$')

        # 27 path entries using 3672 bytes of memory
        p5 = re.compile(r'^(?P<path>[0-9]+) +path +entries +using'
                         ' +(?P<memory_usage>[0-9]+) +bytes +of +memory$')

        # 2 BGP rrinfo entries using 48 bytes of memory
        # 201 BGP AS-PATH entries using 4824 bytes of memory
        p5_1 = re.compile(r'^(?P<num_entries>([0-9]+)) +BGP'
                           ' +(?P<entries_type>(\S+)) +entries +using'
                           ' +(?P<entries_byte>[0-9]+) +bytes +of +memory$')

        # 4 BGP extended community entries using 96 bytes of memory
        p5_2 = re.compile(r'^(?P<num_community_entries>[0-9]+) +BGP +extended'
                           ' +community +entries +using'
                           ' +(?P<memory_usage>[0-9]+) +bytes +of +memory$')

        # 1/1 BGP path/bestpath attribute entries using 280 bytes of memory
        p6 = re.compile(r'^(?P<attribute_entries>(\S+)) +BGP'
                         ' +(?P<attribute_type>(\S+)) +attribute +entries'
                         ' +using +(?P<bytes>[0-9]+) +bytes +of +memory$')

        # 0 BGP route-map cache entries using 0 bytes of memory
        # 0 BGP filter-list cache entries using 0 bytes of memory
        p6_1 = re.compile(r'^(?P<num_cache_entries>([0-9]+)) +BGP'
                           ' +(?P<cache_type>(\S+)) +cache +entries +using'
                           ' +(?P<cache_byte>[0-9]+) +bytes +of +memory$')

        # BGP using 10648 total bytes of memory
        p7 = re.compile(r'^BGP +using +(?P<total_memory>[0-9]+) +total +bytes'
                         ' +of +memory$')

        # BGP activity 47/20 prefixes, 66/39 paths, scan interval 60 secs
        p8 = re.compile(r'^BGP +activity +(?P<activity_prefixes>(\S+))'
                         ' +prefixes, +(?P<activity_paths>(\S+)) +paths, +scan'
                         ' +interval +(?P<scan_interval>[0-9]+) +secs$')

        # Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        # 192.168.111.1       4          100       0       0        1    0    0 01:07:38 Idle
        # 192.168.4.1       4          100       0       0        1    0    0 never    Idle
        # 192.168.51.1       4          100       0       0        1    0    0 01:07:38 Idle
        p9 = re.compile(r'^ *(?P<our_entry>\*)?(?P<neighbor>[a-zA-Z0-9\.\:]+) +(?P<version>[0-9]+)'
                         ' +(?P<as>[0-9]+(\.\d+)?) +(?P<msg_rcvd>[0-9]+)'
                         ' +(?P<msg_sent>[0-9]+) +(?P<tbl_ver>[0-9]+)'
                         ' +(?P<inq>[0-9]+) +(?P<outq>[0-9]+)'
                         ' +(?P<up_down>[a-zA-Z0-9\:]+)'
                         ' +(?P<state>[a-zA-Z0-9\(\)\s]+)$')

        #  Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        #  2001:DB8:20:4:6::6
        #           4          400      67      73       66    0    0 01:03:11        5
        #  *2001::100:1:2:1
        #                  4        65001       7       7      198    0    0 00:00:02        1
        p10 = re.compile(r'^(?P<our_entry>\*)?(?P<neighbor>[a-zA-Z0-9\.\:]+)$')

        p11 = re.compile(r'^(?P<version>[0-9]+)'
                          ' +(?P<as>[0-9]+(\.\d+)?) +(?P<msg_rcvd>[0-9]+)'
                          ' +(?P<msg_sent>[0-9]+) +(?P<tbl_ver>[0-9]+)'
                          ' +(?P<inq>[0-9]+) +(?P<outq>[0-9]+)'
                          ' +(?P<up_down>[a-zA-Z0-9\:]+)'
                         ' +(?P<state>[a-zA-Z0-9\(\)\s]+)$')

        for line in output.splitlines():

            line = line.strip()

            # For address family: IPv4 Unicast
            m = p1.match(line)
            if m:
                # Save variables for use later
                address_family = m.groupdict()['address_family'].lower()
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

            # BGP router identifier 192.168.111.1, local AS number 100
            # BGP router identifier 30.1.107.78, local AS number 304.304
            m = p2.match(line)
            if m:
                route_identifier = m.groupdict()['route_identifier']
                try:
                    local_as = int(m.groupdict()['local_as'])
                except:
                    local_as = m.groupdict()['local_as']

                sum_dict['bgp_id'] = local_as
                continue

            # BGP table version is 28, main routing table version 28
            m = p3.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                routing_table_version = int(m.groupdict()['routing_table_version'])
                continue

            # 27 network entries using 6696 bytes of memory
            m = p4.match(line)
            if m:
                num_prefix_entries = int(m.groupdict()['networks'])
                num_memory_usage = int(m.groupdict()['bytes'])
                continue

            # 27 path entries using 3672 bytes of memory
            m = p5.match(line)
            if m:
                path_total_entries = int(m.groupdict()['path'])
                path_memory_usage = int(m.groupdict()['memory_usage'])
                continue

            # 2 BGP rrinfo entries using 48 bytes of memory
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
            m = p5_2.match(line)
            if m:
                num_community_entries = int(m.groupdict()['num_community_entries'])
                community_memory_usage = int(m.groupdict()['memory_usage'])
                continue

            # 1/1 BGP path/bestpath attribute entries using 280 bytes of memory
            m = p6.match(line)
            if m:
                attribute_entries = str(m.groupdict()['attribute_entries'])
                attribute_type = str(m.groupdict()['attribute_type'])
                attribute_memory_usage = int(m.groupdict()['bytes'])
                continue

            # 0 BGP route-map cache entries using 0 bytes of memory
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
            m = p7.match(line)
            if m:
                total_memory = int(m.groupdict()['total_memory'])
                continue

            # BGP activity 47/20 prefixes, 66/39 paths, scan interval 60 secs
            m = p8.match(line)
            if m:
                activity_prefixes = str(m.groupdict()['activity_prefixes'])
                activity_paths = str(m.groupdict()['activity_paths'])
                scan_interval = str(m.groupdict()['scan_interval'])
                continue

            # Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            # 192.168.111.1       4          100       0       0        1    0    0 01:07:38 Idle
            # 192.168.4.1       4          100       0       0        1    0    0 never    Idle
            # 192.168.51.1       4          100       0       0        1    0    0 01:07:38 Idle
            # 30.1.10.1       4      304.304    6953   38119   136088    0    0 00:50:14     2540
            # 30.2.10.1       4      304.304    6347   38120   136088    0    0 00:50:13     2580
            # 30.3.10.1       4      301.301    7722   38113   136088    0    0 00:50:14     4439
            m = p9.match(line)
            if m:
                # Add neighbor to dictionary
                neighbor = str(m.groupdict()['neighbor'])
                try:
                    neighbor_as = int(m.groupdict()['as'])
                except:
                    neighbor_as = m.groupdict()['as']
                nbr_dict = sum_dict.setdefault('neighbor', {}).setdefault(neighbor, {})

                nbr_af_dict = nbr_dict.setdefault('address_family', {})\
                                      .setdefault(address_family, {})

                # Add keys for this address_family
                nbr_af_dict['version'] = int(m.groupdict()['version'])
                nbr_af_dict['as'] = neighbor_as
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
                except Exception:
                    pass
            else:
                # when neighbor info break down to 2 lines.
                #  Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
                #  2001:DB8:20:4:6::6
                #           4          400      67      73       66    0    0 01:03:11        5
                m = p10.match(line)
                if m :
                    # Add neighbor to dictionary
                    neighbor = str(m.groupdict()['neighbor'])

                    # Add address family to this neighbor
                    if 'address_family' not in nbr_dict:
                        nbr_dict['address_family'] = {}
                    if address_family not in nbr_dict['address_family']:
                        nbr_dict['address_family'][address_family] = {}
                    nbr_af_dict = nbr_dict['address_family'][address_family]

                m = p11.match(line)
                if m:
                    # Add keys for this address_family
                    nbr_af_dict['version'] = int(m.groupdict()['version'])
                    try:
                        nbr_af_dict['as'] = int(m.groupdict()['as'])
                    except:
                        nbr_af_dict['as'] = m.groupdict()['as']
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
                    except Exception:
                        pass
                continue

        return sum_dict


# =====================================================
# Parser for:
#   * 'show bgp summary'
#   * 'show bgp {address_family} unicast summary'
# =====================================================
class ShowBgpSummary(ShowBgpSummarySuperParser, ShowBgpSummarySchema):

    ''' Parser for:
        * 'show bgp summary'
        * 'show bgp {address_family} summary'
    '''

    cli_command = ['show bgp {address_family} summary',
                   'show bgp summary'
                   ]
    exclude = ['msg_rcvd', 'msg_sent']

    def cli(self, address_family='', output=None):

        cmd = ''
        if output is None:
            # Build command
            if address_family:
                cmd = self.cli_command[0].format(address_family=address_family)

            else:
                cmd = self.cli_command[1]
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output,
                           address_family=address_family, cmd=cmd)
