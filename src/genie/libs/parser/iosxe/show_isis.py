
""" show_isis.py

IOSXE parsers for the following show commands:
    * show isis neighbors
    * show isis hostname
    * show isis lsp-log
    * show isis database
    * show isis database detail
    * show isis database verbose
    * show isis node
    * show isis topology
    * show isis topology {flex_algo}
    * show isis flex-algo
    * show isis flex-algo {flex_algo}
    * show isis adjacency stagger
    * show isis adjacency stagger all
    * show isis adjacency stagger detail
    * show isis rib
    * show isis rib {flex_algo}
    * show isis rib {source_ip}
    * show isis rib {source_ip} {subnet_mask}
    * show isis rib redistribution
    * show isis microloop-avoidance flex-algo {flexId}
"""

# Python
from ftplib import parse257
import re
from aiohttp import TraceConnectionQueuedEndParams

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, ListOf
from genie.libs.parser.utils.common import Common

class ShowIsisNeighborsSchema(MetaParser):
    """Schema for show isis neighbors"""
    schema = {
        'isis': {
            Any(): {
                Optional('neighbors'): {
                    Any(): {
                        'type': {
                            Any(): {
                                'interfaces': {
                                    Any(): {
                                        'circuit_id': str,
                                        'holdtime': str,
                                        'ip_address': str,
                                        'state': str,
                                    }
                                }
                            }
                        }
                    }
                },
            }
        }
    }

class ShowIsisNeighbors(ShowIsisNeighborsSchema):
    """Parser for show isis neighbors"""

    cli_command = 'show isis neighbors'
    exclude = ['holdtime']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        # Tag isis_net:
        p1 = re.compile(r'^Tag +(?P<isis_name>\S+)\s*:$')

        # LAB-9001-2      L1   Te0/0/26      10.239.7.29     UP    27       00
        # spine2-ott-lisp-c9k-127 \
        p2 = re.compile(r'^\s*((?P<system_id>\S+([^(L1L2|L1|L2)]))(\s*\\)?)?\s*((?P<type>(L1L2|L1|L2))\s+'
                        r'(?P<interface>\S+)\s+(?P<ip_address>\S+)\s+'
                        r'(?P<state>(UP|DOWN|INIT|NONE)+)\s+(?P<holdtime>\S+)\s+'
                        r'(?P<circuit_id>\S+))?$')
        
        ret_dict, tag_null, prev_sys_id = {}, True, None
        for line in out.splitlines():
            line = line.strip()

            # Tag isis_net:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                isis_name = group['isis_name']
                isis_dict = ret_dict.setdefault('isis', {}).setdefault(isis_name, {})
                tag_null = False
                continue

            # LAB-9001-2      L1   Te0/0/26      10.239.7.29     UP    27       00
            # spine2-ott-lisp-c9k-127 \
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if prev_sys_id:
                    system_id = prev_sys_id
                    prev_sys_id = None
                else:
                    system_id = group['system_id'] if group['system_id'] else None
                
                isis_type = group['type'] if group['type'] else None
                interface = Common.convert_intf_name(group['interface']) if group["interface"] else None
                ip = group['ip_address'] if group['ip_address'] else None
                state = group['state'] if group['state'] else None
                holdtime = group['holdtime'] if group['holdtime'] else None
                circuit_id = group['circuit_id'] if group['circuit_id'] else None

                if not any([system_id, isis_type, interface, ip, state, holdtime, circuit_id]):
                    continue
                elif system_id and not any([isis_type, interface, ip, state, holdtime, circuit_id]):
                    prev_sys_id = system_id
                    continue

                if tag_null:
                    neighbour_dict = ret_dict.setdefault('isis', {}).setdefault('null', {}).\
                                            setdefault('neighbors', {}).setdefault(system_id.strip(), {})
                else:
                    neighbour_dict = isis_dict.setdefault('neighbors', {}).setdefault(system_id.strip(), {})

                type_dict = neighbour_dict.setdefault('type', {}).setdefault(isis_type, {})
                interfaces_dict = type_dict.setdefault('interfaces', {}).setdefault(interface, {})

                interfaces_dict['ip_address'] = ip
                interfaces_dict['state'] = state
                interfaces_dict['holdtime'] = holdtime
                interfaces_dict['circuit_id'] = circuit_id

                continue

        return ret_dict

class ShowIsisHostnameSchema(MetaParser):
    """Schema for show isis hostname"""

    schema = {
        'tag': {
            Any(): {
                Optional('hostname_db'): {
                    'hostname': {
                        Any(): {
                            'hostname': str,
                            Optional('level'): int,
                            Optional('local_router'): bool,
                        },
                    }
                }
            },
        }
    }

class ShowIsisHostname(ShowIsisHostnameSchema):
    """Parser for show isis hostname"""

    cli_command = 'show isis hostname'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        #  Level  System ID      Dynamic Hostname  (VRF1)
        p1 = re.compile(r'^Level +System +ID +Dynamic +Hostname +'
                        r'\((?P<tag>\w+)\)$')
        #  2     7777.77ff.eeee R7
        #      * 2222.22ff.4444 R2
        #      * 2001:0db8:85a3:0000:0000:8a2e:0370:7334.
        p2 = re.compile(r'^(?P<level>\d+)?(\s?(?P<star>\*))? +'
                        r'(?P<system_id>[a-zA-Z\d\.\:]+) +(?P<dynamic_hostname>\w+)$')

        for line in out.splitlines():
            line = line.strip()

            #  Level  System ID      Dynamic Hostname  (VRF1)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tag_dict = result_dict.setdefault('tag', {})\
                    .setdefault(group['tag'],{})
                continue

            #  2     7777.77ff.eeee R7
            #      * 2001:0db8:85a3:0000:0000:8a2e:0370:7334.
            m = p2.match(line)
            if m:
                group = m.groupdict()
                hostname_dict = tag_dict.setdefault('hostname_db', {}).\
                                         setdefault('hostname', {}).\
                                         setdefault(group['system_id'], {})
                hostname_dict.update({'hostname': group['dynamic_hostname']})
                if group['level']:
                    hostname_dict.update({'level': int(group['level'])})
                if group['star']:
                    hostname_dict.update({'local_router': True})
                continue

        return result_dict

class ShowIsisLspLogSchema(MetaParser):
    """Schema for show isis lsp-log"""

    schema = {
        'tag': {
            Any(): {
                'lsp_log': {
                    'level': {
                        Any(): {
                            'index': {
                                Any(): {
                                    'triggers': str,
                                    'when': str,
                                    'count': int,
                                    Optional('interface'): str,
                                },
                            },
                        },
                    },
                }
            },
        }
    }

class ShowIsisLspLog(ShowIsisLspLogSchema):
    """Parser for show isis lsp-log"""

    cli_command = 'show isis lsp-log'
    exclude = ['when']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        #  Tag VRF1:
        p1 = re.compile(r'^Tag +(?P<tag>\w+):$')
        #    Level 1 LSP log
        p2 = re.compile(r'^Level +(?P<level>\d+) +LSP +log$')
        # When       Count             Interface         Triggers
        # 01:13:52        5                            CONFIG OTVINFOCHG
        # 00:25:46        2         GigabitEthernet4   NEWADJ DIS
        p3 = re.compile(r'^(?P<when>[\w\:]+) +(?P<count>\d+)( +(?P<interface>[a-zA-Z]+[\d/.]+))? +(?P<triggers>[\S\ ]+)$')

        tag = "none"
        for line in out.splitlines():
            line = line.strip()

            #  Tag VRF1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tag = group['tag']
                continue

            #  Level 1 LSP log
            m = p2.match(line)
            if m:
                group = m.groupdict()
                level = int(group['level'])
                index = 1
                continue

            # When       Count             Interface         Triggers
            # 01:13:52        5                            CONFIG OTVINFOCHG
            # 00:25:46        2         GigabitEthernet4   NEWADJ DIS
            m = p3.match(line)
            if m:
                group = m.groupdict()
                tag_dict = result_dict.setdefault('tag', {}).\
                                        setdefault(tag, {}).\
                                        setdefault('lsp_log', {}). \
                                        setdefault('level', {}). \
                                        setdefault(level, {}). \
                                        setdefault('index', {}).\
                                        setdefault(index, {})

                tag_dict.update({'when': group['when']})
                tag_dict.update({'count': int(group['count'])})
                tag_dict.update({'triggers': group['triggers']})
                if group['interface']:
                    tag_dict.update({'interface': group['interface']})

                index += 1
                continue

        return result_dict

class ShowIsisDatabaseSchema(MetaParser):
    """Schema for show isis database detail"""

    schema = {
        'tag': {
            Any(): {
                'level': {
                    Any(): {
                        Any(): {
                            'lsp_sequence_num': str,
                            'lsp_checksum': str,
                            Optional('local_router'): bool,
                            'lsp_holdtime': str,
                            Optional('lsp_rcvd'): str,
                            Optional('lsp_index'): int,
                            'attach_bit': int,
                            'p_bit': int,
                            'overload_bit': int,
                            Optional('area_address'): str,
                            Optional('router_id'): str,
                            Optional("router_cap"): str,
                            Optional("d_flag"): bool,
                            Optional("s_flag"): bool,
                            Optional('nlpid'): str,
                            Optional('topology'): {
                                Any(): {
                                    'code': str,
                                },
                            },
                            Optional('hostname'): str,
                            Optional('ip_address'): str,
                            Optional('ipv6_address'): str,
                            Optional(Or("is_neighbor", "extended_is_neighbor", "mt_is_neighbor")): {
                                Any(): ListOf({
                                    "neighbor_id": str,
                                    "metric": int,
                                    Optional("adjacency_sid"): {
                                        Any() :{
                                            "f_flag": bool,
                                            "b_flag": bool,
                                            "v_flag": bool,
                                            "l_flag": bool,
                                            "s_flag": bool,
                                            "p_flag": bool,
                                            "weight": int
                                        }
                                    },
                                    Optional("local_interface_id"): int,
                                    Optional("remote_interface_id"): int,
                                    Optional("interface_ip_address"): str,
                                    Optional("neighbor_ip_address"): str,
                                    Optional("interface_ipv6_address"): str,
                                    Optional("neighbor_ipv6_address"): str,
                                    Optional("physical_link_bw"): int,
                                    Optional("admin_weight"): int,
                                    Optional('reservable_global_pool_bw'): int,
                                    Optional('unreserved_global_pool_bw'): {
                                        'bw_0': int,
                                        'bw_1': int,
                                        'bw_2': int,
                                        'bw_3': int,
                                        'bw_4': int,
                                        'bw_5': int,
                                        'bw_6': int,
                                        'bw_7': int,
                                    },
                                    Optional('uni_link_delay_avg'): {
                                        'a_bit': bool,
                                        'value': int,
                                    },
                                    Optional('uni_link_delay_min_max'): {
                                        'a_bit': bool,
                                        'min': int,
                                        'max': int,
                                    },
                                    Optional('uni_link_delay_var'): int,
                                    Optional('uni_link_loss'): {
                                        'percent': str,
                                        'anomalous': bool,
                                    },
                                    Optional("affinity"): str,
                                    Optional("extended_affinity"): list,
                                    Optional("asla"): {
                                        "l_flag": bool,
                                        "sa_length": int,
                                        "uda_length": int
                                    },
                                    Optional("standard_application"): {
                                        Any(): {
                                            Optional("bit_mask"): str,
                                            Optional("appl_spec_ext_admin_group"): list,
                                            Optional("appl_spec_admin_group"): str,
                                            Optional('appl_spec_uni_link_loss'): {
                                                'percent': str,
                                                'anomalous': bool,
                                            },
                                            Optional("appl_spec_uni_link_delay"): {
                                                "a_bit": bool,
                                                "min": int,
                                                "max": int
                                            },
                                            Optional("appl_spec_te_metric"): int
                                        }
                                    }
                                })
                            },
                            Optional(Or("ipv4_interarea_reachability", "ipv4_internal_reachability", "mt_ipv6_reachability", "ipv6_reachability")): {
                                Any(): ListOf({
                                    "ip_prefix": str,
                                    "prefix_len": str,
                                    "metric": int,
                                    Optional("source_router_id"): str,
                                    Optional("route_admin_tag"): int,
                                    Optional("prefix_attr"): {
                                        "x_flag": bool,
                                        "r_flag": bool,
                                        "n_flag": bool,
                                    },
                                    Optional("prefix_sid_index"): {
                                        Any() : {
                                            Optional("algorithm"): str,
                                            Optional("flex_algo"): int,
                                            Optional("flags"): {
                                                "r_flag": bool,
                                                "n_flag": bool,
                                                "p_flag": bool,
                                                "e_flag": bool,
                                                "v_flag": bool,
                                                "l_flag": bool,
                                            }
                                        }
                                    }
                                })
                            },
                            Optional("flex_algo"): {
                                Any() : {
                                    "metric_type": str,
                                    "alg_type": str,
                                    "priority": int,
                                    Optional("m_flag"): bool,
                                    Optional("exclude_any"): Any(),
                                    Optional("include_any"): Any(),
                                    Optional("include_all"): Any(),
                                },
                            },
                            Optional("segment_routing"): {
                                "spf": bool,
                                "strict_spf": bool,
                                "i_flag": bool,
                                "v_flag": bool,
                                "srgb_base": int,
                                "srgb_range": int,
                                "srlb_base": int,
                                "srlb_range": int,
                                "algorithms": set
                            },
                            Optional("node_msd"): int,
                        },
                    }

                }
            }
        }
    }

