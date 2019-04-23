
""" show_isis.py

IOSXE parsers for the following show commands:
    * show isis neighbors
    * show isis hostname
    * show isis lsp-log
    * show isis database detail

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


class ShowIsisNeighborsSchema(MetaParser):
    """Schema for show isis neighbors"""
    schema = {
        'isis': {
            Any(): {
                'neighbors': {
                    Any(): {
                        'type': {
                            Any(): {
                                'circuit_id': str,
                                'holdtime': str,
                                'interface': str,
                                'ip_address': str,
                                'state': str,
                            }
                        }
                    }
                }
            }
        }
    }

class ShowIsisNeighbors(ShowIsisNeighborsSchema):
    """Parser for show isis neighbors"""

    cli_command = 'show isis neighbors'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Tag isis_net:
            p1 = re.compile(r'^Tag +(?P<isis_name>\S+)\s*:$')
            m = p1.match(line)
            if m:
                isis_name = m.groupdict()['isis_name']
                isis_dict = ret_dict.setdefault('isis', {}).setdefault(isis_name, {})
                continue

            # LAB-9001-2      L1   Te0/0/26      10.239.7.29     UP    27       00
            p2 = re.compile(r'^(?P<system_id>\S+)\s+(?P<type>\S+)\s+(?P<interface>\S+)\s+'
                             '(?P<ip_address>\S+)\s+(?P<state>(UP|DOWN|INIT|NONE)+)\s+'
                             '(?P<holdtime>\S+)\s+(?P<circuit_id>\S+)$')
            m = p2.match(line)
            if m:
                system_id = m.groupdict()['system_id']
                isis_type = m.groupdict()['type']

                neighbour_dict = isis_dict.setdefault('neighbors', {}).setdefault(system_id, {})
                type_dict = neighbour_dict.setdefault('type', {}).setdefault(isis_type, {})

                type_dict['interface'] = m.groupdict()['interface']
                type_dict['ip_address'] = m.groupdict()['ip_address']
                type_dict['state'] = m.groupdict()['state']
                type_dict['holdtime'] = m.groupdict()['holdtime']
                type_dict['circuit_id'] = m.groupdict()['circuit_id']
                continue

        return ret_dict

class ShowIsisHostnameSchema(MetaParser):
    """Schema for show isis hostname"""

    schema = {
        'tag': {
            Any(): {
                'hostname_db': {
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
        p1 = re.compile(r'^Level +System +ID +Dynamic +Hostname +\((?P<tag>\w+)\)$')
        #  2     7777.7777.7777 R7
        #      * 2222.2222.2222 R2
        p2 = re.compile(r'^(?P<level>\d+)?(\s?(?P<star>\*))? +(?P<system_id>[\d\.]+) +(?P<dynamic_hostname>\w+)$')

        for line in out.splitlines():
            line = line.strip()

            #  Level  System ID      Dynamic Hostname  (VRF1)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tag_dict = result_dict.setdefault('tag', {}).setdefault(group['tag'],{})
                continue

            #  2     7777.7777.7777 R7
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
                            Any(): {
                                Any(): {
                                    'metric': int,
                                    Optional('mt_ipv6'): bool,
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
            ' +(?P<lsp_holdtime>[\d\*]+)(/(?P<lsp_rcvd>[\d\*]+))? +(?P<att>\d+)/(?P<p>\d+)/(?P<ol>\d+)$')
        #   Area Address: 49.0001
        p4 = re.compile(r'^Area +Address: +(?P<area_address>[\w\.]+)$')

        #   NLPID:        0xCC 0x8E
        p5 = re.compile(r'^NLPID: +(?P<nlp_id>[\w\s]+)$')

        #   Topology:     IPv4 (0x0)
        #                 IPv6 (0x4002 ATT)
        p6 = re.compile(r'^(Topology: +)?(?P<topology>(IP)+[\w]+) +\((?P<code>[\w\s]+)\)$')

        #   Hostname: R2
        p7 = re.compile(r'^Hostname: +(?P<hostname>\w+)$')
        #   IP Address:   66.66.66.66
        p8 = re.compile(r'^IP +Address: +(?P<ip_address>[\d\.]+)$')

        #   Metric: 10         IP 20.2.7.0/24
        p9 = re.compile(r'^Metric: +(?P<metric>\d+) +(?P<metric_topology>[\w\-]+)( +\((?P<mt_ipv6>[\w\-]+)\))? +(?P<ip>\S+)$')

        #   IPv6 Address: 2001:DB8:66:66:66::66
        p10 = re.compile(r'^IPv6 +Address: +(?P<ip_address>[\w\:]+)$')

        # Router ID:    77.77.77.77
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

            #   IP Address:   66.66.66.66
            m = p8.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.update({'ip_address': group['ip_address']})
                continue

            #  Metric: 10         IP 20.2.7.0/24
            #  Metric: 40         IS (MT-IPv6) R2.01
            #  Metric: 40         IS-Extended R2.01
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ip_dict = lsp_dict.setdefault(group['ip'], {}).setdefault(group['metric_topology'].lower(), {})
                ip_dict.update({'metric': int(group['metric'])})
                if group['mt_ipv6']:
                    ip_dict.update({'mt_ipv6': True})

                continue

            #   IPv6 Address: 2001:DB8:66:66:66::66
            m = p10.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.update({'ipv6_address': group['ip_address']})
                continue

            #  Router ID:    77.77.77.77
            m = p11.match(line)
            if m:
                group = m.groupdict()
                lsp_dict.update({'router_id': group['router_id']})
                continue

        return result_dict

