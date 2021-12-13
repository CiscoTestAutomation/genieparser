
""" show_isis.py

IOSXE parsers for the following show commands:
    * show isis neighbors
    * show isis hostname
    * show isis lsp-log
    * show isis database detail
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
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
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

        # initial return dictionary
        ret_dict = {}
        tag_null = True
        for line in out.splitlines():
            line = line.strip()

            # Tag isis_net:
            p1 = re.compile(r'^Tag +(?P<isis_name>\S+)\s*:$')
            m = p1.match(line)
            if m:
                isis_name = m.groupdict()['isis_name']
                isis_dict = ret_dict.setdefault('isis', {}).setdefault(isis_name, {})
                tag_null = False
                continue

            # LAB-9001-2      L1   Te0/0/26      10.239.7.29     UP    27       00
            p2 = re.compile(r'^(?P<system_id>\S+)\s+(?P<type>\S+)\s+(?P<interface>\S+)\s+'
                             '(?P<ip_address>\S+)\s+(?P<state>(UP|DOWN|INIT|NONE)+)\s+'
                             '(?P<holdtime>\S+)\s+(?P<circuit_id>\S+)$')
            m = p2.match(line)
            if m:
                system_id = m.groupdict()['system_id']
                isis_type = m.groupdict()['type']

                if tag_null:
                    neighbour_dict = ret_dict.setdefault('isis', {}).setdefault('null', {}).\
                                              setdefault('neighbors', {}).setdefault(system_id, {})
                else:
                    neighbour_dict = isis_dict.setdefault('neighbors', {}).setdefault(system_id, {})

                type_dict = neighbour_dict.setdefault('type', {}).setdefault(isis_type, {})

                interface_name = Common.convert_intf_name(m.groupdict()['interface'])
                interfaces_dict = type_dict.setdefault('interfaces', {}).setdefault(interface_name, {})
                interfaces_dict['ip_address'] = m.groupdict()['ip_address']
                interfaces_dict['state'] = m.groupdict()['state']
                interfaces_dict['holdtime'] = m.groupdict()['holdtime']
                interfaces_dict['circuit_id'] = m.groupdict()['circuit_id']
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

class ShowIsisDatabaseDetailSchema(MetaParser):
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
                            'attach_bit': int,
                            'p_bit': int,
                            'overload_bit': int,
                            Optional('area_address'): str,
                            Optional('router_id'): str,
                            Optional('nlpid'): str,
                            Optional('topology'): {
                                Any(): {
                                    'code': str,
                                },
                            },
                            Optional('hostname'): str,
                            Optional('ip_address'): str,
                            Optional('ipv6_address'): str,
                            Optional('is_neighbor'): {
                                Any(): {
                                    'neighbor_id': str,
                                    'metric': int,
                                },
                            },
                            Optional('extended_is_neighbor'): {
                                Any(): {
                                    'neighbor_id': str,
                                    'metric': int,
                                },
                            },
                            Optional('mt_is_neighbor'): {
                                Any(): {
                                    'neighbor_id': str,
                                    'metric': int,
                                },
                            },
                            Optional('ipv4_internal_reachability'): {
                                Any(): {
                                    'ip_prefix': str,
                                    'prefix_len': str,
                                    'metric': int,
                                },
                            },
                            Optional('ipv4_interarea_reachability'): {
                                Any(): {
                                    'ip_prefix': str,
                                    'prefix_len': str,
                                    'metric': int,
                                },
                            },
                            Optional('mt_ipv6_reachability'): {
                                Any(): {
                                    'ip_prefix': str,
                                    'prefix_len': str,
                                    'metric': int,
                                },
                            },
                            Optional('ipv6_reachability'): {
                                Any(): {
                                    'ip_prefix': str,
                                    'prefix_len': str,
                                    'metric': int,
                                },
                            },
                        },
                    }
                }
            }
        }
    }

class ShowIsisDatabaseDetail(ShowIsisDatabaseDetailSchema):
    """Parser for show isis database detail"""

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
        p2 = re.compile(r'^IS\-IS +Level\-(?P<level>\d+) +Link +State +Database(:)?$')

        # LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd      ATT/P/OL
        # R2.00-00            * 0x00000007   0x8A6D                 403/*         1/0/0
        p3 = re.compile(
            r'^(?P<lspid>[\w\-\.]+)(\s*(?P<star>\*))? +(?P<lsp_seq_num>\w+) +(?P<lsp_checksum>\w+)'
            r' +(?P<lsp_holdtime>[\d\*]+)(/(?P<lsp_rcvd>[\d\*]+))? +(?P<att>\d+)/(?P<p>\d+)/(?P<ol>\d+)$')

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
                        is_dict = lsp_dict.setdefault('extended_is_neighbor', {}).setdefault(ip, {})
                    elif mtype == 'IS' and mt_ipv6:
                        is_dict = lsp_dict.setdefault('mt_is_neighbor', {}).setdefault(ip, {})
                    elif mtype == 'IS':
                        is_dict = lsp_dict.setdefault('is_neighbor', {}).setdefault(ip, {})

                    is_dict.update({'neighbor_id': ip,
                                    'metric': int(group['metric'])})

                if mtype.startswith('IP'):
                    if mtype == 'IP':
                        is_dict = lsp_dict.setdefault('ipv4_internal_reachability', {}).setdefault(ip, {})
                    elif mtype == 'IP-Interarea':
                        is_dict = lsp_dict.setdefault('ipv4_interarea_reachability', {}).setdefault(ip, {})
                    elif mtype == 'IPv6' and mt_ipv6:
                        is_dict = lsp_dict.setdefault('mt_ipv6_reachability', {}).setdefault(ip, {})
                    elif mtype == 'IPv6':
                        is_dict = lsp_dict.setdefault('ipv6_reachability', {}).setdefault(ip, {})

                    ip_prefix = ip.split('/')[0]
                    prefix_len = ip.split('/')[1]
                    is_dict.update({'ip_prefix': ip_prefix,
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

        return result_dict

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
                                "ip_router_id": str,
                                "ip_router_lsp": int,
                                "ip_interface_address": str,
                                "ip_interface_address_lsp": int,
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
                                "adj_sid": {
                                    Any(): {
                                        "lsp": int,
                                        "from_host": str,
                                        "to_host": str,
                                    }
                                },
                                "lsp_index": int,
                                "srgb": {
                                    "start": int,
                                    "range": int,
                                    "lsp": int
                                },
                                "srlb": {
                                    "start": int,
                                    "range": int,
                                    "lsp": int
                                },
                                "capability": {
                                    "sr": str,
                                    "strict_spf": str,
                                    "lsp": int
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
        p13 = re.compile(r'^SR capable: (?P<sr_capable>\w+), Strict-SPF capable: (?P<strict_spf_capable>\w+)\s+\(LSP\s+#(?P<lsp_id>\d+)\)$')

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
                Optional("flex-algo"): int,
                Optional("prefix") : {
                    Any() : {
                        "subnet": str,
                        "prefix_attr": {
                            "x_flag": bool,
                            "r_flag": bool,
                            "n_flag": bool
                        },
                        Optional("source_router_id"): str,
                        Optional("prefix_sid_index"): int,
                        Optional("sid_bound_attribute"): str,
                        Optional("strict_spf_sid_index"): int,
                        Optional("strict_sid_bound_attribute"): str,
                        Optional("strict_sid_bound_attribute_te"): bool,
                        "via_interface": {
                            Any(): {
                                "distance": int,
                                "route_type": str,
                                "metric": int,
                                "via_ip": str,
                                Optional("host"): str,
                                "src_ip": str,
                                "tag": str,
                                "lsp": {
                                    "next_hop_lsp_index": int,
                                    "rtp_lsp_index": int,
                                    "rtp_lsp_version": int,
                                    Optional("tpl_lsp_version"): int
                                },
                                Optional("prefix_attr"): {
                                    "x_flag": bool,
                                    "r_flag": bool,
                                    "n_flag": bool
                                },
                                Optional("src_router_id"): str,
                                Optional("srgb"): int,
                                Optional("srgb_range"): int,
                                Optional("prefix_sid_index"): int,
                                Optional("non_strict_sid_flags"): {
                                    "r_flag": bool,
                                    "n_flag": bool,
                                    "p_flag": bool,
                                    "e_flag": bool,
                                    "v_flag": bool,
                                    "l_flag": bool
                                },
                                Optional("strict_spf_sid_index"): int,
                                Optional("strict_spf_sid_flags"): {
                                    "r_flag": bool,
                                    "n_flag": bool,
                                    "p_flag": bool,
                                    "e_flag": bool,
                                    "v_flag": bool,
                                    "l_flag": bool
                                },
                                Optional("u_loop_enabled"): bool,
                                Optional("label"): str,
                                Optional("strict_spf_label"): str,
                                Optional("repair_path"): {
                                    "ip": str,
                                    "interface": str,
                                    Optional("next_hop_ip"): str,
                                    Optional("next_hop_interface"): str,
                                    "metric": int,
                                    Optional("rtp_lsp_index"): int,
                                    Optional("lfa_type"): str,
                                    "label": str,
                                    "attributes": {
                                        "DS": bool,
                                        "LC": bool,
                                        "NP": bool,
                                        "PP": bool,
                                        "SR": bool
                                    },
                                    Optional("nodes"): {
                                        "host" : {
                                            Any(): {
                                                "node_type": str,
                                                "ip": str,
                                                "label": str
                                            }
                                        }
                                    }
                                },
                                Optional("repair_source"): {
                                    "host": str,
                                    Optional("rtp_lsp_index"): int
                                },
                                Optional("path_attribute"): str,
                                Optional("installed"): bool
                            }
                        }
                    }
                }
            }
        }
    }

class ShowIsisRib(ShowIsisRibSchema):
    '''parser for show isis rib
                  show isis rib flex-algo {flex-algo}
                  show isis rib {source_ip}
                  show isis rib {source_ip} {subnet_mask}
    '''

    cli_command = ['show isis rib',
                   'show isis rib flex-algo {flex_id}',
                   'show isis rib {source_ip}',
                   'show isis rib {source_ip} {subnet_mask}']

    def cli(self, flex_id="", source_ip="", subnet_mask="", output=None):
        if output is None:
            if flex_id:
                out = self.device.execute(self.cli_command[1].format(flex_id=flex_id))
            elif source_ip and not subnet_mask:
              out = self.device.execute(self.cli_command[2].format(source_ip=source_ip))
            elif source_ip and subnet_mask:
              out = self.device.execute(self.cli_command[3].format(source_ip=source_ip, subnet_mask=subnet_mask))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}
        in_repair_path = False

        # IPv4 local RIB for IS-IS process 1
        p1 = re.compile(r'^IPv4 local RIB for IS-IS process\s+(?P<tag>\S+)$')

        # 1.1.1.0/24  prefix attr X:0 R:1 N:0
        # 3.3.3.3/32  prefix attr X:0 R:0 N:1  source router id: 3.3.3.3  SID index 3 - Bound
        # 6.6.6.6/32  prefix attr X:0 R:0 N:1  source router id: 6.6.6.6  prefix SID index 61 - Bound (SR_POLICY)
        p2 = re.compile(r'^(?P<ip>\d+.\d+.\d+.\d+)/(?P<subnet>\d+)\s+prefix\s+attr\s+X:(?P<x_flag>0|1)\s+R:(?P<r_flag>0|1)\s+N:(?P<n_flag>0|1)'
        r'(\((?P<strict_sid_bound_attribute_te1>TE)\)){0,1}((\s+source router id:\s+(?P<src_router_id>\d+.\d+.\d+.\d+)){0,1}\s+'
        r'(((prefix SID index|SID index)\s+(?P<prefix_sid_ind>\d+))\s+){0,1}((- Bound){0,1}\s*(\((?P<sid_bound_attribute>\w+)\)'
        r'(\((?P<strict_sid_bound_attribute_te2>\w+)\)){0,1}){0,1}){0,1}){0,1}$')
        
        # [115/L1/70] via 6.6.6.6(MPLS-SR-Tunnel6) R3.00-00, from 4.4.4.4, tag 0
        # [115/L2/50] via 199.1.1.2(Tunnel4001), from 6.6.6.6, tag 0, LSP[105/209/18349]
        p3 = re.compile(r'^\[(?P<distance>\d+)/(?P<route_type>\w+\d+)/(?P<metric>\d+)\]\s+via\s+(?P<ip>\d+.\d+.\d+.\d+)'
                        r'\((?P<interface>[\w-]+\d+(\/\d+(\/\d+)?)?)\)( (?P<host>\S+),)?,* from (?P<from_ip>\d+.\d+.\d+.\d+),\s+tag'
                        r'\s+(?P<tag>\d+)(, LSP\[(?P<next_hop_lsp_index>\d+)/(?P<rtp_lsp_index>\d+)/(?P<rtp_lsp_version>\d+)\])?$')
        
        # LSP 3/4/0(52), prefix attr: X:0 R:0 N:1
        p4 = re.compile(r'^(LSP (?P<next_hop_lsp_index>\d+)/(?P<rtp_lsp_index>\d+)/(?P<rtp_lsp_version>\d+)'
                        r'\((?P<tpl_lsp_version>\d+)\))?(, )?prefix attr:\s+X:(?P<x_flag>0|1)\s+R:(?P<r_flag>0|1)'
                        r'\s+N:(?P<n_flag>0|1)$')

        # SRGB: 16000, range: 8000 prefix-SID index: 3, R:0 N:1 P:0 E:0 V:0 L:0
        p5 = re.compile(r'^SRGB:\s+(?P<srgb>\d+),\s+range:\s+(?P<range>\d+)\s+prefix-SID index:\s+(?P<pre_sid_ind>\w+|\d+)'
                        r'(,\s+R:(?P<r_flag>0|1)\s+N:(?P<n_flag>0|1)\s+P:(?P<p_flag>0|1)\s+E:(?P<e_flag>0|1)'
                        r'\s+V:(?P<v_flag>0|1)\s+L:(?P<l_flag>0|1))?$')

        #(ALT)(installed)
        #(installed)
        p6 = re.compile(r'^(\((?P<path_attr>TE|ALT|SRTE|SRTE_STRICT|SR_POLICY|SR_POLICY_STRICT)\)){0,1}(\((?P<installed>installed)\)){0,1}$')

        # label: implicit-null
        p7 = re.compile(r'^label:\s+(?P<label>\S+)$')

        # repair path: 5.5.5.5 (MPLS-SR-Tunnel4) metric: 65 (DS,SR)
        # repair path: 199.1.2.2(Tunnel4002) metric:50 (PP,LC,DS,NP,SR) LSP[115]
        p8 = re.compile(r'^repair path:\s+(?P<repair_path>\d+.\d+.\d+.\d+)\s*\((?P<interface>[\w-]+\d+(\/\d+(\/\d+)?)?)\)'
                        r'\s+metric:\s*(?P<metric>\d+)\s+\(((?P<pp>PP),)?((?P<lc>LC),)?((?P<ds>DS),)?((?P<np>NP),)?((?P<sr>SR))?\)'
                        r'(\s+LSP\[(?P<rtp_lsp_index>\d+)\])?$')

        # next-hop: 10.10.20.2 (Ethernet1/1)
        p9 = re.compile(r'^next-hop:\s+(?P<next_hop>\d+.\d+.\d+.\d+)\s+\((?P<interface>[\w-]+\d+(\/\d+(\/\d+)?)?)\)$')

        # P node: R5[5.5.5.5], label: 16005
        p10 = re.compile(r'^(?P<node_type>(P|PQ|Q))\s+node:\s+(?P<host>\S+)\[(?P<ip>\d+.\d+.\d+.\d+)\],\s+label:\s+(?P<label>\S+)$')

        # repair source: R3, LSP 3
        p11 = re.compile(r'^repair source:\s+(?P<repair_src>\S+),\s+LSP\s+(?P<rtp_lsp_index>\d+)$')

        # Source router id: 3.3.3.3
        p12 = re.compile(r'Source router id:\s+(?P<src_router_id>\d+.\d+.\d+.\d+)')

        # strict-SPF label: implicit-null
        p13 = re.compile(r'^strict-SPF label:\s+(?P<strict_sid_label>\S+)$')

        # strict-SPF SID index: 6, R:0 N:1 P:0 E:0 V:0 L:0
        p14 = re.compile(r'^strict-SPF SID index:\s+(?P<strict_spf_sid_ind>\d+),\s+R:(?P<r_flag>0|1)'
                         r'\s+N:(?P<n_flag>0|1)\s+P:(?P<p_flag>0|1)\s+E:(?P<e_flag>0|1)\s+V:(?P<v_flag>0|1)'
                         r'\s+L:(?P<l_flag>0|1)$')

        # type: Micro-Loop Avoidance Explicit-Path
        p15 = re.compile(r'^type:\s+(?P<u_loop_enabled>Micro-Loop Avoidance Explicit-Path)$')

        # strict-SPF SID index 6 - Bound (SR_POLICY_STRICT)
        # strict-SPF SID index 505 - Bound(TE)
        p16 = re.compile(r'^strict-SPF SID index\s+(?P<strict_sid_index>\d+)\s+-\s+Bound\s*\((?P<strict_attribute>\S+)\)$')
        
        # TI-LFA link-protecting
        # local LFA
        # remote LFA
        p17 = re.compile(r'^(?P<lfa_type>local LFA|remote LFA|TI-LFA link-protecting)$')

        # Flex-algo 128
        p18 = re.compile(r'^Flex-algo\s+(?P<flex_algo>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # IPv4 local RIB for IS-IS process 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tag = group["tag"]
                ret_dict.setdefault("tag", {}).setdefault(tag, {})
                continue

            # Flex-algo 128
            m = p18.match(line)
            if m:
                group = m.groupdict()
                ret_dict["tag"][tag]["flex-algo"] = int(group['flex_algo'])
                continue

            # 1.1.1.0/24  prefix attr X:0 R:1 N:0
            # 3.3.3.3/32  prefix attr X:0 R:0 N:1  source router id: 3.3.3.3  SID index 3 - Bound
            # 6.6.6.6/32  prefix attr X:0 R:0 N:1  source router id: 6.6.6.6  prefix SID index 61 - Bound (SR_POLICY)
            m = p2.match(line)
            if m:
                in_repair_path = False
                group = m.groupdict()
                ip = group['ip']
                src_router_id = group['src_router_id']
                prefix_sid_ind = group['prefix_sid_ind']
                sid_bound_attr = group['sid_bound_attribute']
                
                ret_dict["tag"][tag].setdefault("prefix", {}).setdefault(ip, {})
                ret_dict["tag"][tag]["prefix"][ip]["subnet"] = group["subnet"]

                prefix_attr = {
                    "x_flag": (group['x_flag'] == "1"),
                    "r_flag": (group['r_flag'] == "1"),
                    "n_flag": (group['n_flag'] == "1")
                }

                ret_dict["tag"][tag]["prefix"][ip].setdefault("prefix_attr", prefix_attr)

                if src_router_id:
                  ret_dict["tag"][tag]["prefix"][ip]["source_router_id"] = src_router_id

                if prefix_sid_ind:
                  ret_dict["tag"][tag]["prefix"][ip]["prefix_sid_index"] = int(prefix_sid_ind)

                if sid_bound_attr and sid_bound_attr == "SR_POLICY_STRICT":
                    ret_dict["tag"][tag]["prefix"][ip]["strict_sid_bound_attribute"] = sid_bound_attr
                elif sid_bound_attr:
                  ret_dict["tag"][tag]["prefix"][ip]["sid_bound_attribute"] = sid_bound_attr
                
                strict_sid_bound_attribute_te = (group["strict_sid_bound_attribute_te1"] == "TE" or group["strict_sid_bound_attribute_te2"] == "TE")
                ret_dict["tag"][tag]["prefix"][ip]["strict_sid_bound_attribute_te"] = strict_sid_bound_attribute_te
                continue

            # [115/L1/70] via 6.6.6.6(MPLS-SR-Tunnel6) R3.00-00, from 4.4.4.4, tag 0
            # [115/L2/50] via 199.1.1.2(Tunnel4001), from 6.6.6.6, tag 0, LSP[105/209/18349]
            m = p3.match(line)
            if m:
                group = m.groupdict()
                distance = group["distance"]
                route_type = group["route_type"]
                metric = group["metric"]
                via_ip = group["ip"]
                interface = group["interface"]
                host = group["host"]
                src_ip = group["from_ip"]
                tag_ = group["tag"]
                next_hop_lsp_index = group["next_hop_lsp_index"]
                rtp_lsp_index = group["rtp_lsp_index"]
                rtp_lsp_version = group["rtp_lsp_version"]

                ret_dict["tag"][tag]["prefix"][ip].setdefault("via_interface", {}).setdefault(interface, {})

                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["distance"]) =  int(distance)

                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["route_type"]) =  route_type

                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["metric"]) =  int(metric)

                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["via_ip"]) =  via_ip

                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["src_ip"]) =  src_ip

                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["tag"]) =  tag_
                if host:
                    (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                             [interface]["host"]) =  host

                ret_dict["tag"][tag]["prefix"][ip]["via_interface"][interface].setdefault("lsp", {})

                if next_hop_lsp_index:
                    (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                             [interface]["lsp"]["next_hop_lsp_index"]) = int(next_hop_lsp_index)

                if rtp_lsp_index:
                    (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                             [interface]["lsp"]["rtp_lsp_index"]) = int(rtp_lsp_index)

                if rtp_lsp_version:
                    (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                             [interface]["lsp"]["rtp_lsp_version"]) = int(rtp_lsp_version)
                continue

            # LSP 3/4/0(52), prefix attr: X:0 R:0 N:1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                next_hop_lsp_index = group["next_hop_lsp_index"]
                rtp_lsp_index = group["rtp_lsp_index"]
                rtp_lsp_version = group["rtp_lsp_version"]
                tpl_lsp_version = group["tpl_lsp_version"]

                if next_hop_lsp_index:
                    (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                             [interface]["lsp"]["next_hop_lsp_index"]) = int(next_hop_lsp_index)

                if rtp_lsp_index:
                    (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                             [interface]["lsp"]["rtp_lsp_index"]) = int(rtp_lsp_index)

                if rtp_lsp_version:
                    (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                             [interface]["lsp"]["rtp_lsp_version"]) = int(rtp_lsp_version)

                if tpl_lsp_version:
                    (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                            [interface]["lsp"]["tpl_lsp_version"]) = int(tpl_lsp_version)

                prefix_att = {
                    "x_flag": (group['x_flag'] == "1"),
                    "r_flag": (group['r_flag'] == "1"),
                    "n_flag": (group['n_flag'] == "1")
                }

                ret_dict["tag"][tag]["prefix"][ip]["via_interface"][interface].setdefault("prefix_attr", prefix_attr)
                continue

            # SRGB: 16000, range: 8000 prefix-SID index: 3, R:0 N:1 P:0 E:0 V:0 L:0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                srgb = int(group["srgb"])
                srgb_range = int(group["range"])

                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["srgb"]) = srgb

                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["srgb_range"]) = srgb_range

                if group["pre_sid_ind"] != "None":
                    (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                             [interface]["prefix_sid_index"]) = int(group["pre_sid_ind"])

                if group["r_flag"] and group["n_flag"] and group["p_flag"] and group["e_flag"] and group["v_flag"] and group["l_flag"]:
                    flags = {
                        "r_flag": (group["r_flag"] == "1"),
                        "n_flag": (group["n_flag"] == "1"),
                        "p_flag": (group["p_flag"] == "1"),
                        "e_flag": (group["e_flag"] == "1"),
                        "v_flag": (group["v_flag"] == "1"),
                        "l_flag": (group["l_flag"] == "1")
                    }
                    ret_dict["tag"][tag]["prefix"][ip]["via_interface"][interface].setdefault("non_strict_sid_flags", flags)
                continue

            # (ALT)(installed)
            # (installed)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if group["path_attr"]:
                    (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                             [interface]["path_attribute"]) = group["path_attr"]

                if group["installed"]:
                    (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                             [interface]["installed"]) = (group["installed"] == "installed")
                continue


            # label: implicit-null
            m = p7.match(line)
            if m:
                group = m.groupdict()
                if in_repair_path:
                    (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                             [interface]["repair_path"]["label"]) = group["label"]
                else:
                    (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                             [interface]["label"]) = group["label"]
                continue

            # repair path: 5.5.5.5 (MPLS-SR-Tunnel4) metric: 65 (DS,SR)
            # repair path: 199.1.2.2(Tunnel4002) metric:50 (PP,LC,DS,NP,SR) LSP[115]
            m = p8.match(line)
            if m:
                in_repair_path = True
                group = m.groupdict()

                rp_rtp_lsp_index = group["rtp_lsp_index"]

                ret_dict["tag"][tag]["prefix"][ip]["via_interface"][interface].setdefault("repair_path", {})

                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["repair_path"]["ip"]) = group["repair_path"]

                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["repair_path"]["interface"]) = group["interface"]

                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["repair_path"]["metric"]) = int(group["metric"])

                if rp_rtp_lsp_index:
                    (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                             [interface]["repair_path"]["rtp_lsp_index"]) = int(rp_rtp_lsp_index)

                attributes  = {
                        "DS": (group["ds"] == "DS"),
                        "LC": (group["lc"] == "LC"),
                        "NP": (group["np"] == "NP"),
                        "PP": (group["pp"] == "PP"),
                        "SR": (group["sr"] == "SR")
                }

                ret_dict["tag"][tag]["prefix"][ip]["via_interface"][interface]["repair_path"].setdefault("attributes", attributes)
                continue

            # next-hop: 10.10.20.2 (Ethernet1/1)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                next_hop_ip = group["next_hop"]
                next_hop_interface = group["interface"]

                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["repair_path"]["next_hop_ip"]) = next_hop_ip

                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["repair_path"]["next_hop_interface"]) = next_hop_interface
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
                ret_dict["tag"][tag]["prefix"][ip]["via_interface"][interface]["repair_path"].setdefault("nodes", {}).setdefault("host", {}).setdefault(host, node_dict)
                continue

            # repair source: R3, LSP 3
            m = p11.match(line)
            if m:
                group = m.groupdict()
                rs_rtp_lsp_index = group["rtp_lsp_index"]
                ret_dict["tag"][tag]["prefix"][ip]["via_interface"][interface].setdefault("repair_source", {})

                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["repair_source"]["host"]) = group["repair_src"]

                if rs_rtp_lsp_index:
                    (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                             [interface]["repair_source"]["rtp_lsp_index"]) = int(rs_rtp_lsp_index)
                continue

            # Source router id: 3.3.3.3
            m = p12.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["src_router_id"]) = group["src_router_id"]
                continue


            # strict-SPF label: implicit-null
            m = p13.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["strict_spf_label"]) = group["strict_sid_label"]
                continue

            # strict-SPF SID index: 6, R:0 N:1 P:0 E:0 V:0 L:0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["strict_spf_sid_index"]) = int(group["strict_spf_sid_ind"])

                if group["r_flag"] and group["n_flag"] and group["p_flag"] and group["e_flag"] and group["v_flag"] and group["l_flag"]:
                    flags = {
                        "r_flag": (group["r_flag"] == "1"),
                        "n_flag": (group["n_flag"] == "1"),
                        "p_flag": (group["p_flag"] == "1"),
                        "e_flag": (group["e_flag"] == "1"),
                        "v_flag": (group["v_flag"] == "1"),
                        "l_flag": (group["l_flag"] == "1")
                    }
                    ret_dict["tag"][tag]["prefix"][ip]["via_interface"][interface].setdefault("strict_spf_sid_flags", flags)
                continue

            # type: Micro-Loop Avoidance Explicit-Path
            m = p15.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["u_loop_enabled"]) = True
                continue

            # strict-SPF SID index 6 - Bound (SR_POLICY_STRICT)
            # strict-SPF SID index 505 - Bound(TE)
            m = p16.match(line)
            if m:
                group = m.groupdict()
                strict_attribute = group["strict_attribute"]
                (ret_dict["tag"][tag]["prefix"]
                         [ip]["strict_spf_sid_index"]) = int(group["strict_sid_index"])
                        
                if strict_attribute == "TE":
                    (ret_dict["tag"][tag]["prefix"]
                         [ip]["strict_sid_bound_attribute_te"]) = True
                else:
                    (ret_dict["tag"][tag]["prefix"]
                            [ip]["strict_sid_bound_attribute"]) = group["strict_attribute"]
                continue

            # TI-LFA link-protecting
            # local LFA
            # remote LFA
            m = p17.match(line)
            if m:
                group = m.groupdict()
                (ret_dict["tag"][tag]["prefix"][ip]["via_interface"]
                         [interface]["repair_path"]["lfa_type"]) = group["lfa_type"]
                continue

        return ret_dict