class ShowIsisDatabaseSuperParser(ShowIsisDatabaseSchema):
    """
        Super Parser for 
            show isis database
            show isis database detail
            show isis database verbose
    """

    cli_command = 'show isis database detail'
    exclude = ['lsp_holdtime' , 'lsp_checksum', 'lsp_sequence_num']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}
        tag = ""
        #  Tag VRF1:
        p1 = re.compile(r'^Tag +(?P<tag>\w+):$')

        # IS-IS Level-1 Link State Database:
        # IS-IS Level-1 LSP r1.00-00
        p2 = re.compile(r'^IS\-IS +Level\-(?P<level>\d+)\s+'
                        r'(Link +State +Database(:)?)?(LSP\s+(?P<host_name>\S+))?$')

        # LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd      ATT/P/OL
        # R2.00-00            * 0x00000007   0x8A6D                 403/*         1/0/0
        p3 = re.compile(
            r'^(?P<lspid>[\w\-\.]+)(\s*(?P<star>\*))?\s+(?P<lsp_seq_num>\w+)\s+'
            r'(?P<lsp_checksum>\w+)\s+(?P<lsp_holdtime>[\d\*]+)'
            r'(/(?P<lsp_rcvd>[\d\*]+))?\s+(?P<att>\d+)/(?P<p>\d+)/(?P<ol>\d+)\s*'
            r'(\((?P<lsp_index>\d+)\))?$')

        #   Area Address: 49.0001
        p4 = re.compile(r'^Area +Address: +(?P<area_address>[\w\.]+)$')

        #   NLPID:        0xCC 0x8E
        p5 = re.compile(r'^NLPID: +(?P<nlp_id>[\w\s]+)$')

        #   Topology:     IPv4 (0x0)
        #                 IPv6 (0x4002 ATT)
        p6 = re.compile(r'^(Topology: +)?(?P<topology>(IP)+[\w]+) +\((?P<code>[\w\s]+)\)$')

        #   Hostname: R2
        p7 = re.compile(r'^Hostname: +(?P<hostname>\w+)$')

        #   IP Address:   10.84.66.66
        p8 = re.compile(r'^IP +Address: +(?P<ip_address>[\d\.]+)$')

        #  Metric: 10         IS R2.01
        #  Metric: 10         IP 10.229.7.0/24
        #  Metric: 40         IS (MT-IPv6) R2.01
        #  Metric: 40         IS-Extended R2.01
        #  Metric: 10         IPv6 2001:DB8:2:2:2::2/128
        #  Metric: 10         IPv6 (MT-IPv6) 2001:DB8:20:2::/64
        p9 = re.compile(r'^Metric: +(?P<metric>\d+) +(?P<type>[\w\-]+)( +\((?P<mt_ipv6>[\w\-]+)\))? +(?P<ip>\S+)$')

        #   IPv6 Address: 2001:DB8:66:66:66::66
        p10 = re.compile(r'^IPv6 +Address: +(?P<ip_address>[\w\:]+)$')

        # Router ID:    10.1.77.77
        p11 = re.compile(r'^Router +ID: +(?P<router_id>\S+)$')

        # Flex algorithm: 128 Metric-Type: IGP Alg-type: SPF Priority: 128
        p12 = re.compile(r'^Flex algorithm:\s+(?P<flex_algo>\d+)\s+Metric-Type:\s+'
                         r'(?P<metric_type>\S+)\s+Alg-type:\s+(?P<alg_type>\S+)\s+'
                         r'Priority:\s+(?P<priority>\d+)$')

        #   M:1
        p13 = re.compile(r'^M:\s*(?P<m_flag>0|1)$')

        # Router CAP:   1.1.1.1, D:0, S:0
        p14 = re.compile(r'^Router CAP:\s+(?P<router_cap>[\d+\.]+),\s+D:\s*(?P<d_flag>0|1)'
                         r',\s+S:\s*(?P<s_flag>0|1)$')

        # Segment Routing: I:1 V:0, SRGB Base: 16000 Range: 8000
        p15 = re.compile(r'^Segment\s+Routing:\s+I:(?P<i_flag>0|1)\s+'
                         r'V:(?P<v_flag>0|1),\s+SRGB\s+Base:\s+(?P<srgb_base>\d+)'
                         r'\s+Range:\s+(?P<srgb_range>\d+)$')

        # Segment Routing Local Block: SRLB Base: 15000 Range: 1000
        p16 = re.compile(r'^Segment\s+Routing\s+Local\s+Block:\s+SRLB Base:\s+'
                         r'(?P<srlb_base>\d+)\s+Range:\s+(?P<srlb_range>\d+)$')

        # Segment Routing Algorithms: SPF, Strict-SPF, Flex-algo 128
        p17 = re.compile(r'^Segment\s+Routing\s+Algorithms:\s+((?P<spf>SPF)?)'
                         r',\s+((?P<strict_spf>Strict-SPF)?),\s+Flex-algo\s+'
                         r'(?P<flex_id>\d+)$')

        # Segment Routing Algorithms: Flex-algo 129, Flex-algo 130, Flex-algo 131
        p18 = re.compile(r'^Segment\s+Routing\s+Algorithms:\s+Flex-algo\s+'
                         r'(?P<flex_id_1>\d+)((,\s+Flex-algo\s+(?P<flex_id_2>\d+))?)'
                         r'((,\s+Flex-algo\s+(?P<flex_id_3>\d+))?)$')

        # Node-MSD 
        # MSD: 16
        p19 = re.compile(r'^MSD:\s+(?P<msd>\d+)$')

        # Prefix-attr: X:0 R:0 N:0
        p20 = re.compile(r'^Prefix-attr: X:\s*(?P<x_flag>0|1)\s+R:\s*'
                         r'(?P<r_flag>0|1)\s+N:\s*(?P<n_flag>0|1)$')

        # Adjacency SID Value:16 F:0 B:0 V:1 L:1 S:0 P:0 Weight:0
        p21 = re.compile(r'^Adjacency SID Value:\s*(?P<adj_sid>\d+)\s+'
                         r'F:\s*(?P<f_flag>0|1)\s+B:\s*(?P<b_flag>0|1)\s+'
                         r'V:\s*(?P<v_flag>0|1)\s+L:\s*(?P<l_flag>0|1)\s+'
                         r'S:\s*(?P<s_flag>0|1)\s+P:\s*(?P<p_flag>0|1)\s+'
                         r'Weight:\s*(?P<weight>0|1)$')

        # Local Interface ID: 1, Remote Interface ID: 1
        p22 = re.compile(r'^Local\s+Interface\s+ID:\s+(?P<local_intrf_id>\d+),\s+'
                         r'Remote\s+Interface\s+ID:\s+(?P<remote_intrf_id>\d+)$')

        # Neighbor IP Address: 12.12.12.2
        p23 = re.compile(r'^Neighbor\s+IP\s+Address:(?P<neighbor_ip>[\d\.]+)$')

        # Admin. Weight: 10
        p24 = re.compile(r'^Admin.\s+Weight:\s+(?P<admin_weight>\d+)$')

        # Physical LINK BW: 10000 kbits/sec
        p25 = re.compile(r'^Physical\s+LINK\s+BW:\s+(?P<physical_link_bw>\d+)\.+$')

        # Interface IPV6 Address: 12:12::1
        p26 = re.compile(r'^Interface\s+IPV6\s+Address:\s+(?P<intrf_ipv6>\S+)$')

        # Neighbor IPV6 Address: 12:12::2
        p27 = re.compile(r'^Neighbor\s+IPV6\s+Address:\s+(?P<neighbor_ipv6>\S+)$')

        # Route Admin Tag: 30
        p28 = re.compile(r'^Route\s+Admin\s+Tag:\s+(?P<route_admin_tag>\d+)$')

        # Prefix-SID Index: 1, Algorithm: SPF, R:0 N:1 P:0 E:0 V:0 L:0
        p29 = re.compile(r'^Prefix-SID Index:\s+(?P<prefix_sid_index>\d+),\s+'
                         r'Algorithm:\s+((?P<algo>SPF|Strict-SPF),)?(Flex-algo'
                         r'\s+(?P<flex_algo>\d+),)?\s+R:(?P<r_flag>0|1)\s+'
                         r'N:(?P<n_flag>0|1)\s+P:(?P<p_flag>0|1)\s+'
                         r'E:(?P<e_flag>0|1)\s+V:(?P<v_flag>0|1)\s+'
                         r'L:(?P<l_flag>0|1)$')

        # Source Router ID: 1.1.1.1
        p30 = re.compile(r'^Source\s+Router\s+ID:\s+(?P<source_router_id>[\d\.]+)$')

        # Reservable Global Pool BW: 0 kbits/sec 
        p31 = re.compile(r'^Reservable Global Pool BW:\s+(?P<reservable_gpbw>\d+)\s+kbits/sec$')

        # Global Pool BW Unreserved:
        # [0]:        0 kbits/sec, [1]:        0 kbits/sec
        p32 = re.compile(r'^\[(?P<index_1>\d)\]:\s+(?P<bit_1>\d+)\s+kbits/sec,\s+'
                         r'\[(?P<index_2>\d)\]:\s+(?P<bit_2>\d+)\s+kbits/sec$')

        # Uni Link Delay(Avg.) A-bit:0 Value:113
        p33 = re.compile(r'^Uni Link Delay(Avg.)\s+A-bit:\s*(?P<a_bit>0|1)\s+'
                         r'Value:\s*(?P<value>\d+)$')

        # Uni Link Delay(Min/Max) A-bit:0 Min:93 Max:160
        p34 = re.compile(r'^Uni Link Delay(Min/Max) A-bit:\s*(?P<a_bit>0|1)\s+'
                         r'Min:\s*(?P<min>\d+)\s+Max:\s*(?P<max>\d+)$')

        # Uni Link Delay(Var.) Value:12 
        p35 = re.compile(r'^Uni Link Delay(Var.) Value:\s*(?P<uni_link_delay>\d+)$')
        
        # ASLA: L flag: 0, SA-Length 1, UDA-Length 0
        p36 = re.compile(r'^ASLA: L flag:\s*(?P<l_flag>0|1),\s+SA-Length\s*'
                         r'(?P<sa_length>\d+),\s+UDA-Length\s*(?P<uda_length>\d+)$')

        # Standard Applications:  FLEX-ALGO
        p37 = re.compile(r'^Standard Applications:\s+(?P<standard_app>\S+)$')

        #  Bit mask:  0x10
        p38 = re.compile(r'^Bit mask:\s+(?P<bit_mask>\S+)$')

        #  Appl spec Uni Link Delay(Min/Max) A-bit:0 Min:100 Max:100
        p39 = re.compile(r'^Appl spec Uni Link Delay(Min/Max) A-bit:\s*'
                         r'(?P<a_bit>0|1)\s+Min:\s*(?P<min>\d+)\s+Max:\s*(?P<max>\d+)$')

        #  Appl spec Ext Admin Group:
        #     0x00000000 0x00000000 0x00000000 0x00000000
        #     0x00000000 0x00000000 0x00000000 0x80000000
        p40 = re.compile(r'^Appl spec Ext Admin Group:$')

        #  Appl spec Admin Group: 0x00000001
        p41 = re.compile(r'^Appl spec Admin Group:\s+(?P<appl_spec_ag>\S+)$')

        # Affinity: 0x00000000
        p42 = re.compile(r'^Affinity:\s+(?P<affinity>\S+)$')

        # Extended Affinity:
        #    0x00000000 0x00000000 0x00000000 0x00000000
        #    0x00000000 0x00000000 0x00000200
        p43 = re.compile(r'^Extended Affinity:$')

        #   Flex-algo Exclude-any Ext Admin Group:
        #    0x00000000 0x00000000 0x00000000 0x00000000
        #    0x00000000 0x00000000 0x00000200
        p44 = re.compile(r'^Flex-algo Exclude-any Ext Admin Group:$')

        #   Flex-algo Include-any Ext Admin Group:
        #    0x00000000 0x00000000 0x00000000 0x00000000
        #    0x00000000 0x00000000 0x00000200
        p45 = re.compile(r'^Flex-algo Include-any Ext Admin Group:$')

        #   Flex-algo Include-all Ext Admin Group:
        #    0x00000000 0x00000000 0x00000000 0x00000000
        #    0x00000000 0x00000000 0x00000200
        p46 = re.compile(r'^Flex-algo Include-all Ext Admin Group:$')

        #    0x00000000
        #    0x00000000 0x00000000
        #    0x00000000 0x00000000 0x00000200
        #    0x00000000 0x00000000 0x00000000 0x00000000
        p47 = re.compile(r'^(?P<hex>(0x\w{8}\s*){1,4})$')

        # Uni Link Loss 0.799998% 
        # Uni Link Loss 0.799998% (Anomalous)         
        p48 = re.compile(r'^Uni Link Loss\s+(?P<loss>\S+)%(\s+\((?P<anomalous>Anomalous)\))?$')

        # Appl spec Uni Link Loss 0.899997% (Anomalous)
        p49 = re.compile(r'^Appl spec Uni Link Loss\s+(?P<loss>\S+)%(\s+\((?P<anomalous>Anomalous)\))?$')

        # Appl spec Admin. Weight: 10
        p50 = re.compile(r'^Appl spec Admin.\s+Weight:\s+(?P<appl_spec_te_metric>\d+)$')

        in_extended_affinity = False
        in_include_all = False
        in_exclude_any = False
        in_include_any = False
        in_ext_admin_group = False

        for line in out.splitlines():
            line = line.strip()    

            #  Tag VRF1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tag = group['tag']
                continue

            # IS-IS Level-1 Link State Database:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                tag_dict = result_dict.setdefault('tag', {}). \
                                       setdefault(tag, {}). \
                                       setdefault('level', {}). \
                                       setdefault(int(group['level']), {})
                continue

            # LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd      ATT/P/OL
            # R2.00-00            * 0x00000007   0x8A6D                 403/*         1/0/0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                lsp_dict = tag_dict.setdefault(group['lspid'], {})
                if group['star']:
                    lsp_dict.update({'local_router': True})
                lsp_dict.update({'lsp_sequence_num': group['lsp_seq_num']})
                lsp_dict.update({'lsp_checksum': group['lsp_checksum']})
                lsp_dict.update({'lsp_holdtime': group['lsp_holdtime']})
                if group['lsp_rcvd']:
                    lsp_dict.update({'lsp_rcvd': group['lsp_rcvd']})
                lsp_dict.update({'attach_bit': int(group['att'])})
                lsp_dict.update({'p_bit': int(group['p'])})
                lsp_dict.update({'overload_bit': int(group['ol'])})
                if group['lsp_index']:
                    lsp_dict.update({'lsp_index': int(group['lsp_index'])})
                continue

            #   Area Address: 49.0001
            m = p4.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.update({"area_address": group['area_address']})
                continue

            #   NLPID:        0xCC 0x8E
            m = p5.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.update({"nlpid": group['nlp_id']})
                continue

            #   Topology:     IPv4 (0x0)
            #                 IPv6 (0x4002 ATT)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.setdefault('topology', {}).setdefault(group['topology'].lower(), {}).update({'code': group['code']})
                continue

            #   Hostname: R2
            m = p7.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.update({'hostname': group['hostname']})
                continue

            #   IP Address:   10.84.66.66
            m = p8.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.update({'ip_address': group['ip_address']})
                continue

            #  Metric: 10         IS R2.01
            #  Metric: 10         IP 10.229.7.0/24
            #  Metric: 10         IP-Interarea 10.229.7.0/24
            #  Metric: 40         IS (MT-IPv6) R2.01
            #  Metric: 40         IS-Extended R2.01
            #  Metric: 10         IPv6 2001:DB8:2:2:2::2/128
            #  Metric: 10         IPv6 (MT-IPv6) 2001:DB8:20:2::/64
            m = p9.match(line)
            if m:
                group = m.groupdict()
                mtype = group['type']
                mt_ipv6 = group['mt_ipv6']
                ip = group['ip']

                if mtype.startswith('IS'):
                    if mtype == 'IS-Extended':
                        is_list = lsp_dict.setdefault('extended_is_neighbor', {}).setdefault(ip, [])
                    elif mtype == 'IS' and mt_ipv6:
                        is_list = lsp_dict.setdefault('mt_is_neighbor', {}).setdefault(ip, [])
                    elif mtype == 'IS':
                        is_list = lsp_dict.setdefault('is_neighbor', {}).setdefault(ip, [])

                    is_list.append({'neighbor_id': ip,
                                    'metric': int(group['metric'])})

                if mtype.startswith('IP'):
                    if mtype == 'IP':
                        is_list = lsp_dict.setdefault('ipv4_internal_reachability', {}).setdefault(ip, [])
                    elif mtype == 'IP-Interarea':
                        is_list = lsp_dict.setdefault('ipv4_interarea_reachability', {}).setdefault(ip, [])
                    elif mtype == 'IPv6' and mt_ipv6:
                        is_list = lsp_dict.setdefault('mt_ipv6_reachability', {}).setdefault(ip, [])
                    elif mtype == 'IPv6':
                        is_list = lsp_dict.setdefault('ipv6_reachability', {}).setdefault(ip, [])

                    ip_prefix, prefix_len = ip.split('/')

                    is_list.append({'ip_prefix': ip_prefix,
                                    'prefix_len': prefix_len,
                                    'metric': int(group['metric'])})
                continue

            #   IPv6 Address: 2001:DB8:66:66:66::66
            m = p10.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.update({'ipv6_address': group['ip_address']})
                continue

            #  Router ID:    10.1.77.77
            m = p11.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.update({'router_id': group['router_id']})
                continue

            # Flex algorithm: 128 Metric-Type: IGP Alg-type: SPF Priority: 128
            m = p12.match(line)
            if m:
                group = m.groupdict()
                flex_algo_dict = lsp_dict.setdefault("flex_algo", {}).\
                                          setdefault(int(group["flex_algo"]), {})
                flex_algo_dict["metric_type"] = group["metric_type"]
                flex_algo_dict["alg_type"] = group["alg_type"]
                flex_algo_dict["priority"] = int(group["priority"])
                continue

            #   M:1
            m = p13.match(line)
            if m:
                group = m.groupdict()
                flex_algo_dict["m_flag"] = group["m_flag"] == "1"
                continue

            # Router CAP:   1.1.1.1, D:0, S:0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                lsp_dict["router_cap"] = group["router_cap"]
                lsp_dict["d_flag"] = group["d_flag"] == "1"
                lsp_dict["s_flag"] = group["s_flag"] == "1"
                continue

            # Segment Routing: I:1 V:0, SRGB Base: 16000 Range: 8000
            m = p15.match(line)
            if m:
                group = m.groupdict()
                sr_dict = lsp_dict.setdefault("segment_routing", {})
                sr_dict["i_flag"] = group["i_flag"] == "1"
                sr_dict["v_flag"] = group["v_flag"] == "1"
                sr_dict["srgb_base"] = int(group["srgb_base"])
                sr_dict["srgb_range"] = int(group["srgb_range"])
                continue

            # Segment Routing Local Block: SRLB Base: 15000 Range: 1000
            m = p16.match(line)
            if m:
                group = m.groupdict()
                sr_dict["srlb_base"] = int(group["srlb_base"])
                sr_dict["srlb_range"] = int(group["srlb_range"]) 
                continue     

            # Segment Routing Algorithms: SPF, Strict-SPF, Flex-algo 128
            m = p17.match(line)
            if m:
                group = m.groupdict()
                sr_dict["spf"] = True if group["spf"] else False
                sr_dict["strict_spf"] = True if group["strict_spf"] else False
                sr_dict["algorithms"] = set()
                sr_dict["algorithms"].add(int(group["flex_id"]))
                continue
            
            # Segment Routing Algorithms: Flex-algo 129, Flex-algo 130, Flex-algo 131
            m = p18.match(line)
            if m:
                group = m.groupdict()
                sr_dict["algorithms"].add(int(group["flex_id_1"]))
                if group["flex_id_2"]:
                    sr_dict["algorithms"].add(int(group["flex_id_2"]))
                if group["flex_id_3"]:
                    sr_dict["algorithms"].add(int(group["flex_id_3"]))
                continue

            # Node-MSD 
            # MSD: 16
            m = p19.match(line)
            if m:
                group = m.groupdict()
                lsp_dict["node_msd"] = int(group["msd"])
            
            # Prefix-attr: X:0 R:0 N:0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                prefix_attr = {
                    "x_flag": (group['x_flag'] == "1"),
                    "r_flag": (group['r_flag'] == "1"),
                    "n_flag": (group['n_flag'] == "1")
                }

                is_list[-1].setdefault("prefix_attr", prefix_attr)
                continue

            # Adjacency SID Value:16 F:0 B:0 V:1 L:1 S:0 P:0 Weight:0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                adj_sid_flags = {
                    "f_flag": group["f_flag"] == "1",
                    "b_flag": group["b_flag"] == "1",
                    "v_flag": group["v_flag"] == "1",
                    "l_flag": group["l_flag"] == "1",
                    "s_flag": group["s_flag"] == "1",
                    "p_flag": group["p_flag"] == "1",
                    "weight": int(group["weight"])
                }
                is_list[-1].setdefault("adjacency_sid", {}).\
                        setdefault(int(group["adj_sid"]), adj_sid_flags)
                continue

            # Local Interface ID: 1, Remote Interface ID: 1
            m = p22.match(line)
            if m:
                group = m.groupdict()
                is_list[-1]["local_interface_id"] = int(group["local_intrf_id"])
                is_list[-1]["remote_interface_id"] = int(group["remote_intrf_id"])
                continue

            # Neighbor IP Address: 12.12.12.2
            m = p23.match(line)
            if m:
                group = m.groupdict()
                is_list[-1]["neighbor_ip_address"] = group["neighbor_ip_address"]
                continue
            
            # Admin. Weight: 10
            m = p24.match(line)
            if m:
                group = m.groupdict()
                is_list[-1]["admin_weight"] = int(group["admin_weight"])
                continue

            # Physical LINK BW: 10000 kbits/sec
            m = p25.match(line)
            if m:
                group = m.groupdict()
                is_list[-1]["physical_link_bw"] = group["physical_link_bw"]
                continue
            
            # Interface IPV6 Address: 12:12::1
            m = p26.match(line)
            if m:
                group = m.groupdict()
                is_list[-1]["interface_ipv6_address"] = group["intrf_ipv6"]
                continue

            # Neighbor IPV6 Address: 12:12::2
            m = p27.match(line)
            if m:
                group = m.groupdict()
                is_list[-1]["neighbor_ipv6_address"] = group["neighbor_ipv6"]
                continue

            # Route Admin Tag: 30
            m = p28.match(line)
            if m:
                group = m.groupdict()
                is_list[-1]["route_admin_tag"] = int(group["route_admin_tag"])
                continue

            # Prefix-SID Index: 1, Algorithm: SPF, R:0 N:1 P:0 E:0 V:0 L:0
            # Prefix-SID Index: 128, Algorithm: Flex-algo 128, R:0 N:1 P:0 E:0 V:0 L:0
            m = p29.match(line)
            if m:
                group = m.groupdict()
                prefix_sid_dict = is_list[-1].setdefault("prefix_sid_index", {}).\
                                          setdefault(int(group["prefix_sid_index"]), {})
                if group["algo"]:
                    prefix_sid_dict["algorithm"] = group["algo"]
                if group["flex_algo"]:
                    prefix_sid_dict["flex_algo"] = int(group["flex_algo"])
                flags =  {
                    "r_flag": group["r_flag"] == "1",
                    "n_flag": group["n_flag"] == "1",
                    "p_flag": group["p_flag"] == "1",
                    "e_flag": group["e_flag"] == "1",
                    "v_flag": group["v_flag"] == "1",
                    "l_flag": group["l_flag"] == "1",
                }
                prefix_sid_dict.setdefault("flags", flags)
                continue

            # Source Router ID: 1.1.1.1
            m = p30.match(line)
            if m:
                group = m.groupdict()
                is_list[-1]["source_router_id"] = group["source_router_id"]
                continue

            # Reservable Global Pool BW: 0 kbits/sec 
            m = p31.match(line)
            if m:
                group = m.groupdict()
                is_list[-1]["reservable_global_pool_bw"] = int(group["reservable_gpbw"])
                continue

            # [0]:        0 kbits/sec, [1]:        0 kbits/sec
            m = p32.match(line)
            if m:
                group = m.groupdict()
                is_list[-1].setdefault("unreserved_global_pool_bw", {})
                is_list[-1]["unreserved_global_pool_bw"]["bw_" + group["index_1"]] = int(group["bit_1"])
                is_list[-1]["unreserved_global_pool_bw"]["bw_" + group["index_2"]] = int(group["bit_2"])
                continue

            # Uni Link Delay(Avg.) A-bit:0 Value:113
            m = p33.match(line)
            if m:
                group = m.groupdict()
                is_list[-1]["uni_link_delay_avg"] = {
                    "a_bit": (group["a_bit"] == "1"),
                    "value": int(group["value"])
                }
                continue

            # Uni Link Delay(Min/Max) A-bit:0 Min:93 Max:160
            m = p34.match(line)
            if m:
                group = m.groupdict()
                is_list[-1]["uni_link_delay_min_max"] = {
                    "a_bit": (group["a_bit"] == "1"),
                    "min": int(group["min"]),
                    "max": int(group["max"])
                }
                continue

            # Uni Link Delay(Var.) Value:12 
            m = p35.match(line)
            if m:
                group = m.groupdict()
                is_list[-1]["uni_link_delay_var"] = int(group["uni_link_delay"])
                continue

            # ASLA: L flag: 0, SA-Length 1, UDA-Length 0
            m = p36.match(line)
            if m:
                group = m.groupdict()
                is_list[-1]["asla"] = {
                    "l_flag": (group["l_flag"] == "1"),
                    "sa_length": int(group["sa_length"]),
                    "uda_length": int(group["uda_length"])
                }
                continue

            # Standard Applications:  FLEX-ALGO
            m = p37.match(line)
            if m:
                group = m.groupdict()
                standard_app_dict = is_list[-1].setdefault("standard_application", {}).\
                                            setdefault(group["standard_app"], {})
                continue

            #  Bit mask:  0x10
            m = p38.match(line)
            if m:
                group = m.groupdict() 
                standard_app_dict["bit_mask"] = group["bit_mask"] 
                continue

            #  Appl spec Uni Link Delay(Min/Max) A-bit:0 Min:100 Max:100
            m = p39.match(line)
            if m:
                group = m.groupdict() 
                standard_app_dict["appl_spec_uni_link_delay"] = {
                    "a_bit": (group["a_bit"] == "1"),
                    "min": int(group["min"]),
                    "max": int(group["max"])
                } 
                continue

            #  Appl spec Admin Group: 0x00000001
            m = p41.match(line)
            if m:
                group = m.groupdict() 
                standard_app_dict["appl_spec_admin_group"] = group["appl_spec_ag"]
                continue

            # Affinity: 0x00000000
            m = p42.match(line)
            if m:
                group = m.groupdict() 
                is_list[-1]["affinity"] = group["affinity"]
                continue

            #    0x00000000
            #    0x00000000 0x00000000
            #    0x00000000 0x00000000 0x00000200
            #    0x00000000 0x00000000 0x00000000 0x00000000
            m = p47.match(line)
            if m:
                group = m.groupdict()
                if in_ext_admin_group:
                    standard_app_dict["appl_spec_ext_admin_group"]. \
                        append(group["hex"])
                elif in_extended_affinity:
                    is_list[-1]["extended_affinity"].append(group["hex"])
                elif in_exclude_any:
                    flex_algo_dict["exclude_any"].append(group["hex"])
                elif in_include_any:
                    flex_algo_dict["include_any"].append(group["hex"])
                elif in_include_all:
                    flex_algo_dict["include_all"].append(group["hex"])
                continue
            else:
                in_extended_affinity = False
                in_include_all = False
                in_exclude_any = False
                in_include_any = False
                in_ext_admin_group = False

            #  Appl spec Ext Admin Group:
            m = p40.match(line)
            if m:
                in_ext_admin_group = True
                standard_app_dict["appl_spec_ext_admin_group"] = []
                continue

            # Extended Affinity:
            m = p43.match(line)
            if m:
                in_extended_affinity = True
                is_list[-1]["extended_affinity"] = []
                continue
                
            #   Flex-algo Exclude-any Ext Admin Group:
            m = p44.match(line)
            if m:
                in_exclude_any = True
                flex_algo_dict["exclude_any"] = []
                continue

            #   Flex-algo Include-any Ext Admin Group:
            m = p45.match(line)
            if m:
                in_include_any = True  
                flex_algo_dict["include_any"] = []
                continue    

            #   Flex-algo Include-all Ext Admin Group:
            m = p46.match(line)
            if m:
                in_include_all = True 
                flex_algo_dict["include_all"] = []
                continue

            # Uni Link Loss 0.799998% 
            # Uni Link Loss 0.799998% (Anomalous)    
            m = p48.match(line)
            if m:
                group = m.groupdict()
                is_list[-1]["uni_link_loss"] = {
                    "percent": group["loss"],
                    "anomalous": False
                }
                if group["anomalous"]:
                    is_list[-1]["uni_link_loss"]["anomalous"] = True
                continue 

            # Appl spec Uni Link Loss 0.899997% (Anomalous)
            # Appl spec Uni Link Loss 0.899997%
            m = p49.match(line)
            if m:
                group = m.groupdict()
                standard_app_dict["appl_spec_uni_link_loss"] = {
                    "percent": group["loss"],
                    "anomalous": False
                }
                if group["anomalous"]:
                    standard_app_dict["appl_spec_uni_link_loss"]["anomalous"] = True
                continue 
            
            # Appl spec Admin. Weight: 10
            m = p50.match(line)
            if m:
                group = m.groupdict()
                standard_app_dict["appl_spec_te_metric"] = int(group["appl_spec_te_metric"])
                continue
            
        return result_dict

