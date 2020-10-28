'''
show_ip.py

IOSXE parsers for the following show commands:
    * show ip aliases
	* show ip aliases default-vrf
	* show ip aliases vrf {vrf}
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# ==============================
# Schema for 'show ip aliases', 'show ip aliases vrf {vrf}'
# ==============================
class ShowIPAliasSchema(MetaParser):
    '''
	Schema for:
	show ip aliases
	show ip aliases vrf {vrf}
	'''
    schema = {
        'vrf': {
            Any(): {
                'index': {
                    Any(): { # just incrementing 1, 2, 3, ... per entry
                        'address_type': str,
                        'ip_address': str,
                        Optional('port'): int,
                    },
                },
            },
        },
    }

# ==============================
# Parser for 'show ip aliases', 'show ip aliases vrf {vrf}'
# ==============================
class ShowIPAlias(ShowIPAliasSchema):
    '''
    Parser for:
    show ip aliases
    show ip aliases vrf {vrf}
    '''
    cli_command = ['show ip aliases',
        'show ip aliases vrf {vrf}']

    def cli(self, vrf = '', output = None):
        if output is None:
            if vrf:
                out = self.device.execute(self.cli_command[1].format(vrf = vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init vars
        parsed_dict = {}
        index = 1   # set a counter for the index

        # Address Type             IP Address      Port
        # Interface                10.169.197.94
        p1 = re.compile(r'(?P<address_type>(\S+)) +(?P<ip_address>(\S+))(?: +(?P<port>(\d+)))?$')
        # "?:" (for port) means optional

        for line in out.splitlines():
            line = line.strip()

            # Interface                10.169.197.94
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if vrf:
                    vrf = vrf
                else:
                    vrf = 'default'
                vrf_dict = parsed_dict.setdefault('vrf', {}).\
                                       setdefault(vrf, {}).\
                                       setdefault('index', {}).\
                                       setdefault(index, {})
                vrf_dict['address_type'] = group['address_type']
                vrf_dict['ip_address'] = group['ip_address']
                if group['port']:
                    vrf_dict['port'] = int(group['port'])

                index += 1
                continue

        return parsed_dict

# ==============================
# Parser for show ip aliases default-vrf'
# ==============================
class ShowIPAliasDefaultVrf(ShowIPAlias):
    '''
    Parser for:
	show ip aliases default-vrf
	'''
    cli_command = 'show ip aliases default-vrf'

    def cli(self, output = None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output

        return super().cli(output = show_output)


# =======================================
# Schema for:
#  * 'show ip bgp vpnv4 vrf {vrf} summary'
# =======================================
class ShowIpBgpVpnv4VrfUserSummarySchema(MetaParser):
    """Schema for show ip bgp vpnv4 vrf {vrf} summary."""

    schema = {
            "rid": str,
            "local_as": int,
            "table_version": int,
            "main_routing_table_version": int,
            "network_entries": int,
            "network_entries_memory_usage_bytes": int,
            "multipath_network_entries": int,
            "multipath_paths": int,
            "path_attribute_entries": int,
            "best_path_attribute_entries": int,
            "as_path_entries": int,
            "as_path_entries_memory_usage_bytes": int,
            "extended_community_entries": int,
            "extended_community_entries_memory_usage_bytes": int,
            "route_map_cache_entries": int,
            "route_map_cache_entries_memory_usage_bytes": int,
            "filter_list_cache_entries": int,
            "filter_list_cache_entries_memory_usage_bytes": int,
            "total_memory_usage_bytes": int,
            "prefix_memory_allocation_count": int,
            "prefix_memory_release_count": int,
            "path_memory_allocation_count": int,
            "path_memory_release_count": int,
            "neighbor_ips": {
                str: {
                    "version": int,
                    "as": int,
                    "messages_received": int,
                    "messages_sent": int,
                    "table_version": int,
                    "in_queue": int,
                    "out_queue": int,
                    "up_down": str,
                    "state": int
                },
                str: {
                    "version": int,
                    "as": int,
                    "messages_received": int,
                    "messages_sent": int,
                    "table_version": int,
                    "in_queue": int,
                    "out_queue": int,
                    "up_down": str,
                    "state": int
                },
                str: {
                    "version": int,
                    "as": int,
                    "messages_received": int,
                    "messages_sent": int,
                    "table_version": int,
                    "in_queue": int,
                    "out_queue": int,
                    "up_down": str,
                    "state": int
                }
            }
        }


# =======================================
# Parser for:
#  * 'show ip bgp vpnv4 vrf {vrf} summary'
# =======================================
class ShowIpBgpVpnv4VrfUserSummary(ShowIpBgpVpnv4VrfUserSummarySchema):
    """Parser for show ip bgp vpnv4 vrf {vrf} summary"""

    cli_command = 'show ip bgp vpnv4 vrf {vrf} summary'

    def cli(self, vrf, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vrf=vrf))
        else:
            output = output

        # BGP router identifier 10.19.228.213, local AS number 64106
        # BGP table version is 4571, main routing table version 4571
        # 69 network entries using 17664 bytes of memory
        # 80 path entries using 10880 bytes of memory
        # 11 multipath network entries and 22 multipath paths
        # 33/22 BGP path/bestpath attribute entries using 9768 bytes of memory
        # 2 BGP AS-PATH entries using 64 bytes of memory
        # 5 BGP extended community entries using 120 bytes of memory
        # 0 BGP route-map cache entries using 0 bytes of memory
        # 0 BGP filter-list cache entries using 0 bytes of memory
        # BGP using 38496 total bytes of memory
        # BGP activity 854/668 prefixes, 2572/2305 paths, scan interval 60 secs
        #
        # Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        # 10.199.228.201  4        65001  202074  202468     4571    0    0 18w1d          10
        # 10.199.228.209  4        65001  499437  638231     4571    0    0 5w2d           58
        # 10.199.228.217  4        65001  496306  634769     4571    0    0 5w2d           10

        # BGP router identifier 10.19.228.213, local AS number 64106
        p_bgp_router = re.compile(r"^BGP\s+router\s+identifier\s+(?P<rid>\S+),\s+local\s+AS\s+number\s+(?P<as>\d+)$")

        # BGP table version is 4571, main routing table version 4571
        p_bgp_table = re.compile(r"^BGP\s+table\s+version\s+is\s+(?P<tv>\d+),\s+main\s+routing\s+table\s+version\s+(?P<mtv>\d+)$")

        # 69 network entries using 17664 bytes of memory
        p_bgp_network = re.compile(r"^(?P<ne>\d+)\s+network\s+entries\s+using\s+(?P<mem>\d+)\s+bytes\s+of\s+memory$")

        # 80 path entries using 10880 bytes of memory
        p_bgp_paths = re.compile(r"(?P<pe>\d+)\s+path\s+entries\s+using\s+(?P<mem>\d+s)\s+bytes\s+of\s+memory$")

        # 11 multipath network entries and 22 multipath paths
        p_bgp_multipath = re.compile(r"^(?P<me>\d+)\s+multipath\s+network\s+entries\s+and\s+(?P<multipaths>\d+)\s+multipath\s+paths$")

        # 33/22 BGP path/bestpath attribute entries using 9768 bytes of memory
        p_bgp_bp = re.compile(r"^(?P<path_num>\d+)\/(?P<b_path_num>\d+)\s+BGP\s+path\/bestpath\s+attribute\s+entries\s+using\s+(?P<mem>\d+)\s+bytes\s+of\s+memory$")

        # 2 BGP AS-PATH entries using 64 bytes of memory
        p_bgp_as = re.compile(r"^(?P<as>\d+)\s+BGP\s+AS-PATH\s+entries\s+using\s+(?P<mem>\d+)\s+bytes\s+of\s+memory$")

        # 5 BGP extended community entries using 120 bytes of memory
        p_bgp_exten = re.compile(r"^(?P<bgp_exten>\d+)\s+BGP\s+extended\s+community\s+entries\s+using\s+(?P<mem>\d+)\s+bytes\s+of\s+memory$")

        # 0 BGP route-map cache entries using 0 bytes of memory
        p_bgp_route_map = re.compile(r"(?P<rm>\d+)\s+BGP\s+route-map\s+cache\s+entries\s+using\s+(?P<mem>\d+)\s+bytes\s+of\s+memory$")

        # 0 BGP filter-list cache entries using 0 bytes of memory
        p_bgp_filter = re.compile(r"^(?P<filter>\d+)\s+BGP\s+filter-list\s+cache\s+entries\s+using\s+(?P<mem>\d+)\s+bytes\s+of\s+memory$")

        # BGP using 38496 total bytes of memory
        p_bgp_mem = re.compile(r"^BGP\s+using\s+(?P<mem>\d+)\s+total\s+bytes\s+of\s+memory$")

        # BGP activity 854/668 prefixes, 2572/2305 paths, scan interval 60 secs
        p_bgp_activity = re.compile(r"^BGP\s+activity\s+(?P<alloc_1>\d+)\/(?P<release_1>\d+)\s+prefixes,\s+(?P<alloc_2>\d+)\/(?P<release_2>\d+)\s+paths,\s+scan\s+interval\s+(?P<si>\d+)\s+secs$")

        # 18 networks peaked at 07:08:57 Sep 16 2020 UTC (5w2d ago)
        p_bgp_peaked = re.compile(r"^(?P<networks>\d+)\s+networks\s+peaked\s+at\s+(?P<date>[^(]+)\((?P<ago>\S+)\s+ago\)$")

        # 10.199.228.201  4        65001  202074  202468     4571    0    0 18w1d          10
        p_bgp_neighbor = re.compile(r"^(?P<neighbor>\S+)\s+(?P<v>\d+)\s+(?P<as>\d+)\s+(?P<msgr>\d+)\s+(?P<msgs>\d+)\s+(?P<tblv>\d+)\s+(?P<inq>\d+)\s+(?P<outq>\d+)\s+(?P<ud>\S+)\s+(?P<state>\d+)$")

        bgp_dict = {}

        for line in output.splitlines():
            line = line.strip()
            if p_bgp_router.match(line):
                # BGP router identifier 10.19.228.213, local AS number 64106
                m_bgp_router = p_bgp_router.match(line)
                bgp_dict.update({ "rid": m_bgp_router.group("rid") })
                bgp_dict.update({ "local_as": int(m_bgp_router.group("as")) })
                continue
            elif p_bgp_table.match(line):
                # BGP table version is 4571, main routing table version 4571
                m_bgp_table = p_bgp_table.match(line)
                bgp_dict.update({ "table_version": int(m_bgp_table.group("tv")) })
                bgp_dict.update({ "main_routing_table_version": int(m_bgp_table.group("tv")) })
                continue
            elif p_bgp_network.match(line):
                # 69 network entries using 17664 bytes of memory
                m_bgp_network = p_bgp_network.match(line)
                bgp_dict.update({ "network_entries": int(m_bgp_network.group("ne")) })
                bgp_dict.update({ "network_entries_memory_usage_bytes": int(m_bgp_network.group("mem")) })
                continue
            elif p_bgp_paths.match(line):
                # 80 path entries using 10880 bytes of memory
                m_bgp_paths = p_bgp_paths.match(line)
                bgp_dict.update({ "path_entries": m_bgp_paths.group("pe") })
                bgp_dict.update({ "path_entries_memory_usage_bytes": int(m_bgp_paths.group("mem")) })
                continue
            elif p_bgp_multipath.match(line):
                # 11 multipath network entries and 22 multipath paths
                m_bgp_multipath = p_bgp_multipath.match(line)
                bgp_dict.update({"multipath_network_entries": int(m_bgp_multipath.group("me")) })
                bgp_dict.update({ "multipath_paths": int(m_bgp_multipath.group("multipaths")) })
                continue
            elif p_bgp_bp.match(line):
                # 33/22 BGP path/bestpath attribute entries using 9768 bytes of memory
                m_bgp_bp = p_bgp_bp.match(line)
                bgp_dict.update({ "path_attribute_entries": int(m_bgp_bp.group("path_num")) })
                bgp_dict.update({ "best_path_attribute_entries": int(m_bgp_bp.group("b_path_num")) })
                continue
            elif p_bgp_as.match(line):
                # 2 BGP AS-PATH entries using 64 bytes of memory
                m_bgp_as = p_bgp_as.match(line)
                bgp_dict.update({ "as_path_entries": int(m_bgp_as.group("as")) })
                bgp_dict.update({ "as_path_entries_memory_usage_bytes": int(m_bgp_as.group("mem")) })
                continue
            elif p_bgp_exten.match(line):
                # 5 BGP extended community entries using 120 bytes of memory
                m_bgp_exten = p_bgp_exten.match(line)
                bgp_dict.update({ "extended_community_entries": int(m_bgp_exten.group("bgp_exten")) })
                bgp_dict.update({ "extended_community_entries_memory_usage_bytes": int(m_bgp_exten.group("mem")) })
                continue
            elif p_bgp_route_map.match(line):
                # 0 BGP route-map cache entries using 0 bytes of memory
                m_bgp_route_map = p_bgp_route_map.match(line)
                bgp_dict.update({ "route_map_cache_entries": int(m_bgp_route_map.group("rm")) })
                bgp_dict.update({ "route_map_cache_entries_memory_usage_bytes": int(m_bgp_route_map.group("mem")) })
                continue
            elif p_bgp_filter.match(line):
                # BGP filter-list cache entries using 0 bytes of memory
                m_bgp_filter = p_bgp_filter.match(line)
                bgp_dict.update({ "filter_list_cache_entries": int(m_bgp_filter.group("filter")) })
                bgp_dict.update({ "filter_list_cache_entries_memory_usage_bytes": int(m_bgp_filter.group("mem")) })
                continue
            elif p_bgp_mem.match(line):
                # BGP using 38496 total bytes of memory
                m_bgp_mem = p_bgp_mem.match(line)
                bgp_dict.update({ "total_memory_usage_bytes": int(m_bgp_mem.group("mem")) })
                continue
            elif p_bgp_activity.match(line):
                m_bgp_activity = p_bgp_activity.match(line)
                bgp_dict.update({ "prefix_memory_allocation_count": int(m_bgp_activity.group("alloc_1")) })
                bgp_dict.update({ "prefix_memory_release_count": int(m_bgp_activity.group("release_1")) })
                bgp_dict.update({ "path_memory_allocation_count": int(m_bgp_activity.group("alloc_2")) })
                bgp_dict.update({ "path_memory_release_count": int(m_bgp_activity.group("release_2")) })
                continue
            elif p_bgp_peaked.match(line):
                # 18 networks peaked at 07:08:57 Sep 16 2020 UTC (5w2d ago)
                m_bgp_peaked = p_bgp_peaked.match(line)
                bgp_dict.update({ "networks_peaked" : m_bgp_peaked.group("networks") })
                bgp_dict.update({ "networks_peaked_time" : m_bgp_peaked.group("date").strip() })
                bgp_dict.update({ "time_since_network_peak" : m_bgp_peaked.group("ago") })
                continue
            elif p_bgp_neighbor.match(line):
                # 10.199.228.201  4        65001  202074  202468     4571    0    0 18w1d          10
                m_bgp_neighbor = p_bgp_neighbor.match(line)
                neighbor_dict = bgp_dict.setdefault("neighbor_ips", {}).setdefault(m_bgp_neighbor.group("neighbor"), {} )
                neighbor_dict.update({ "version": int(m_bgp_neighbor.group("v")) })
                neighbor_dict.update({ "as": int(m_bgp_neighbor.group("as")) })
                neighbor_dict.update({ "messages_received": int(m_bgp_neighbor.group("msgr")) })
                neighbor_dict.update({ "messages_sent": int(m_bgp_neighbor.group("msgs")) })
                neighbor_dict.update({ "table_version": int(m_bgp_neighbor.group("tblv")) })
                neighbor_dict.update({ "in_queue": int(m_bgp_neighbor.group("inq")) })
                neighbor_dict.update({ "out_queue": int(m_bgp_neighbor.group("outq")) })
                neighbor_dict.update({ "up_down": m_bgp_neighbor.group("ud") })
                neighbor_dict.update({ "state": int(m_bgp_neighbor.group("state")) })
                continue

        return bgp_dict