class ShowIsisDatabase(ShowIsisDatabaseSuperParser, ShowIsisDatabaseSchema):

    cli_command = 'show isis database'
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
            
        return super().cli(output=output)
        
class ShowIsisDatabaseVerbose(ShowIsisDatabaseSuperParser, ShowIsisDatabaseSchema):

    cli_command = 'show isis database verbose'
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
            
        return super().cli(output=output)
class ShowIsisDatabaseDetail(ShowIsisDatabaseSuperParser, ShowIsisDatabaseSchema):

    cli_command = 'show isis database detail'
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
            
        return super().cli(output=output)

class ShowRunSectionIsisSchema(MetaParser):
    """Schema for show run | sec isis"""

    schema = {
        'instance':{
            Any(): {
                'vrf': {
                    Any():{}
                }
            }
        }
    }

class ShowRunSectionIsis(ShowRunSectionIsisSchema):
    """Parser for show run | sec isis"""

    cli_command = 'show run | sec isis'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        # router isis VRF1
        p1 = re.compile(r'^router +isis *(?P<instance>\S*)$')
        # vrf VRF1
        p2 = re.compile(r'^vrf +(?P<vrf>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # router isis VRF1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                instance = group['instance'] if group['instance'] else ''
                tag_dict = result_dict\
                    .setdefault('instance', {})\
                    .setdefault(instance,{})
                continue

            # vrf VRF1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                vrf_dict = tag_dict.setdefault('vrf', {}).\
                                         setdefault(group['vrf'], {})
                continue

        if result_dict:
            for k in result_dict['instance']:
                if 'vrf' not in result_dict['instance'][k]:
                    result_dict['instance'][k].setdefault('vrf',{}).setdefault('default' ,{})

        return result_dict

class ShowIsisNodeSchema(MetaParser):
    '''schema for show isis node'''
    schema = {
        "tag": {
            Any(): {
                Optional("level"): {
                    Any(): {
                        "hosts": {
                            Any(): {
                                Optional("ip_router_id"): str,
                                Optional("ip_router_lsp"): int,
                                Optional("ip_interface_address"): str,
                                Optional("ip_interface_address_lsp"): int,
                                Optional("ip_pq_address"): str,
                                Optional("ip_prefix_sid"): {
                                    "id": int,
                                    "r_flag": int,
                                    "n_flag": int,
                                    "p_flag": int,
                                    "e_flag": int,
                                    "v_flag": int,
                                    "l_flag": int
                                },
                                Optional("ip_strict_spf_sid"): {
                                    "id": int,
                                    "r_flag": int,
                                    "n_flag": int,
                                    "p_flag": int,
                                    "e_flag": int,
                                    "v_flag": int,
                                    "l_flag": int
                                },
                                Optional("adj_sid"): {
                                    Any(): {
                                        "lsp": int,
                                        "from_host": str,
                                        "to_host": str,
                                    }
                                },
                                "lsp_index": int,
                                Optional("srgb"): {
                                    "start": int,
                                    "range": int,
                                    "lsp": int
                                },
                                Optional("srlb"): {
                                    "start": int,
                                    "range": int,
                                    "lsp": int
                                },
                                "capability": {
                                    "sr": str,
                                    "strict_spf": str,
                                    Optional("lsp"): int
                                },
                                Optional("sr_endpoint"): str,
                                Optional("policy"): {
                                    "id": str,
                                    "ifnum": int,
                                    "metric": int,
                                    "flag": int
                                },
                                Optional("flex_algo"): {
                                    Any(): {
                                        "metric_type": str,
                                        "alg_type": str,
                                        "priority": int
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

class ShowIsisNode(ShowIsisNodeSchema):
    '''Parser for show isis node'''

    cli_command = 'show isis node'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        # Tag 1:
        p1 = re.compile(r'^Tag (?P<tag>\S+):$')

        # ISIS level-1 node information for R1-asr1k-43.00
        p2 = re.compile(r'^ISIS (?P<level>\S+)\s+node information for\s+(?P<host>\S+)$')

        # IP router ID: 1.1.1.1 (LSP #0)
        p3 = re.compile(r'^IP router ID: (?P<ip_router_id>\d+\.\d+\.\d+\.\d+)\s+\(LSP\s+#(?P<lsp_id>\d+)\)$')

        # IP interface address: 1.1.1.1 (LSP #0)
        p4 = re.compile(r'^IP interface address: (?P<ip_interface_address>\d+\.\d+\.\d+\.\d+)\s+\(LSP\s+#(?P<lsp_id>\d+)\)$')

        # IP PQ address: 3.3.3.3
        p5 = re.compile(r'^IP PQ address: (?P<ip_pq_address>\d+\.\d+\.\d+\.\d+)$')

        # IP prefix SID: 31, R:0 N:1 P:0 E:0 V:0 L:0
        p6 = re.compile(r'^IP prefix SID: (?P<prefix>\d+), R:(?P<r_flag>[01]) N:(?P<n_flag>[01]) P:(?P<p_flag>[01]) E:(?P<e_flag>[01]) V:(?P<v_flag>[01]) L:(?P<l_flag>[01])$')

        # IP strict-SPF SID: 131, R:0 N:1 P:0 E:0 V:0 L:0
        p7 = re.compile(r'^IP strict-SPF SID: (?P<prefix>\d+), R:(?P<r_flag>[01]) N:(?P<n_flag>[01]) P:(?P<p_flag>[01]) E:(?P<e_flag>[01]) V:(?P<v_flag>[01]) L:(?P<l_flag>[01])$')

        # Adj-sid from R1-asr1k-43.00 to R2-asr1k-33
        p8 = re.compile(r'^Adj-sid from (?P<from>\S+) to (?P<to>\S+)$')

        # adj-sid 739 (LSP #0)
        p9 = re.compile(r'^adj-sid (?P<adj_sid>\d+)\s+\(LSP\s+#(?P<lsp_id>\d+)\)$')

        # LSP index: 3
        p10 = re.compile(r'^LSP index: (?P<lsp_index>\S+)$')

        # SRGB start[0]: 16000, SRGB range[0]: 8000 (LSP #0)
        p11 = re.compile(r'^SRGB start\[0]: (?P<srgb_start>\d+), SRGB range\[0]: (?P<srgb_range>\d+)\s+\(LSP\s+#(?P<lsp_id>\d+)\)$')

        # SRLB start[0]: 15000, SRLB range[0]: 1000 (LSP #0)
        p12 = re.compile(r'^SRLB start\[0]: (?P<srlb_start>\d+), SRLB range\[0]: (?P<srlb_range>\d+)\s+\(LSP\s+#(?P<lsp_id>\d+)\)$')

        # SR capable: No, Strict-SPF capable: No (LSP #0)
        p13 = re.compile(r'^SR capable: (?P<sr_capable>\w+), Strict-SPF capable: (?P<strict_spf_capable>\w+)(\s+\(?LSP\s+#)?(?P<lsp_id>\d+)?\)?$')

        # SR end-point: 4.4.4.4
        p14 = re.compile(r'^SR end-point: (?P<sr_endpoint>\d+\.\d+\.\d+\.\d+)$')

        # Policy: Tunnel65536 ifnum 23 metric 0 flag 0
        p15 = re.compile(r'^Policy: (?P<policy>\S+) ifnum (?P<ifnum>\d+) metric (?P<metric>\d+) flag (?P<flag>\d+)$')

        # Flex algorithm:128 Metric-Type:IGP Alg-type:SPF Priority:131
        p16 =re.compile(r'^Flex algorithm:(?P<flex_algo>\d+) Metric-Type:(?P<metric>\w+) Alg-type:(?P<alg_type>\w+) Priority:(?P<priority>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Tag 1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tag = group["tag"]
                ret_dict.setdefault("tag", {}).setdefault(tag, {})
                continue

             # ISIS level-1 node information for R1-asr1k-43.00
            m = p2.match(line)
            if m:
                group = m.groupdict()
                level = group["level"]
                host = group["host"]
                ret_dict["tag"][tag].setdefault("level", {}).setdefault(level, {}).setdefault("hosts", {}).setdefault(host, {})
                continue

            # IP router ID: 1.1.1.1 (LSP #0)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["ip_router_id"] = group["ip_router_id"]
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["ip_router_lsp"] = int(group["lsp_id"])
                continue

            # IP interface address: 1.1.1.1 (LSP #0)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["ip_interface_address"] = group["ip_interface_address"]
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["ip_interface_address_lsp"] = int(group["lsp_id"])
                continue

            # IP PQ address: 3.3.3.3
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["ip_pq_address"] = group["ip_pq_address"]
                continue

            # IP prefix SID: 31, R:0 N:1 P:0 E:0 V:0 L:0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ip_prefix_sid = {
                    "id": int(group["prefix"]),
                    "r_flag": int(group["r_flag"]),
                    "n_flag": int(group["n_flag"]),
                    "p_flag": int(group["p_flag"]),
                    "e_flag": int(group["e_flag"]),
                    "v_flag": int(group["v_flag"]),
                    "l_flag": int(group["l_flag"])
                }

                ret_dict["tag"][tag]["level"][level]["hosts"][host]["ip_prefix_sid"] = ip_prefix_sid
                continue

            # IP strict-SPF SID: 131, R:0 N:1 P:0 E:0 V:0 L:0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ip_strict_spf_prefix_sid = {
                    "id": int(group["prefix"]),
                    "r_flag": int(group["r_flag"]),
                    "n_flag": int(group["n_flag"]),
                    "p_flag": int(group["p_flag"]),
                    "e_flag": int(group["e_flag"]),
                    "v_flag": int(group["v_flag"]),
                    "l_flag": int(group["l_flag"])
                }
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["ip_strict_spf_sid"] = ip_strict_spf_prefix_sid
                continue

            # Adj-sid from R1-asr1k-43.00 to R2-asr1k-33
            m = p8.match(line)
            if m:
                group = m.groupdict()
                from_host = group["from"]
                to_host = group["to"]
                continue

            # adj-sid 739 (LSP #0)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                adj_sid = int(group["adj_sid"])
                ret_dict["tag"][tag]["level"][level]["hosts"][host].setdefault("adj_sid", {}).setdefault(adj_sid, {})
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["adj_sid"][adj_sid]["lsp"] = int(group["lsp_id"])
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["adj_sid"][adj_sid]["to_host"] = to_host
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["adj_sid"][adj_sid]["from_host"] = from_host
                continue

            # LSP index: 3
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["lsp_index"] = int(group["lsp_index"])
                continue

            # SRGB start[0]: 16000, SRGB range[0]: 8000 (LSP #0)
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict["tag"][tag]["level"][level]["hosts"][host].setdefault("srgb", {})
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["srgb"]["start"] = int(group["srgb_start"])
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["srgb"]["range"] = int(group["srgb_range"])
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["srgb"]["lsp"] = int(group["lsp_id"])
                continue

            # SRLB start[0]: 15000, SRLB range[0]: 1000 (LSP #0)
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict["tag"][tag]["level"][level]["hosts"][host].setdefault("srlb", {})
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["srlb"]["start"] = int(group["srlb_start"])
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["srlb"]["range"] = int(group["srlb_range"])
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["srlb"]["lsp"] = int(group["lsp_id"])
                continue

            # SR capable: No, Strict-SPF capable: No (LSP #0)
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ret_dict["tag"][tag]["level"][level]["hosts"][host].setdefault("capability", {})
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["capability"]["sr"] = group["sr_capable"]
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["capability"]["strict_spf"] = group["strict_spf_capable"]
                if group["lsp_id"]:
                    ret_dict["tag"][tag]["level"][level]["hosts"][host]["capability"]["lsp"] = int(group["lsp_id"])
                continue

            # SR end-point: 4.4.4.4
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["sr_endpoint"] = group["sr_endpoint"]
                continue

            # Policy: Tunnel65536 ifnum 23 metric 0 flag 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                policy = {
                    "id": group["policy"],
                    "ifnum": int(group["ifnum"]),
                    "metric": int(group["metric"]),
                    "flag": int(group["flag"])
                }
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["policy"] = policy
                continue

            # Flex algorithm:128 Metric-Type:IGP Alg-type:SPF Priority:131
            m = p16.match(line)
            if m:
                group = m.groupdict()
                flex_algo = int(group["flex_algo"])
                flex_dict = {
                        "metric_type": group["metric"],
                        "alg_type": group["alg_type"],
                        "priority": int(group["priority"])
                }
                ret_dict["tag"][tag]["level"][level]["hosts"][host].setdefault("flex_algo", {}).setdefault(flex_algo, {})
                ret_dict["tag"][tag]["level"][level]["hosts"][host]["flex_algo"][flex_algo] = flex_dict
                continue

        return ret_dict

class ShowIsisAdjacencyStaggerSchema(MetaParser):
    """Schema for show isis adjacency stagger"""
    schema = {
        'tag': { 
            Any(): {
                Optional('state'): { 
                    Any(): {
                        Optional('init_nbr'): int,
                        Optional('max_nbr'): int,
                        Optional('full_exp_nbr'): int,
                        Optional('syncing_nbr'): int,
                        Optional('host'): {
                            Any(): {
                                'level': {
                                    str: { 
                                        'interface': {
                                            str: { 
                                                'state': str,
                                                'timer': str, 
                                                'csnp_rcvd': str,
                                                'init_flood': str, 
                                                'req_size': int,
                                                Optional('lsp'): {
                                                    str: {
                                                        'index': int
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
    
class ShowIsisAdjacencyStagger(ShowIsisAdjacencyStaggerSchema):
    """Parser for show isis adjacency stagger"""

    
    cli_command = 'show isis adjacency stagger'

    def cli(self, output=None):
        
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Tag name:
        p1 = re.compile(r'^Tag +(?P<isis_name>\S+)\s*:$')

        #Adjacency stagger enabled: init 2, max 64
        #Adjacency stagger disabled
        p2 = re.compile(r'^Adjacency\s+stagger\s+(?P<state>disabled|enabled)(:\s+init\s+(?P<init>\d+),?\s+max\s+(?P<max>\d+))?$')

        #Full or expired P2P nbrs: 2
        p3 = re.compile(r'^Full or expired P2P nbrs: (?P<full>\d+)$')

        #Syncing P2P nbrs: 0
        p4 = re.compile(r'^Syncing P2P nbrs: (?P<sync>\d+)$')

        #R2              L1L2 Et0/0         Full    NewCfg  yes  yes   0
        p5 = re.compile(r'^(?P<host>\w+)\s+(?P<level>L1|L2|L1L2)\s+(?P<intf>\S+)\s+(?P<state>Uninitialized|Syncing|Full|Unknown)\s+(?P<timer>Expired|Stopped|NewCfg|\d+)\s+(sec\s+)?(?P<csnp>no|yes)\s+(?P<flood>no|yes)\s+(?P<reqlist>\d+)$')

        #0200.C5F5.A202.01-00/0 0200.C5F5.A202.02-00/0 0200.C5F6.0602.00-00/0 0200.C5F6.0602.01-00/0
        p6 = re.compile(r'(\S{4}\.\S{4}\.\S{4}.\d{2}-\d{2})/(\d+)')
        for line in out.splitlines():
            line = line.strip()


            # Tag name:
            m = p1.match(line)
            if m:
                isis_name = m.groupdict()['isis_name']
                tag_dict = ret_dict.setdefault('tag', {}).setdefault(isis_name, {})
                continue

            #Adjacency stagger enabled: init 2, max 64
            #Adjacency stagger disabled
            m = p2.match(line)
            if m:
                group = m.groupdict()
                state = group['state']
                init = group['init']
                max_nbr = group['max']
                state_dict = tag_dict.setdefault('state', {}).setdefault(state, {})
                if init is not None:
                    state_dict['init_nbr'] = int(init)
                if max_nbr is not None:
                    state_dict['max_nbr'] = int(max_nbr)
                continue

            #Full or expired P2P nbrs: 2
            m = p3.match(line)
            if m:
                full = m.groupdict()['full']
                if full:
                    state_dict['full_exp_nbr'] = int(full)
                continue

            #Syncing P2P nbrs: 0
            m = p4.match(line)
            if m:
                sync = m.groupdict()['sync']
                if sync:
                    state_dict['syncing_nbr'] = int(sync)
                continue

            #R2              L1L2 Et0/0         Full    NewCfg  yes  yes   0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                host = group['host']
                level = group['level']
                intf = group['intf']
                intf_dict = state_dict.setdefault('host', {}).setdefault(host, {}).\
                            setdefault('level', {}).setdefault(level, {}).\
                            setdefault('interface', {}).setdefault(intf, {})
                intf_dict['state'] = group['state']
                intf_dict['timer'] = group['timer']
                intf_dict['csnp_rcvd'] = group['csnp']
                intf_dict['init_flood'] = group['flood']
                intf_dict['req_size'] = int(group['reqlist'])

            #0200.C5F5.A202.01-00/0 0200.C5F5.A202.02-00/0 0200.C5F6.0602.00-00/0 0200.C5F6.0602.01-00/0
            for m in p6.finditer(line):
                lsp = m.groups()[0]
                index = m.groups()[1]
                lsp_dict = intf_dict.setdefault('lsp', {}).setdefault(lsp, {})
                lsp_dict['index'] = int(index)
                
        return ret_dict

class ShowIsisAdjacencyStaggerDetail(ShowIsisAdjacencyStagger):

    cli_command = 'show isis adjacency stagger detail'
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
    
        return super().cli(output=output)

class ShowIsisAdjacencyStaggerAll(ShowIsisAdjacencyStagger):

    cli_command = 'show isis adjacency stagger all'
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
            
        return super().cli(output=output)

class ShowIsisTopologySchema(MetaParser):
    """Schema for show isis topology
                  show isis topology flex-algo {flex_id}"""
    schema = {
        "tag": {
            Any() : {
                Optional("level"): {
                    Any(): {
                        Optional("flex_algo"): int,
                        "hosts": {
                            Any(): {
                                Optional("metric"): int,
                                Optional("interface"): {
                                    Any(): {
                                        "next_hop": str,
                                        "snpa": str
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

class ShowIsisTopology(ShowIsisTopologySchema):
    '''Parser for show isis topology
                  show isis topology flex-algo {flex_id}'''

    cli_command = ['show isis topology',
                   'show isis topology flex-algo {flex_id}']

    def cli(self, flex_id="", output=None):
        if output is None:
            if flex_id:
                out = self.device.execute(self.cli_command[1].format(flex_id=flex_id))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        # Tag 1:
        p1 = re.compile(r'^Tag (?P<tag>\S+):$')

        # IS-IS TID 0 paths to level-1 routers
        p2 = re.compile(r'^.+paths to level-(?P<level>\d).+$')

        # Flex-algo 129
        p3 = re.compile(r'^Flex-algo\s+(?P<flex_algo>\d+)$')

        # R1-asr1k-43          --
        p4 = re.compile(r'^(?P<system_id>\S+)\s+(?P<metric>--+)$')

        # R2-asr1k-33          10         R2-asr1k-33          Gi0/0/2     c47d.4f12.e020
        p5 = re.compile(r'^(?P<system_id>\S+)\s+(?P<metric>\d+)\s+(?P<next_hop>\S+)\s+(?P<interface>\w+[/\d]+)\s+(?P<snpa>[\w\d]{4}.[\w\d]{4}.[\w\d]{4})$')

        #                                 R2-asr1k-33          Gi0/0/3     c47d.4f12.e021
        p6 = re.compile(r'^(?P<next_hop>\S+)\s+(?P<interface>\w+[/\d]+)\s+(?P<snpa>[\w\d]{4}.[\w\d]{4}.[\w\d]{4})$')

        for line in out.splitlines():
            line = line.strip()

            # Tag 1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tag = group["tag"]
                ret_dict.setdefault("tag", {}).setdefault(tag, {})
                continue

            # IS-IS TID 0 paths to level-1 routers
            m = p2.match(line)
            if m:
                group = m.groupdict()
                level = int(group["level"])
                ret_dict["tag"][tag].setdefault("level", {}).setdefault(level, {}).setdefault("hosts", {})
                continue

            # Flex-algo 129
            if flex_id:
                m = p3.match(line)
                if m:
                    group = m.groupdict()
                    ret_dict["tag"][tag]["level"][level]["flex_algo"] = int(group["flex_algo"])
                    continue

            # R1-asr1k-43          --
            m = p4.match(line)
            if m:
                group = m.groupdict()
                system_id = group["system_id"]
                ret_dict["tag"][tag]["level"][level]["hosts"].setdefault(system_id, {})
                continue

            # R2-asr1k-33          10         R2-asr1k-33          Gi0/0/2     c47d.4f12.e020
            m = p5.match(line)
            if m:
                group = m.groupdict()
                system_id = group["system_id"]
                metric = group["metric"]
                intrf = group["interface"]
                next_hop = group["next_hop"]
                snpa = group["snpa"]

                system_dict = {
                    "metric": int(metric),
                    "interface": {
                        intrf : {
                            "next_hop": next_hop,
                            "snpa": snpa
                        }
                    }
                }

                ret_dict["tag"][tag]["level"][level]["hosts"].setdefault(system_id, system_dict)
                continue

            #                                 R2-asr1k-33          Gi0/0/3     c47d.4f12.e021
            m = p6.match(line)
            if m:
                group = m.groupdict()
                intrf = group["interface"]
                next_hop = group["next_hop"]
                snpa = group["snpa"]
                if intrf not in ret_dict["tag"][tag]["level"][level]["hosts"][system_id]["interface"]:
                    intf_dict = {
                        "next_hop": next_hop,
                        "snpa": snpa
                    }
                    ret_dict["tag"][tag]["level"][level]["hosts"][system_id]["interface"].setdefault(intrf, intf_dict)
                continue

        return ret_dict

class ShowIsisFlexAlgoSchema(MetaParser):
    '''schema for show isis flex-algo'''
    schema = {
        "tag": {
            Any(): {
                Optional("flex_algo_count"): int,
                Optional("use_delay_metric_advertisement"): list,
                Optional("flex_algo"): {
                    Any(): {
                        "level": {
                            Any(): {
                                Optional('delay_metric'): bool,
                                Optional('def_priority'): int,
                                Optional('def_source'): str,
                                Optional('def_equal_to_local'): bool,
                                Optional('def_metric_type'): str,
                                Optional('def_prefix_metric'): bool,
                                Optional('disabled'): bool,
                                Optional("microloop_avoidance_timer_running"): bool,
                                Optional("def_include_all_affinity"): list,
                                Optional("def_include_any_affinity"): list,
                                Optional("def_exclude_any_affinity"): list,

                            }
                        },
                        Optional('local_priority'): int,
                        Optional('frr_disabled'): bool,
                        Optional('microloop_avoidance_disabled'): bool
                    }
                }
            }
        }
    }

class ShowIsisFlexAlgo(ShowIsisFlexAlgoSchema):
    '''parser for show isis flex-algo
                  show isis flex-algo {flex_id}'''

    cli_command = ['show isis flex-algo',
                   'show isis flex-algo {flex_id}']

    def cli(self, flex_id="", output=None):
        if output is None:
            if flex_id:
                out = self.device.execute(self.cli_command[1].format(flex_id=flex_id))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}
        exclude_any, include_any, include_all = False, False, False

        # Tag 1:
        p1 = re.compile(r'^Tag\s+(?P<tag>\S+):$')

        #  Flex-Algo count: 3
        p2 = re.compile(r'^Flex-Algo count:\s+(?P<count>\d+)$')

        # Flex-Algo 128:
        p3 = re.compile(r'^Flex-Algo\s+(?P<flex_algo>\d+):$')

        # IS-IS Level-1
        p4 = re.compile(r'^IS-IS Level-(?P<level>\d+)$')

        # Definition Priority: 131
        p5 = re.compile(r'^Definition Priority:\s+(?P<def_priority>\d+)$')

        # Definition Source: R6-asr1k-20.00
        p6 = re.compile(r'^Definition Source:\s+(?P<def_source>\S+)$')

        # Definition Equal to Local: Yes
        p7 = re.compile(r'^Definition Equal to Local:\s+(?P<def_equal>Yes|No)$')

        # Definition Metric Type: IGP
        p8 = re.compile(r'^Definition Metric Type:\s+(?P<def_metric_type>\S+)$')

        # Definition Flex-Algo Prefix Metric: Yes
        p9 = re.compile(r'^Definition Flex-Algo Prefix Metric:\s+(?P<def_flex_prefix_metric>Yes|No)$')

        # Disabled: No
        p10 = re.compile(r'^Disabled:\s(?P<disabled>Yes|No)$')

        # Microloop Avoidance Timer Running: No
        p11 = re.compile(r'^Microloop Avoidance Timer Running:\s+(?P<microloop_avoidance_timer>Yes|No)$')

        #    Local Priority: 128
        p12 = re.compile(r'^Local Priority:\s+(?P<local_priority>\d+)$')

        #    FRR Disabled: No
        p13 = re.compile(r'^FRR Disabled:\s+(?P<frr_disabled>Yes|No)$')

        #    Microloop Avoidance Disabled: No
        p14 = re.compile(r'^Microloop Avoidance Disabled:\s+(?P<microloop_avoidance_disabled>Yes|No)$')

        # Definition Exclude-any Affinity:
        p15 = re.compile(r'^Definition Exclude-any Affinity:$')

        # Definition Include-any Affinity:
        p16 = re.compile(r'^Definition Include-any Affinity:$')

        # Definition Include-all Affinity:
        p17 = re.compile(r'^Definition Include-all Affinity:$')

        # 0x00000000 0x00000000 0x00000000 0x00000000
        p18 = re.compile(r'^(?P<hex_val>0x\d{8})(\s+(?P<hex_val2>0x\d{8}))?(\s+(?P<hex_val3>0x\d{8}))?(\s+(?P<hex_val4>0x\d{8}))?$')

        # Use delay metric advertisement: Application, Legacy
        p19 = re.compile(r'^Use delay metric advertisement:\s+(?P<use_delay_metric_advertise>.+)$')

        #Delay metric: Active
        p20 = re.compile(r'^Delay metric:\s+(?P<delay_metric>Active|Inactive)$')

        flex_algo = None
        for line in out.splitlines():
            line = line.strip()

            # Tag 1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tag = group["tag"]
                ret_dict.setdefault("tag", {}).setdefault(tag, {}).setdefault("flex_algo", {})
                flex_algo = None
                continue

            #  Flex-Algo count: 3
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["tag"][tag]["flex_algo_count"] = int(group["count"])
                continue

            # Flex-Algo 128:
            m = p3.match(line)
            if m:
                group = m.groupdict()
                flex_algo = group["flex_algo"]
                ret_dict["tag"][tag].setdefault("flex_algo", {}).setdefault(flex_algo, {})
                ret_dict["tag"][tag]["flex_algo"][flex_algo].setdefault("level", {})
                continue

            # IS-IS Level-1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                level = group["level"]
                if flex_algo:
                    ret_dict["tag"][tag]["flex_algo"][flex_algo].setdefault("level", {}).setdefault(level, {})
                else:
                    ret_dict["tag"][tag].setdefault("flex_algo", {}).setdefault("global", {}).setdefault("level", {}).setdefault(level, {})
                continue

            # Definition Priority: 131
            m = p5.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]["flex_algo"][flex_algo]
                        ["level"][level]['def_priority']) = int(group["def_priority"])
                continue

            # Definition Source: R6-asr1k-20.00
            m = p6.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]["flex_algo"][flex_algo]
                         ["level"][level]['def_source']) = group["def_source"]
                continue

            # Definition Equal to Local: Yes
            m = p7.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]["flex_algo"][flex_algo]
                         ["level"][level]['def_equal_to_local']) = (group["def_equal"] == "Yes")
                continue

            # Definition Metric Type: IGP
            m = p8.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]["flex_algo"][flex_algo]
                         ["level"][level]['def_metric_type']) = group["def_metric_type"]
                continue

            # Definition Flex-Algo Prefix Metric: Yes
            m = p9.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]["flex_algo"][flex_algo]
                         ["level"][level]['def_prefix_metric']) = (group["def_flex_prefix_metric"] == "Yes")
                exclude_any, include_all, include_any = False, False, False
                continue

            # Disabled: No
            m = p10.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]["flex_algo"][flex_algo]
                         ["level"][level]['disabled']) = (group["disabled"] == "Yes")
                exclude_any, include_all, include_any = False, False, False
                continue

            # Microloop Avoidance Timer Running: No
            m = p11.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]["flex_algo"][flex_algo]
                         ["level"][level]
                         ['microloop_avoidance_timer_running']) = (group["microloop_avoidance_timer"] == "Yes")
                continue

            #    Local Priority: 128
            m = p12.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]
                        ["flex_algo"][flex_algo]['local_priority']) = int(group["local_priority"])
                continue

            #    FRR Disabled: No
            m = p13.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]
                         ["flex_algo"][flex_algo]['frr_disabled']) = (group["frr_disabled"] == "Yes")
                continue

            #    Microloop Avoidance Disabled: No
            m = p14.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]["flex_algo"][flex_algo]
                         ['microloop_avoidance_disabled']) = (group["microloop_avoidance_disabled"] == "Yes")
                continue

            # Definition Exclude-any Affinity:
            m = p15.match(line)
            if m:
                exclude_any, include_all, include_any = True, False, False
                (ret_dict["tag"][tag]["flex_algo"][flex_algo]
                        ["level"][level]["def_exclude_any_affinity"]) = []
                continue

            # Definition Include-any Affinity:
            m = p16.match(line)
            if m:
                exclude_any, include_all, include_any = False, False, True
                (ret_dict["tag"][tag]["flex_algo"][flex_algo]
                        ["level"][level]["def_include_any_affinity"]) = []
                continue

            # Definition Include-all Affinity:
            m = p17.match(line)
            if m:
                exclude_any, include_all, include_any = False, True, False
                (ret_dict["tag"][tag]["flex_algo"][flex_algo]
                        ["level"][level]["def_include_all_affinity"]) = []
                continue

            # 0x00000000 0x00000000 0x00000000 0x00000000
            m = p18.match(line)
            if m:
                group = m.groupdict()
                hex_vals = [val for val in group.values() if val]
                if exclude_any:
                    ret_dict["tag"][tag]["flex_algo"][flex_algo]["level"][level]["def_exclude_any_affinity"].extend(hex_vals)
                elif include_all:
                    ret_dict["tag"][tag]["flex_algo"][flex_algo]["level"][level]["def_include_all_affinity"].extend(hex_vals)
                elif include_any:
                    ret_dict["tag"][tag]["flex_algo"][flex_algo]["level"][level]["def_include_any_affinity"].extend(hex_vals)
                continue

            # Use delay metric advertisement: Application, Legacy
            m = p19.match(line)
            if m:
                group = m.groupdict()
                ret_dict["tag"][tag]["use_delay_metric_advertisement"] = group["use_delay_metric_advertise"].split(", ")
                continue

            #Delay metric: Active
            m = p20.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]["flex_algo"]["global"]
                         ["level"][level]['delay_metric']) = (group["delay_metric"] == "Active")
                continue

        return ret_dict

class ShowIsisRibSchema(MetaParser):
    schema = {
        "tag": {
            Any(): {
                "topo_type": str,
                "topo_name": str,
                "tid": int,
                "topo_id": str,
                Optional("flex_algo"): {
                    Any(): {
                        Optional("prefix") : {
                            Any() : {
                                "subnet": str,
                                Optional("prefix_attr"): {
                                    "x_flag": bool,
                                    "r_flag": bool,
                                    "n_flag": bool
                                },
                                Optional("source_router_id"): str,
                                Optional("algo"): {
                                    Any(): {
                                        Optional("sid_index"): int,
                                        Optional("bound"): bool,
                                        Optional("attribute"): str,
                                    }
                                },
                                "via_interface": {
                                    Any(): {
                                        "level": {
                                            Any(): {
                                                "source_ip": {
                                                    Any(): {
                                                        "distance": int,
                                                        "metric": int,
                                                        "via_ip": str,
                                                        Optional("host"): str,
                                                        "tag": str,
                                                        Optional("lsp"): { 
                                                            Optional("next_hop_lsp_index"): int,
                                                            Optional("rtp_lsp_index"): int,
                                                            Optional("rtp_lsp_version"): int,
                                                            Optional("tpl_lsp_version"): int
                                                        },
                                                        Optional("filtered_out"): bool, 
                                                        Optional("prefix_attr"): {
                                                            "x_flag": bool,
                                                            "r_flag": bool,
                                                            "n_flag": bool
                                                        },
                                                        Optional("source_router_id"): str,
                                                        Optional("srgb_start"): int,
                                                        Optional("srgb_range"): int,
                                                        Optional("algo"): {
                                                            Any() : {
                                                                Optional("flags"): {
                                                                    "r_flag": bool,
                                                                    "n_flag": bool,
                                                                    "p_flag": bool,
                                                                    "e_flag": bool,
                                                                    "v_flag": bool,
                                                                    "l_flag": bool
                                                                },
                                                                Optional("sid_index"): int,
                                                                Optional("label"): str,
                                                                Optional("from_srapp"): bool
                                                            }
                                                        },
                                                        Optional("u_loop_enabled"): bool,
                                                        Optional("repair_path"): {
                                                            "ip": str,
                                                            "interface": str,
                                                            Optional("stale"): bool,
                                                            Optional("next_hop_ip"): str,
                                                            Optional("next_hop_interface"): str,
                                                            "metric": int,
                                                            Optional("rtp_lsp_index"): int,
                                                            Optional("lfa_type"): str,
                                                            "attributes": {
                                                                "DS": bool,
                                                                "LC": bool,
                                                                "NP": bool,
                                                                "PP": bool,
                                                                "SR": bool
                                                            },
                                                            Optional("srgb_start"): str,
                                                            Optional("srgb_range"): str,
                                                            "algo": {
                                                                Any():{
                                                                    Optional("flags"): {
                                                                    "r_flag": bool,
                                                                    "n_flag": bool,
                                                                    "p_flag": bool,
                                                                    "e_flag": bool,
                                                                    "v_flag": bool,
                                                                    "l_flag": bool
                                                                },
                                                                Optional("sid_index"): int,
                                                                Optional("label"): str,
                                                                }
                                                            },
                                                            Optional("nodes"): {
                                                                "host" : {
                                                                    Any(): {
                                                                        "node_type": str,
                                                                        "ip": str,
                                                                        "label": str
                                                                    }
                                                                }
                                                            },
                                                            Optional("repair_source"): {
                                                                "host": str,
                                                                Optional("rtp_lsp_index"): int
                                                            }
                                                        },
                                                        Optional("path_attribute"): {
                                                            Optional("ALT"): bool,
                                                            Optional("SR_POLICY"): bool,
                                                            Optional("SR_POLICY_STRICT"): bool,
                                                            Optional("SRTE"): bool,
                                                            Optional("SRTE_STRICT"): bool,
                                                            Optional("ULOOP_EP"): bool,
                                                            Optional("TE"): bool,
                                                        },
                                                        Optional("installed"): bool,
                                                        Optional("forced"): str,
                                                        Optional("had_repair_path"): bool
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
            }
        }
    }


class ShowIsisRib(ShowIsisRibSchema):
    '''parser for show isis rib
                  show isis rib flex-algo
                  show isis rib flex-algo {flex-algo}
                  show isis rib {source_ip}
                  show isis rib {source_ip} {subnet_mask}
    '''

    cli_command = ['show isis rib',
                   'show isis rib flex-algo',
                   'show isis rib flex-algo {flex_id}',
                   'show isis rib {source_ip}',
                   'show isis rib {source_ip} {subnet_mask}']

    def cli(self, flex_id="", source_ip="", subnet_mask="", output=None):
        if output is None:
            if flex_id:
                out = self.device.execute(self.cli_command[2].format(flex_id=flex_id))
            elif source_ip and not subnet_mask:
              out = self.device.execute(self.cli_command[3].format(source_ip=source_ip))
            elif source_ip and subnet_mask:
              out = self.device.execute(self.cli_command[4].format(source_ip=source_ip, subnet_mask=subnet_mask))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        flex_algo_enabled, in_repair_path, ret_dict = False, False, {}

        # IPv4 local RIB for IS-IS process 1
        p1 = re.compile(r'^IPv4 local RIB for IS-IS process\s+(?P<tag>\S+)$')

        # 6.6.6.6/32
        # 1.1.1.0/24  prefix attr X:0 R:1 N:0
        # 3.3.3.3/32  prefix attr X:0 R:0 N:1  source router id: 3.3.3.3  SID index 3 - Bound
        # 6.6.6.6/32  prefix attr X:0 R:0 N:1  source router id: 6.6.6.6  prefix SID index 61 - Bound (SR_POLICY)
        p2 = re.compile(r'^(?P<ip>[\d.]+)/(?P<subnet>\d+)(\s+((prefix\s+attr\s+'
                        r'X:(?P<x_flag>0|1)\s+R:(?P<r_flag>0|1)\s+N:'
                        r'(?P<n_flag>0|1)))?((\((?P<strict_sid_bound_attribute_te1>TE)'
                        r'\)))?((\s*source router id:\s+(?P<src_router_id>[\d.]+))?'
                        r'\s+((((prefix SID index|SID index))\s+(?P<prefix_sid_ind>'
                        r'(\d+|Invalid by SRMS)))\s*)?(((- (?P<bound>Bound)){0,1}'
                        r'\s*(\((?P<sid_bound_attribute>\w+)\)'
                        r'(\((?P<strict_sid_bound_attribute_te2>\w+)\))?)?)?)?)?)?$')

        # [115/L1/70] via 6.6.6.6(MPLS-SR-Tunnel6) R3.00-00, from 4.4.4.4, tag 0
        # [115/L2/50] via 199.1.1.2(Tunnel4001), from 6.6.6.6, tag 0, LSP[105/209/18349]
        p3 = re.compile(r'^\[(?P<distance>\d+)/(?P<route_type>\w+(\d+)?)/'
                        r'(?P<metric>\d+)\]\s+via\s+(?P<ip>[\d.]+)'
                        r'\((?P<interface>[\w-]+\d+(\/\d+(\/\d+)?)?)\)'
                        r'( (?P<host>\S+),)?,* from (?P<from_ip>[\d.]+),\s+tag'
                        r'\s+(?P<tag>\d+)(, LSP\[(?P<next_hop_lsp_index>\d+)/'
                        r'(?P<rtp_lsp_index>\d+)/(?P<rtp_lsp_version>\d+)\])?'
                        r'(\s+(?P<filtered>-))?$')
        
        # LSP 3/4/0(52), prefix attr: X:0 R:0 N:1
        p4 = re.compile(r'^(LSP (?P<next_hop_lsp_index>\d+)/'
                        r'(?P<rtp_lsp_index>\d+)/(?P<rtp_lsp_version>\d+)'
                        r'\((?P<tpl_lsp_version>\d+)\))?(, )?prefix attr:'
                        r'\s+X:(?P<x_flag>0|1)\s+R:(?P<r_flag>0|1)\s+N:(?P<n_flag>0|1)$')

        # SRGB: 16000, range: 8000 prefix-SID index: 3, R:0 N:1 P:0 E:0 V:0 L:0
        p5 = re.compile(r'^SRGB:\s+(?P<srgb>\d+),\s+range:\s+(?P<range>\d+)\s+'
                        r'prefix-SID index:\s+(?P<pre_sid_ind>\w+|\d+)(,\s+'
                        r'R:(?P<r_flag>0|1)\s+N:(?P<n_flag>0|1)\s+'
                        r'P:(?P<p_flag>0|1)\s+E:(?P<e_flag>0|1)\s+'
                        r'V:(?P<v_flag>0|1)\s+L:(?P<l_flag>0|1))?$')

        #(ALT)(installed)
        #(installed)
        p6 = re.compile(r'^(\((?P<alt_attr>ALT)\))?'
                        r'(\((?P<forced>(bdw|def|all)\s+forced)\))?'
                        r'(\((?P<path_attr>(SR_POLICY|SRTE|SR_POLICY_STRICT'
                        r'|SRTE_STRICT|ULOOP_EP|TE))\))?'
                        r'(\((?P<installed>installed)\))?'
                        r'(\((?P<had_rp>had repair path)\))?$')

        # label: implicit-null
        p7 = re.compile(r'^label:\s+(?P<label>\S+)$')

        # repair path: 5.5.5.5 (MPLS-SR-Tunnel4) metric: 65 (DS,SR)
        # repair path: 199.1.2.2(Tunnel4002) metric:50 (PP,LC,DS,NP,SR) LSP[115]
        p8 = re.compile(r'^repair path(?P<stale>\(\?\))?:\s+'
                        r'(?P<repair_path>\d+.\d+.\d+.\d+)\s*'
                        r'\((?P<interface>[\w-]+\d+(\/\d+(\/\d+)?)?)\)'
                        r'\s+metric:\s*(?P<metric>\d+)\s+'
                        r'\(((?P<pp>PP),)?((?P<lc>LC),)?((?P<ds>DS),)?'
                        r'((?P<np>NP),)?((?P<sr>SR))?\)'
                        r'(\s+LSP\[(?P<rtp_lsp_index>\d+)\])?$')

        # next-hop: 10.10.20.2 (Ethernet1/1)
        p9 = re.compile(r'^next-hop:\s+(?P<next_hop>(([\d.]+)|(not found)))(\s+'
                        r'(\((?P<interface>[\w-]+\d+(\/\d+(\/\d+)?)?)\)))?$')

        # P node: R5[5.5.5.5], label: 16005
        p10 = re.compile(r'^(?P<node_type>(P|PQ|Q))\s+node:\s+(?P<host>\S+)'
                         r'\[(?P<ip>[\d.]+)\],\s+label:\s+(?P<label>\S+)$')

        # repair source: R3, LSP 3
        p11 = re.compile(r'^repair source:\s+(?P<repair_src>\S+)(,\s+LSP\s+'
                         r'(?P<rtp_lsp_index>\d+))?$')

        # Source router id: 3.3.3.3
        p12 = re.compile(r'source router id:\s+(?P<src_router_id>[\d.]+)')

        # strict-SPF label: implicit-null
        p13 = re.compile(r'^strict-SPF label:\s+(?P<strict_sid_label>\S+)$')

        # strict-SPF SID index: 6, R:0 N:1 P:0 E:0 V:0 L:0
        # Prefix-SID index: 4, R:0 N:1 P:0 E:0 V:0 L:0
        # Prefix-SID index: 1004, R:0 N:0 P:0 E:0 V:0 L:0, from SRAPP
        p14 = re.compile(r'(Prefix-SID index:|strict-SPF SID index:)\s+'
                             r'(?P<spf_sid_ind>\d+),\s+R:(?P<r_flag>0|1)\s+'
                             r'N:(?P<n_flag>0|1)\s+P:(?P<p_flag>0|1)\s+'
                             r'E:(?P<e_flag>0|1)\s+V:(?P<v_flag>0|1)\s+'
                             r'L:(?P<l_flag>0|1)(,\s+from\s+(?P<srapp>SRAPP))?')

        # type: Micro-Loop Avoidance Explicit-Path
        p15 = re.compile(r'^type:\s+'
                         r'(?P<u_loop_enabled>Micro-Loop Avoidance Explicit-Path)$')

        # strict-SPF SID index 6 - Bound (SR_POLICY_STRICT)
        # strict-SPF SID index 505 - Bound(TE)
        # p16 = re.compile(r'^strict-SPF SID index\s+(?P<strict_sid_index>\d+)'
        #                  r'\s+-\s+(?P<bound>Bound)\s*'
        #                  r'\((?P<strict_attribute>\S+)\)')
        p16 = re.compile(r'strict-SPF SID index\s+(?P<strict_sid_index>\d+)'
                         r'\s+(-\s+(?P<bound>Bound))?\s*'
                         r'(\((?P<strict_attribute>\S+)\))?')
        
        # TI-LFA link-protecting
        # local LFA
        # remote LFA
        p17 = re.compile(r'^(?P<lfa_type>local LFA|remote LFA|TI-LFA link-protecting'
                         r'|TI-LFA node/SRLG-protecting|TI-LFA node-protecting'
                         r'|TI-LFA SRLG-protecting)$')

        # Flex-algo 128
        p18 = re.compile(r'^Flex-algo\s+(?P<flex_algo>\d+)$')
        
        # IPV4 unicast topology base (TID 0, TOPOID 0x0) =================
        # IPV4 multicast topology *** (TID 0, TOPOID 0x0) =================
        p19 = re.compile(r'^IPV4\s+(?P<topo_type>unicast|multicast)\s+topology'
                         r'\s+(?P<topo_name>\S+)\s+\(TID\s+(?P<tid>\d+),\s+'
                         r'TOPOID\s+(?P<topo_id>\S+)\).+$')

        for line in out.splitlines():
            line = line.strip()

            # IPv4 local RIB for IS-IS process 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tag = group["tag"]
                tag_dict = ret_dict.setdefault("tag", {}).setdefault(tag, {})
                continue

            # IPV4 unicast topology base (TID 0, TOPOID 0x0) =================
            m = p19.match(line)
            if m:
                group = m.groupdict()
                tag_dict["topo_type"] = group["topo_type"]
                tag_dict["topo_name"] = group["topo_name"]
                tag_dict["tid"] = int(group["tid"])
                tag_dict["topo_id"] = group["topo_id"]
                continue

            # Flex-algo 128
            m = p18.match(line)
            if m:
                flex_algo_enabled = True
                group = m.groupdict()
                flex_id = int(group['flex_algo'])
                flex_algo_dict = tag_dict.setdefault("flex_algo", {}).\
                    setdefault(flex_id, {})
                continue

            # 1.1.1.0/24  prefix attr X:0 R:1 N:0
            # 3.3.3.3/32  prefix attr X:0 R:0 N:1  source router id: 3.3.3.3  SID index 3 - Bound
            # 6.6.6.6/32  prefix attr X:0 R:0 N:1  source router id: 6.6.6.6  prefix SID index 61 - Bound (SR_POLICY)
            m = p2.match(line)
            if m:
                if not flex_algo_enabled:
                    flex_algo_dict = tag_dict.setdefault("flex_algo", {}).\
                        setdefault("None", {})
                in_repair_path = False
                group = m.groupdict()
                ip = group['ip']
                bound = group['bound']
                src_router_id = group['src_router_id']
                prefix_sid_ind = group['prefix_sid_ind']
                sid_bound_attr = group['sid_bound_attribute']
                prefix_attr = {
                    "x_flag": (group['x_flag'] == "1"),
                    "r_flag": (group['r_flag'] == "1"),
                    "n_flag": (group['n_flag'] == "1")
                }

                prefix_dict = flex_algo_dict.setdefault("prefix", {}).\
                                       setdefault(ip, {})
                prefix_dict.setdefault("prefix_attr", prefix_attr)
                
                prefix_dict["subnet"] = group["subnet"]

                if src_router_id:
                    prefix_dict["source_router_id"] = src_router_id

                prefix_dict.setdefault("algo", {}).setdefault(0, {})
                prefix_dict.setdefault("algo", {}).setdefault(1, {})


                if prefix_sid_ind and prefix_sid_ind != "Invalid by SRMS":
                    prefix_dict["algo"][0]["sid_index"] = int(prefix_sid_ind)
                    prefix_dict["algo"][0]["bound"] = bound is not None

                if sid_bound_attr:
                    if "strict" in sid_bound_attr.lower():
                        prefix_dict["algo"][1]["attribute"] = sid_bound_attr
                    else:
                        prefix_dict["algo"][0]["attribute"] = sid_bound_attr
                continue

            # strict-SPF SID index 6 - Bound (SR_POLICY_STRICT)
            # strict-SPF SID index 505 - Bound(TE)
            m = p16.match(line)
            if m:
                group = m.groupdict()
                strict_attribute = group["strict_attribute"]
                prefix_dict["algo"][1]["sid_index"] = int(group["strict_sid_index"])
                prefix_dict["algo"][1]["bound"] = bound is not None

                if strict_attribute:
                    prefix_dict["algo"][1]["attribute"] = group["strict_attribute"]

                continue

            # [115/L1/70] via 6.6.6.6(MPLS-SR-Tunnel6) R3.00-00, from 4.4.4.4, tag 0
            # [115/L2/50] via 199.1.1.2(Tunnel4001), from 6.6.6.6, tag 0, LSP[105/209/18349]
            m = p3.match(line)
            if m:
                group = m.groupdict()
                route_type = group["route_type"]
                interface = group["interface"]
                host = group["host"]
                source_ip = group["from_ip"]
                next_hop_lsp_index = group["next_hop_lsp_index"]
                rtp_lsp_index = group["rtp_lsp_index"]
                rtp_lsp_version = group["rtp_lsp_version"]

                via_interface_dict = prefix_dict.\
                                        setdefault("via_interface", {}).\
                                        setdefault(interface, {})
                level_dict = via_interface_dict.setdefault("level", {}).\
                                                setdefault(route_type, {})
                
                source_ip_dict = level_dict.setdefault("source_ip", {}).\
                                            setdefault(source_ip, {})
                lsp_dict = source_ip_dict.setdefault("lsp", {})

                source_ip_dict["distance"] = int(group["distance"])
                source_ip_dict["metric"] = int(group["metric"])
                source_ip_dict["via_ip"] = group["ip"]
                source_ip_dict["tag"] = group["tag"]
                source_ip_dict["filtered_out"] = group['filtered'] is not None

                if host: source_ip_dict["host"] = host

                if next_hop_lsp_index:
                    lsp_dict["next_hop_lsp_index"] = int(next_hop_lsp_index)

                if rtp_lsp_index:
                    lsp_dict["rtp_lsp_index"] = int(rtp_lsp_index)

                if rtp_lsp_version:
                    lsp_dict["rtp_lsp_version"] = int(rtp_lsp_version)
                

                continue

            # LSP 3/4/0(52), prefix attr: X:0 R:0 N:1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                next_hop_lsp_index = group["next_hop_lsp_index"]
                rtp_lsp_index = group["rtp_lsp_index"]
                rtp_lsp_version = group["rtp_lsp_version"]
                tpl_lsp_version = group["tpl_lsp_version"]
                prefix_attr = {
                    "x_flag": (group['x_flag'] == "1"),
                    "r_flag": (group['r_flag'] == "1"),
                    "n_flag": (group['n_flag'] == "1")
                }

                if next_hop_lsp_index:
                    lsp_dict["next_hop_lsp_index"] = int(next_hop_lsp_index)

                if rtp_lsp_index:
                    lsp_dict["rtp_lsp_index"] = int(rtp_lsp_index)

                if rtp_lsp_version:
                    lsp_dict["rtp_lsp_version"] = int(rtp_lsp_version)

                if tpl_lsp_version:
                    lsp_dict["tpl_lsp_version"] = int(tpl_lsp_version)

                source_ip_dict.setdefault("prefix_attr", prefix_attr)

                continue

            # SRGB: 16000, range: 8000 prefix-SID index: 3, R:0 N:1 P:0 E:0 V:0 L:0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                source_ip_dict["srgb_start"] = int(group["srgb"])
                source_ip_dict["srgb_range"] = int(group["range"])

                source_ip_dict.setdefault("algo", {}).setdefault(0, {})

                if group["pre_sid_ind"] != "None":
                    source_ip_dict["algo"][0]["sid_index"] = int(group["pre_sid_ind"])

                if (group["r_flag"] and group["n_flag"] and group["p_flag"] and
                    group["e_flag"] and group["v_flag"] and group["l_flag"]):
                    flags = {
                        "r_flag": (group["r_flag"] == "1"),
                        "n_flag": (group["n_flag"] == "1"),
                        "p_flag": (group["p_flag"] == "1"),
                        "e_flag": (group["e_flag"] == "1"),
                        "v_flag": (group["v_flag"] == "1"),
                        "l_flag": (group["l_flag"] == "1")
                    }
                    if in_repair_path:
                        repair_path_dict.setdefault("algo", {}).setdefault(0, {})
                        repair_path_dict["algo"][0]["flags"] = flags
                    else:
                        source_ip_dict["algo"][0]["flags"] = flags

                continue

            # (ALT)(installed)
            # (installed)
            # (ALT)(all forced)(SR_POLICY)(installed)(had repair path)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if not any(group.values()):
                    continue

                attr_dict = {
                    "ALT": False,
                    "SR_POLICY": False,
                    "SR_POLICY_STRICT": False,
                    "SRTE": False,
                    "SRTE_STRICT": False,
                    "ULOOP_EP": False,
                    "TE": False,
                }
                source_ip_dict.setdefault("path_attribute", attr_dict)
                if group["path_attr"]:
                    source_ip_dict["path_attribute"][group["path_attr"]] = True
                if group["alt_attr"]:
                    source_ip_dict["path_attribute"][group["alt_attr"]] = True
                if group["forced"]:
                    source_ip_dict["forced"] = group["forced"]
                source_ip_dict["had_repair_path"] = group["had_rp"] is not None
                source_ip_dict["installed"] = group["installed"] is not None

                continue

            # label: implicit-null
            m = p7.match(line)
            if m:
                group = m.groupdict()
                
                if in_repair_path:
                    repair_path_dict.setdefault("algo", {}).setdefault(0, {})
                    repair_path_dict["algo"][0]["label"] = group["label"]
                else:
                    source_ip_dict.setdefault("algo", {}).setdefault(0, {})
                    source_ip_dict["algo"][0]["label"] = group["label"]

                continue

            # repair path: 5.5.5.5 (MPLS-SR-Tunnel4) metric: 65 (DS,SR)
            # repair path: 199.1.2.2(Tunnel4002) metric:50 (PP,LC,DS,NP,SR) LSP[115]
            m = p8.match(line)
            if m:
                in_repair_path = True
                group = m.groupdict()
                rp_rtp_lsp_index = group["rtp_lsp_index"]
                attributes  = {
                        "DS": (group["ds"] == "DS"),
                        "LC": (group["lc"] == "LC"),
                        "NP": (group["np"] == "NP"),
                        "PP": (group["pp"] == "PP"),
                        "SR": (group["sr"] == "SR")
                }
                
                repair_path_dict = source_ip_dict.setdefault("repair_path", {})
                repair_path_dict.setdefault("attributes", attributes)

                repair_path_dict["ip"] = group["repair_path"]
                repair_path_dict["interface"] = group["interface"]
                repair_path_dict["metric"] = int(group["metric"])
                repair_path_dict["stale"] = group["stale"] is not None

                if rp_rtp_lsp_index:
                    repair_path_dict["rtp_lsp_index"] = int(rp_rtp_lsp_index)

                continue

            # next-hop: 10.10.20.2 (Ethernet1/1)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                if group["interface"]:
                    repair_path_dict["next_hop_interface"] = group["interface"]
                repair_path_dict["next_hop_ip"] = group["next_hop"]

                continue

            # P node: R5[5.5.5.5], label: 16005
            m = p10.match(line)
            if m:
                group = m.groupdict()
                host = group["host"]
                node_dict = {
                    "node_type": group["node_type"],
                    "ip": group["ip"],
                    "label": group["label"]
                }

                repair_path_dict.setdefault("nodes", {}).setdefault("host", {}).\
                                 setdefault(host, node_dict)

                continue

            # repair source: R3, LSP 3
            m = p11.match(line)
            if m:
                group = m.groupdict()
                rs_rtp_lsp_index = group["rtp_lsp_index"]
                repair_source_dict = repair_path_dict.setdefault("repair_source", {})
                repair_source_dict["host"] = group["repair_src"]

                if rs_rtp_lsp_index:
                    repair_source_dict["rtp_lsp_index"] = int(rs_rtp_lsp_index)

                continue

            # source router id: 3.3.3.3
            m = p12.match(line)
            if m:
                group = m.groupdict()
                source_ip_dict["source_router_id"] = group["src_router_id"]

                continue

            # strict-SPF label: implicit-null
            m = p13.match(line)
            if m:
                group = m.groupdict()
                
                if in_repair_path:
                    repair_path_dict.setdefault("algo", {}).setdefault(1, {})
                    source_ip_dict["repair_path"]["algo"][1]["label"] = group["strict_sid_label"]
                else:
                    source_ip_dict.setdefault("algo", {}).setdefault(1, {})
                    source_ip_dict["algo"][1]["label"] = group["strict_sid_label"]

                continue

            # strict-SPF SID index: 6, R:0 N:1 P:0 E:0 V:0 L:0
            # Prefix-SID index: 4, R:0 N:1 P:0 E:0 V:0 L:0
            # Prefix-SID index: 1004, R:0 N:0 P:0 E:0 V:0 L:0, from SRAPP
            m = p14.match(line)
            if m:
                group = m.groupdict()
                if in_repair_path:
                    repair_path_dict.setdefault("algo", {}).setdefault(0, {})
                    repair_path_dict.setdefault("algo", {}).setdefault(1, {})
                else:
                    source_ip_dict.setdefault("algo", {}).setdefault(0, {})
                    source_ip_dict.setdefault("algo", {}).setdefault(1, {})


                if (group["r_flag"] and group["n_flag"] and group["p_flag"] and
                    group["e_flag"] and group["v_flag"] and group["l_flag"]):
                    flags = {
                        "r_flag": (group["r_flag"] == "1"),
                        "n_flag": (group["n_flag"] == "1"),
                        "p_flag": (group["p_flag"] == "1"),
                        "e_flag": (group["e_flag"] == "1"),
                        "v_flag": (group["v_flag"] == "1"),
                        "l_flag": (group["l_flag"] == "1")
                    }

                if line.startswith("Prefix"):
                    if in_repair_path:
                        repair_path_dict["algo"][0]["sid_index"] = int(group["spf_sid_ind"])
                        repair_path_dict["algo"][0]["flags"] = flags
                    else:
                        source_ip_dict["algo"][0]["sid_index"] = int(group["spf_sid_ind"])
                        source_ip_dict["algo"][0]["flags"] = flags
                        if group["srapp"]:
                            source_ip_dict["algo"][0]["from_srapp"] = (group["srapp"] == "SRAPP")
                elif line.startswith("strict"):
                    if in_repair_path:
                        repair_path_dict["algo"][1]["sid_index"] = int(group["spf_sid_ind"])
                        repair_path_dict["algo"][1]["flags"] = flags
                    else:
                        source_ip_dict["algo"][1]["sid_index"] = int(group["spf_sid_ind"])
                        source_ip_dict["algo"][1]["flags"] = flags
                        if group["srapp"]:
                            source_ip_dict["algo"][1]["from_srapp"] = (group["srapp"] == "SRAPP")
                
                

                continue

            # type: Micro-Loop Avoidance Explicit-Path
            m = p15.match(line)
            if m:
                group = m.groupdict()
                source_ip_dict["u_loop_enabled"] = True
                
                continue

            # TI-LFA link-protecting
            # local LFA
            # remote LFA
            m = p17.match(line)
            if m:
                group = m.groupdict()
                repair_path_dict["lfa_type"] = group["lfa_type"]

                continue

        return ret_dict

class ShowIsisRibRedistributionSchema(MetaParser):
    """Schema for show isis rib redistributon"""
    schema = {
        'tag': { 
            Any(): {
                'topo_type': { 
                    Any() : {
                        'topo_name': str,
                        'mtid': str,
                        'topo_id': str,
                        'level': {
                            str: {
                                Optional('prefix'): {
                                    str: {
                                        'mask_len': int,
                                        'route_type': str,
                                        'metric': int,
                                        Optional('external'): bool,
                                        Optional('interarea'): bool,
                                        Optional('isis'): bool,
                                        Optional('tag'): str,
                                        Optional('algo'): {
                                            int: {
                                                'index': int,
                                                'r_flag': bool,
                                                'n_flag': bool,
                                                'p_flag': bool,
                                                'e_flag': bool,
                                                'v_flag': bool,
                                                'l_flag': bool,
                                                Optional('map_type'): str,
                                                Optional('pfx_metric'): int,
                                                Optional('advertise'): bool
                                            },
                                        },
                                        Optional('x_flag'): bool,
                                        Optional('r_flag'): bool,
                                        Optional('n_flag'): bool,
                                        Optional('src_rtr_id'): str
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

class ShowIsisRibRedistribution(ShowIsisRibRedistributionSchema):
    """Parser for show isis rib redistribution"""

    
    cli_command = ['show isis rib redistribution']

    def cli(self, output=None):
        
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        #######  Reg-exes  ##########
        # IPv4 redistribution RIB for IS-IS process 1
        p1 = re.compile(r'^IPv4 redistribution RIB for IS-IS process +'
                        '(?P<isis_name>\S+)$')

        #IPV4 unicast base topology (TID 0, TOPOID 0x0) =================
        p2 = re.compile(r'^IPV4 (?P<topo>unicast|multicast) (?P<topo_name>.+)'
                        ' \(TID (?P<mtid>\d+), TOPOID (?P<topoid>\S+)\).*')

        #====== Level 1 ======
        p3 = re.compile(r'^=*\s*Level\s*(?P<level>\d)\s*=*$')

        #22.22.22.22/32
        p4 = re.compile(r'^(?P<prefix>\d+(\.\d+){3})/(?P<masklen>\d+)$')

        #[Connected/10]
        #[ISIS/0] external  prefix-SID index: 44, R:1 N:0 P:1 E:0 V:0 L:0
        p5 = re.compile(r'^\[(?P<rt_pdb>Connected|Static|BGP|RIP|IGRP|EIGRP'
             '|OSPF|OSPFv3|ISIS|Mobil|ODR|LISP|OMP|NAT Route)/'
             '(?P<metric>\d+)\] *'
             '(?P<interarea>interarea)? *(?P<external>external)? *'
             '(?P<isis>isis )? *(?P<algo>prefix-SID index: )?(?P<index>\d+)?'
             '(, R:)*(?P<r_flag>0|1)?( N:)*(?P<n_flag>0|1)?'
             '( P:)*(?P<p_flag>0|1)?( E:)*(?P<e_flag>0|1)?'
             '( V:)*(?P<v_flag>0|1)?( L:)*(?P<l_flag>0|1)?')

        #strict-SPF SID index: 404, R:1 N:0 P:1 E:0 V:0 L:0
        p6 = re.compile(r'^(?P<algo>strict-SPF SID index: )(?P<index>\d+)'
             ', R:(?P<r_flag>0|1) N:(?P<n_flag>0|1) P:(?P<p_flag>0|1)'
             ' E:(?P<e_flag>0|1) V:(?P<v_flag>0|1) L:(?P<l_flag>0|1)$')
        
        #flex-algo 129 SID index: 122, R:0 N:1 P:0 E:0 V:0 L:0 map 0x1
        p7 = re.compile(r'^flex-algo (?P<algo>\d+) SID index: (?P<index>\d+)'
             ', R:(?P<r_flag>0|1) N:(?P<n_flag>0|1) P:(?P<p_flag>0|1)'
             ' E:(?P<e_flag>0|1) V:(?P<v_flag>0|1) L:(?P<l_flag>0|1) '
             'map (?P<map>.*)$')
        
        #prefix-metric: 0, not advertised
        p8 = re.compile(r'^prefix-metric: (?P<metric>\d+), '
             '(?P<not_advertised>not )?advertised$')
      
        #prefix attr: X:0 R:0 N:1
        p9 = re.compile(r'^prefix attr: X:(?P<x_flag>0|1) R:(?P<r_flag>0|1) '
             'N:(?P<n_flag>0|1)$')

        #source router id: 22.22.22.22
        p10 = re.compile(r'^source router id: (?P<src>\d+(\.\d+){3})$')
  
        ########## Searching the output ################
        for line in out.splitlines():
            line = line.strip()

            # IPv4 redistribution RIB for IS-IS process 1
            m = p1.match(line)
            if m:
                l_isis_name = m.groupdict()['isis_name']
                tag_dict = ret_dict.setdefault('tag', {}).setdefault(l_isis_name, {})
                continue

            #IPV4 unicast base topology (TID 0, TOPOID 0x0) =================
            m = p2.match(line)
            if m:
                group = m.groupdict()
                l_topo = group['topo']
                l_mtid = group['mtid']
                l_topoid = group['topoid']
                topo_dict = tag_dict.setdefault('topo_type', {}).setdefault(l_topo, {})
                topo_dict['topo_name'] = group['topo_name']
                topo_dict['mtid'] = l_mtid
                topo_dict['topo_id'] = l_topoid
                continue

            #====== Level 1 ======
            m = p3.match(line)
            if m:
                level = m.groupdict()['level']
                lvl_dict = topo_dict.setdefault('level', {}).setdefault(level, {})
                continue

            #22.22.22.22/32
            m = p4.match(line)
            if m:
                prefix = m.groupdict()['prefix']
                masklen = m.groupdict()['masklen']
                pfx_dict = lvl_dict.setdefault('prefix', {}).setdefault(prefix, {})
                pfx_dict['mask_len'] = int(masklen)
                continue

            #[ISIS/0] external  prefix-SID index: 44, R:1 N:0 P:1 E:0 V:0 L:0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                pfx_dict['route_type'] = (group['rt_pdb']).lower()
                pfx_dict['metric'] = int(group['metric'])
                external = group['external'] 
                interarea = group['interarea']
                isis = group['isis']
                algo = group['algo']
                index = group['index']
                pfx_dict['external'] = (external is not None);
                pfx_dict['interarea'] = (interarea is not None);
                pfx_dict['isis'] = (isis is not None);
                if algo is not None:
                    sid_dict = pfx_dict.setdefault('algo', {}).setdefault(0, {})
                    sid_dict['index'] = int(index)
                    sid_dict['p_flag'] = (group['p_flag'] == "1")
                    sid_dict['r_flag'] = (group['r_flag'] == "1")
                    sid_dict['v_flag'] = (group['v_flag'] == "1")
                    sid_dict['e_flag'] = (group['e_flag'] == "1")
                    sid_dict['l_flag'] = (group['l_flag'] == "1")
                    sid_dict['n_flag'] = (group['n_flag'] == "1")
                continue

            #strict-SPF SID index: 404, R:1 N:0 P:1 E:0 V:0 L:0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                algo = group['algo']
                index = group['index']
                sid_dict = pfx_dict.setdefault('algo', {}).setdefault(1, {})
                sid_dict['index'] = int(index)
                sid_dict['p_flag'] = (group['p_flag'] == "1")
                sid_dict['r_flag'] = (group['r_flag'] == "1")
                sid_dict['v_flag'] = (group['v_flag'] == "1")
                sid_dict['e_flag'] = (group['e_flag'] == "1")
                sid_dict['l_flag'] = (group['l_flag'] == "1")
                sid_dict['n_flag'] = (group['n_flag'] == "1")
                continue

            #flex-algo 129 SID index: 122, R:0 N:1 P:0 E:0 V:0 L:0 map 0x1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                algo = group['algo']
                index = group['index']
                maps = group['map']
                sid_dict = pfx_dict.setdefault('algo', {}).setdefault(int(algo), {})
                sid_dict['index'] = int(index)
                sid_dict['p_flag'] = (group['p_flag'] == "1")
                sid_dict['r_flag'] = (group['r_flag'] == "1")
                sid_dict['v_flag'] = (group['v_flag'] == "1")
                sid_dict['e_flag'] = (group['e_flag'] == "1")
                sid_dict['l_flag'] = (group['l_flag'] == "1")
                sid_dict['n_flag'] = (group['n_flag'] == "1")
                sid_dict['map_type'] = maps
                continue

            #prefix-metric: 0, not advertised
            m = p8.match(line)
            if m:
                group = m.groupdict()
                metric = group['metric']
                not_adv = group['not_advertised']
                sid_dict['pfx_metric'] = int(metric)
                sid_dict['advertise'] = (not_adv is None)
                continue

            #prefix attr: X:0 R:0 N:1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                pfx_dict['x_flag'] = (group['x_flag'] == '1')
                pfx_dict['r_flag'] = (group['r_flag'] == '1')
                pfx_dict['n_flag'] = (group['n_flag'] == '1')
                continue

            #source router id: 22.22.22.22
            m = p10.match(line)
            if m:
                group = m.groupdict()
                pfx_dict['src_rtr_id'] = group['src']
                continue

        return ret_dict


class ShowIsisNodeLevelSchema(MetaParser):
    """
    Schema for show isis node {level}
    """
    schema = {
      'tag' : {
          Any() : {
            'level': {
                Any(): {
                  'host': {
                      Any(): {
                         Optional('ip_interface_address'): str,
                         Optional('lsp_id'): int,
                         'lsp_index' : {                   
                             Any(): {
                               'sr_capable' :str,
                               'strict_spf_capable':str,                             
                                 },
                              },
                            },
                        },
                     },
                  },
               },
            },
         } 
 
class ShowIsisNodeLevel(ShowIsisNodeLevelSchema):
    """ Parser for show isis node {level}"""

    cli_command = 'show isis node {level}'
    
    def cli(self,level, output=None): 
        if output is None:
            output = self.device.execute(self.cli_command.format(level=level))

        # initial variables
        ret_dict = {}

                
        # Tag nSVL-1:
        p1 = re.compile(r'^Tag (?P<tag>\S+):$')

        # ISIS level-1 node information for Switch.00
        p2 = re.compile(r'^ISIS (?P<level>\S+)\s+node information for\s+(?P<host>\S+)$')

        # LSP index: 1
        p3 = re.compile(r'^LSP index:\s+(?P<lsp_index>\d+)$')

        # SR capable: No, Strict-SPF capable: No
        p4 =  re.compile('^SR capable: (?P<sr_capable>\w+), Strict-SPF capable: (?P<strict_spf_capable>\w+)$')

        # IP interface address: 1.1.1.1 (LSP #0)
        p5 =  re.compile(r'^IP interface address: (?P<ip_interface_address>[\d\.]+)\s+\(LSP\s+\#(?P<lsp_id>\d+)\)$')

        for line in output.splitlines():
            line = line.strip()

            # Tag 1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('tag',{},).setdefault((group['tag']),{})
                continue

            # ISIS level-1 node information for Switch.00
            m = p2.match(line)
            if m:
                group = m.groupdict()
                level_dict = root_dict.setdefault('level',{}).setdefault((group['level']),{})
                level_dict = level_dict.setdefault('host',{}).setdefault((group['host']),{})
            
                continue
            
            # LSP index: 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                lsp_index_dict = level_dict.setdefault('lsp_index',{}).setdefault(int(group['lsp_index']),{})
                continue
            
            # SR capable: No, Strict-SPF capable: No
            m = p4.match(line)
            if m:
                group = m.groupdict()
                lsp_index_dict['sr_capable']= group['sr_capable']
                lsp_index_dict['strict_spf_capable'] = group['strict_spf_capable']
                continue
            
            # IP interface address: 1.1.1.1 (LSP #0)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                level_dict['ip_interface_address'] = group['ip_interface_address']
                level_dict['lsp_id'] = int(group['lsp_id'])
                continue
                
        return ret_dict


class ShowIsisNodeSummarySchema(MetaParser):
    """
    Schema for show isis node summary
    """
    schema = {
       'tag' :{
          Any():{
            'level': {
               Any() :{
                 'switch':list
               },
            },
         },
      },
   }
  
class ShowIsisNodeSummary(ShowIsisNodeSummarySchema):
    """ Parser for show isis node summary"""

    cli_command = 'show isis node summary'
    
    def cli(self, output=None): 
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict = {}

        # Tag nSVL-1:
        p1 = re.compile(r'^Tag (?P<tag>\S+):$')

        # ISIS level-1 node information for sw.F87A4137BE0.00
        # ISIS level-1 node information for sw.F87A4137BE0.01
        p2 = re.compile(r'^ISIS level-(?P<level>\d+)\s+node information for\s+(?P<switch>\S+)$')

        for line in output.splitlines():
            line = line.strip()
            
            # Tag nSVL-1:
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                root_dict = ret_dict.setdefault('tag',{}).setdefault(groups['tag'],{})
                continue

            # ISIS level-1 node information for sw.F87A4137BE0.00
            # ISIS level-1 node information for sw.F87A4137BE0.01
            m = p2.match(line)
            if m:
                group = m.groupdict()
                switch_list = root_dict.setdefault('level', {}).setdefault(group['level'], {}).setdefault('switch', [])
                switch_list.append(group['switch'])
                continue
                
        return ret_dict       


class ShowIsisTopologyLevelSchema(MetaParser):
    """
    Schema for show isis topology {level}
    """
    schema = {
       'tag' :{
          Any():{
            'level': {
                Any() :{
                   'system_id':{
                       Any():{
                         Optional('metric') : int,
                         Optional('next_hop') :str,
                         Optional('interface'):str,
                         Optional('snpa'): str
                      },
                  },
              },
           },
        },
    },
}  

class ShowIsisTopologyLevel(ShowIsisTopologyLevelSchema):
    """ Parser for show  isis topology {level}"""

    cli_command = 'show isis topology {level}'
    
    def cli(self,level,output=None): 
        if output is None:
            output = self.device.execute(self.cli_command.format(level=level))
        
        # initial variables
        ret_dict = {}

        # Tag nSVL-1:
        p1 = re.compile(r'^Tag (?P<tag>\S+):$')

        # IS-IS TID 0 paths to level-2 routers
        p2 = re.compile('^.+paths to level-(?P<level>\d).+$')

        # System Id            Metric     Next-Hop             Interface   SNPA
        # sw.F87A4137BE00      10         sw.F87A4137BE00      Po241       f87a.4137.bf02
        p3 = re.compile('(?P<system_id>\S+)\s+(?P<metric>\d+)\s+(?P<next_hop>\S+)\s+(?P<interface>\w+)\s+(?P<snpa>[\w\d\.]+)$')

        for line in output.splitlines():
            line = line.strip()

            # Tag 1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('tag',{},).setdefault((group['tag']),{})
                continue

            # IS-IS TID 0 paths to level-2 routers
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict1 = root_dict.setdefault('level',{}).setdefault((group['level']),{})
                continue

            # System Id            Metric     Next-Hop             Interface   SNPA
            # sw.F87A4137BE00      10         sw.F87A4137BE00      Po241       f87a.4137.bf02
            m = p3.match(line)
            if m:
                group = m.groupdict()
                system_id_dict = root_dict1.setdefault('system_id',{}).setdefault(group['system_id'],{})
                system_id_dict['metric'] = int(group['metric'])
                system_id_dict['next_hop'] = (group['next_hop'])
                system_id_dict['interface']= (group['interface'])
                system_id_dict['snpa']= (group['snpa'])
                continue   
                
        return ret_dict

class ShowIsisMicroloopAvoidanceFlexAlgoSchema(MetaParser):
    """
    Schema for show isis microloop-avoidance flex-algo {flexId}
               show isis microloop-avoidance flex-algo all 
    """
    schema = {
       "tag" : {
          Any():{
               "flex_algo":{
                    Any():{
                        "state" : str,
                        "delay" : int,
                        "runningl1": str,
                        "runningl2": str
                    },
                },
            },
        }
    } 

class ShowIsisMicroloopAvoidanceFlexAlgo(ShowIsisMicroloopAvoidanceFlexAlgoSchema):
    """ Parser for show isis microloop-avoidance flex-algo {flexId}"""

    cli_command = 'show isis microloop-avoidance flex-algo {flexId}'

    def cli(self, flexId='all', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(flexId=flexId))

        # initial variables
        ret_dict = {}
        # Tag: srtest
        p1 = re.compile(r'Tag\:\s+(?P<isis_tag>\w+)')

        # Algo  State            Delay  Running(L1/L2)
        # 128   Segment-Routing  5000   FALSE/NA
        p2 = re.compile(r'(?P<flex_algo_id>\d+)\s+(?P<state>[\w\-]+)\s+(?P<delay>\d+)\s+(?P<RunningL1>\S+)\/(?P<RunningL2>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # Tag 1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('tag',{},).setdefault((group['isis_tag']),{})
                continue
            ##Algo  State            Delay  Running(L1/L2)
            ##128   Segment-Routing  5000   FALSE/NA
            m = p2.match(line)
            if m:
                 group = m.groupdict()
                 flex_dict = root_dict.setdefault('flex_algo',{},).setdefault((group['flex_algo_id']),{})
                 flex_dict['state']=group['state']
                 flex_dict['delay']=int(group['delay'])
                 flex_dict['runningl1']=group['RunningL1']
                 flex_dict['runningl2']=group['RunningL2']
                 continue
        return ret_dict 
