"""show_mld.py

NXOS parsers for the following show commands:

    * show ipv6 mld interface
    * show ipv6 mld interface vrf all
    * show ipv6 mld interface detail vrf <WORD>
    * show ipv6 mld groups
    * show ipv6 mld groups vrf all
    * show ipv6 mld groups vrf <WORD>
    * show ipv6 mld local-groups
    * show ipv6 mld local-groups vrf all
    * show ipv6 mld local-groups vrf <WORD>

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# import parser utils
from genie.libs.parser.utils.common import Common

# ==============================================
# Parser for 'show ipv6 mld interface'
# Parser for 'show ipv6 mld interface vrf all'
# Parser for 'show ipv6 mld interface vrf <vrf>'
# ==============================================

class ShowIpv6MldInterfaceSchema(MetaParser):
    """Schema for:
        show ipv6 mld interface
        show ipv6 mld interface vrf all
        show ipv6 mld interface vrf <vrf>"""

    schema = {'vrfs': {
                Any(): {
                    Optional('interface'): {
                        Any(): {
                            'enable': bool,
                            'link_status': str,
                            'oper_status': str,
                            Optional('ipv6'): {
                                Any(): {
                                    'ip': str,
                                    'prefix_length': str,
                                    'status': str,
                                },
                            },
                            Optional('link_local'): {
                                'address': str,
                                'status': str,
                                Optional('ipv6_address'): str,
                            },
                            Optional('querier'): str,
                            Optional('querier_version'): int,
                            Optional('next_query_sent_in'): str,
                            Optional('membership_count'): int,
                            Optional('version'): int,
                            Optional('host_version'): int,
                            Optional('query_interval'): int,
                            Optional('configured_query_interval'): int,
                            Optional('query_max_response_time'): int,
                            Optional('configured_query_max_response_time'): int,
                            Optional('startup_query'): {
                                Optional('configured_interval'): int,
                                Optional('interval'): int,
                                Optional('count'): int,
                            },
                            Optional('last_member'): {                                
                                Optional('mrt'): int,
                                Optional('query_count'): int,
                            },
                            Optional('group_timeout'): int,
                            Optional('configured_group_timeout'): int,
                            Optional('querier_timeout'): int,
                            Optional('configured_querier_timeout'): int,
                            Optional('unsolicited_report_interval'): int,
                            Optional('robustness_variable'): int,
                            Optional('configured_robustness_variable'): int,
                            Optional('link_local_groups_reporting'): bool,
                            Optional('immediate_leave'): bool,
                            Optional('enable_refcount'): int,
                            Optional('group_policy'): str,
                            Optional('max_groups'): int,
                            Optional('available_groups'): int,
                            Optional('statistics'): {
                                'sent' :{
                                    Any(): int,
                                },
                                'received' :{
                                    Any(): int,
                                }
                            }
                        }
                    },
                },
            },
        }

class ShowIpv6MldInterface(ShowIpv6MldInterfaceSchema):
    """Parser for:
        show ipv6 mld interface
        show ipv6 mld interface vrf all
        show ipv6 mld interface vrf <vrf>"""

    cli_command = ['show ipv6 mld interface vrf {vrf}', 'show ipv6 mld interface']

    def cli(self, vrf='', output=None):
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            cmd = self.cli_command[1]

        # excute command to get output
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # ICMPv6 MLD Interfaces for VRF "VRF1"
            p1 = re.compile(r'^ICMPv6 +MLD +Interfaces +for +VRF +\"(?P<vrf>\S+)\"$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                continue

            # Ethernet2/1, Interface status: protocol-up/link-up/admin-up
            p2 = re.compile(r'^(?P<intf>[\w\/\.\-]+), +'
                             'Interface +status: +protocol\-(?P<protocol_status>\w+)\/'
                             'link\-(?P<link_status>\w+)\/'
                             'admin\-(?P<admin_status>\w+)$')
            m = p2.match(line)
            if m:
                intf = m.groupdict()['intf']

                if 'vrfs' not in ret_dict:
                    ret_dict['vrfs'] = {}
                if vrf not in ret_dict['vrfs']:
                    ret_dict['vrfs'][vrf] = {}

                if 'interface' not in ret_dict['vrfs'][vrf]:
                    ret_dict['vrfs'][vrf]['interface'] = {}

                if intf not in ret_dict['vrfs'][vrf]['interface']:
                    ret_dict['vrfs'][vrf]['interface'][intf] = {}

                ret_dict['vrfs'][vrf]['interface'][intf]['oper_status'] = m.groupdict()['protocol_status']
                ret_dict['vrfs'][vrf]['interface'][intf]['link_status'] = m.groupdict()['link_status']
                ret_dict['vrfs'][vrf]['interface'][intf]['enable'] = True if \
                    m.groupdict()['admin_status'].lower() == 'up' else False
                continue

            # 2001:db1:1::1/64 [VALID]
            p3 = re.compile(r'^(?P<address>(?P<ip>[a-z0-9\:]+)'
                             '\/(?P<prefix_length>[0-9]+))'
                             ' *\[(?P<status>[a-zA-Z]+)\]$')
            m = p3.match(line)
            if m:
                ip  = m.groupdict()['ip']
                prefix_length = m.groupdict()['prefix_length']
                address = m.groupdict()['address']
                status = m.groupdict()['status'].lower()

                if 'ipv6' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['ipv6'] = {}
                if address not in ret_dict['vrfs'][vrf]['interface'][intf]['ipv6']:
                    ret_dict['vrfs'][vrf]['interface'][intf]['ipv6'][address] = {}
                
                ret_dict['vrfs'][vrf]['interface'][intf]['ipv6'][address]\
                    ['ip'] = ip

                ret_dict['vrfs'][vrf]['interface'][intf]['ipv6'][address]\
                    ['prefix_length'] = prefix_length

                ret_dict['vrfs'][vrf]['interface'][intf]['ipv6'][address]\
                    ['status'] = status
                continue

            # Link Local Address : fe80::5054:ff:fed7:c01f(VALID)
            p3_1 = re.compile(r'^Link +Local +Address *: *'
                             '(?P<address>[\w\:]+)'
                             '\((?P<status>[a-zA-Z]+)\)$')
            m = p3_1.match(line)
            if m:
                if 'link_local' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['link_local'] = {}
                
                ret_dict['vrfs'][vrf]['interface'][intf]['link_local']['address'] = \
                    m.groupdict()['address']

                ret_dict['vrfs'][vrf]['interface'][intf]['link_local']['status'] = \
                    m.groupdict()['status'].lower()
                continue

            # IPv6 Link-local Address: fe80::5054:ff:fed7:c01f
            p3_2 = re.compile(r'^IPv6 +Link\-local +Address *: *'
                             '(?P<address>[\w\:]+)$')
            m = p3_2.match(line)
            if m:
                if 'link_local' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['link_local'] = {}
                
                ret_dict['vrfs'][vrf]['interface'][intf]['link_local']['ipv6_address'] = \
                    m.groupdict()['address']
                continue

            # Active Querier: fe80::5054:ff:fed7:c01f
            p4 = re.compile(r'^Active +Querier: +(?P<querier>[\w\.\:]+)$')
            m = p4.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['querier'] = m.groupdict()['querier']
                continue

            # Querier version: 2, next query sent in: 00:05:18
            p4_1 = re.compile(r'^Querier +version: +(?P<version>\d+), +'
                             'next +query +sent +in: +(?P<in>[\w\.\:]+)$')
            m = p4_1.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['querier_version'] = int(m.groupdict()['version'])
                ret_dict['vrfs'][vrf]['interface'][intf]['next_query_sent_in'] = m.groupdict()['in']
                continue

            # MLD Membership count: 2
            p5 = re.compile(r'^MLD +Membership +count: +(?P<count>\d+)$')
            m = p5.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['membership_count'] = \
                    int(m.groupdict()['count'])
                continue

            # MLD version: 2, host version: 2
            p7 = re.compile(r'^MLD +version: +(?P<ver>\d+), +'
                             'host +version: +(?P<host_ver>\d+)$')
            m = p7.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['version'] = \
                    int(m.groupdict()['ver'])
                ret_dict['vrfs'][vrf]['interface'][intf]['host_version'] = \
                    int(m.groupdict()['host_ver'])
                continue

            # MLD query interval: 366 secs, configured value: 366 secs
            p8 = re.compile(r'^MLD +query +interval: +(?P<intverval>\d+) +secs, +'
                             'configured +value: +(?P<conf_intvl>\d+) +secs$')
            m = p8.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['query_interval'] = \
                    int(m.groupdict()['intverval'])
                ret_dict['vrfs'][vrf]['interface'][intf]['configured_query_interval'] = \
                    int(m.groupdict()['conf_intvl'])
                continue

            # MLD max response time: 16 secs, configured value: 16 secs
            p9 = re.compile(r'^MLD +max +response +time: +(?P<time>\d+) +secs, +'
                             'configured +value: +(?P<conf_time>\d+) +secs$')
            m = p9.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['query_max_response_time'] = \
                    int(m.groupdict()['time'])
                ret_dict['vrfs'][vrf]['interface'][intf]['configured_query_max_response_time'] = \
                    int(m.groupdict()['conf_time'])
                continue

            # MLD startup query interval: 91 secs, configured value: 31 secs
            p10 = re.compile(r'^MLD +startup +query +interval: +(?P<intvl>\d+) +secs, +'
                             'configured +value: +(?P<conf_intvl>\d+) +secs$')
            m = p10.match(line)
            if m:
                if 'startup_query' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['startup_query'] = {}
                ret_dict['vrfs'][vrf]['interface'][intf]['startup_query']['interval'] = \
                    int(m.groupdict()['intvl'])
                ret_dict['vrfs'][vrf]['interface'][intf]['startup_query']['configured_interval'] = \
                    int(m.groupdict()['conf_intvl'])
                continue

            # MLD startup query count: 7
            p11 = re.compile(r'^MLD +startup +query +count: +(?P<count>\d+)$')
            m = p11.match(line)
            if m:
                if 'startup_query' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['startup_query'] = {}
                ret_dict['vrfs'][vrf]['interface'][intf]['startup_query']['count'] = \
                    int(m.groupdict()['count'])
                continue

            # MLD last member mrt: 1 secs
            p12 = re.compile(r'^MLD +last +member +mrt: +(?P<mrt>\d+) +secs$')
            m = p12.match(line)
            if m:
                if 'last_member' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['last_member'] = {}
                ret_dict['vrfs'][vrf]['interface'][intf]['last_member']['mrt'] = \
                    int(m.groupdict()['mrt'])
                continue

            # MLD last member query count: 7
            p13 = re.compile(r'^MLD +last +member +query +count: +(?P<count>\d+)$')
            m = p13.match(line)
            if m:
                if 'last_member' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['last_member'] = {}
                ret_dict['vrfs'][vrf]['interface'][intf]['last_member']['query_count'] = \
                    int(m.groupdict()['count'])
                continue

            # MLD group timeout: 2578 secs, configured value: 260 secs
            p14 = re.compile(r'^MLD +group +timeout: +(?P<timeout>\d+) +secs, +'
                             'configured +value: +(?P<conf_timeout>\d+) +secs$')
            m = p14.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['group_timeout'] = \
                    int(m.groupdict()['timeout'])
                ret_dict['vrfs'][vrf]['interface'][intf]['configured_group_timeout'] = \
                    int(m.groupdict()['conf_timeout'])
                continue

            # MLD querier timeout: 2570 secs, configured value: 255 secs
            p15 = re.compile(r'^MLD +querier +timeout: +(?P<timeout>\d+) +secs, +'
                             'configured +value: +(?P<conf_timeout>\d+) +secs$')
            m = p15.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['querier_timeout'] = \
                    int(m.groupdict()['timeout'])
                ret_dict['vrfs'][vrf]['interface'][intf]['configured_querier_timeout'] = \
                    int(m.groupdict()['conf_timeout'])
                continue

            # MLD unsolicited report interval: 1 secs
            p16 = re.compile(r'^MLD +unsolicited +report +interval: +(?P<val>\d+) +secs$')
            m = p16.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['unsolicited_report_interval'] = \
                    int(m.groupdict()['val'])
                continue

            # MLD robustness variable: 7, configured value: 7
            p17 = re.compile(r'^MLD +robustness +variable: +(?P<val1>\d+), +'
                              'configured +value: +(?P<val2>\d+)$')
            m = p17.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['robustness_variable'] = \
                    int(m.groupdict()['val1'])
                ret_dict['vrfs'][vrf]['interface'][intf]['configured_robustness_variable'] = \
                    int(m.groupdict()['val2'])
                continue

            # MLD reporting for link-local groups: disabled
            p18 = re.compile(r'^MLD +reporting +for +link\-local +groups: +(?P<status>\w+)$')
            m = p18.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['link_local_groups_reporting'] = True \
                    if 'enable' in m.groupdict()['status'].lower() else False
                continue

            # MLD interface enable refcount: 4
            p19 = re.compile(r'^MLD +interface +enable +refcount: +(?P<count>\d+)$')
            m = p19.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['enable_refcount'] = \
                    int(m.groupdict()['count'])
                continue

            # MLD immediate leave: enabled
            p20 = re.compile(r'^MLD +immediate +leave: +(?P<status>\w+)$')
            m = p20.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['immediate_leave'] = True \
                    if 'enable' in m.groupdict()['status'].lower() else False
                continue

            # MLD Report Policy: test
            p22 = re.compile(r'^MLD +Report +Policy: +(?P<policy>\S+)$')
            m = p22.match(line)
            if m:
                if m.groupdict()['policy'] != 'None':
                    ret_dict['vrfs'][vrf]['interface'][intf]['group_policy'] = \
                        m.groupdict()['policy']
                continue

            # MLD State Limit: 6400,  Available States: 6400
            p23 = re.compile(r'^MLD +State +Limit: +(?P<max_groups>\d+), +'
                              'Available +States: +(?P<available_groups>\d+)$')
            m = p23.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['max_groups'] = \
                    int(m.groupdict()['max_groups'])

                ret_dict['vrfs'][vrf]['interface'][intf]['available_groups'] = \
                    int(m.groupdict()['available_groups'])
                continue

            # ICMPv6 MLD Statistics (sent/received):
            #   V1 Queries:          0/0
            #   V1 Leaves :          0/0
            p25 = re.compile(r'^(?P<title>[\w\s]+) *: +(?P<sent1>\d+)\/(?P<received1>\d+)$')
            m = p25.match(line)
            if m:
                if 'statistics' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['statistics'] = {}

                if 'sent' not in ret_dict['vrfs'][vrf]['interface'][intf]['statistics']:
                    ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['sent'] = {}
                if 'received' not in ret_dict['vrfs'][vrf]['interface'][intf]['statistics']:
                    ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['received'] = {}

                title = m.groupdict()['title'].strip().lower().replace(' ', '_')

                ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['sent'][title] = \
                    int(m.groupdict()['sent1'])

                ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['received'][title] = \
                    int(m.groupdict()['received1'])
                continue

        return ret_dict


# ===========================================
# Parser for 'show ipv6 mld groups'
# Parser for 'show ipv6 mld groups vrf all'
# Parser for 'show ipv6 mld groups vrf <vrf>'
# ===========================================
class ShowIpv6MldGroupsSchema(MetaParser):
    """Schema for:
        show ipv6 mld groups
        show ipv6 mld groups vrf all
        show ipv6 mld groups vrf <vrf>"""

    schema = {'vrfs': {
                Any(): {
                    'groups_count': int,
                    Optional('interface'): {
                        Any(): {
                            'group': {
                                Any(): {
                                    Optional('source'): {
                                        Any(): {
                                            'expire': str,
                                            'up_time': str,
                                            'last_reporter':str,
                                            'type': str,
                                        }
                                    },
                                    Optional('expire'): str,
                                    Optional('up_time'): str,
                                    Optional('last_reporter'): str,
                                    Optional('type'): str,
                                }
                            }
                        },
                    },
                },
            }
        }

class ShowIpv6MldGroups(ShowIpv6MldGroupsSchema):
    """Parser for:
        show ipv6 mld groups
        show ipv6 mld groups vrf all
        show ipv6 mld groups vrf <vrf>"""
    cli_command = ['show ipv6 mld groups vrf {vrf}', 'show ipv6 mld groups']

    def cli(self, vrf='', output=None):
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            cmd = self.cli_command[1]

        # excute command to get output
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables
        ret_dict = {}
        source = None
        group = None
        sub_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # MLD Connected Group Membership for VRF "default" - 2 total entries
            p1 = re.compile(r'^MLD +Connected +Group +Membership +for +VRF +\"(?P<vrf>\S+)\"'
                             ' +\- +(?P<entries>\d+) +total +entries$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']

                if 'vrfs' not in ret_dict:
                    ret_dict['vrfs'] = {}
                if vrf not in ret_dict['vrfs']:
                    ret_dict['vrfs'][vrf] = {}

                ret_dict['vrfs'][vrf]['groups_count'] = int(m.groupdict()['entries'])
                continue

            # (2001:db8:0:abcd::2, ff30::2)
            p2 = re.compile(r'^\((?P<source>[\w\.\:\*]+), *(?P<group>[\w\.\:]+)\)$')
            m = p2.match(line)
            if m:
                group = m.groupdict()['group']
                source = m.groupdict()['source']
                continue

            # Type: Static, Interface: Ethernet2/1
            p3 = re.compile(r'^Type: +(?P<type>\w+), Interface: +(?P<intf>[\w\.\/\-]+)$')
            m = p3.match(line)
            if m:
                intf = m.groupdict()['intf'].capitalize()
                if 'interface' not in ret_dict['vrfs'][vrf]:
                    ret_dict['vrfs'][vrf]['interface'] = {}
                if intf not in ret_dict['vrfs'][vrf]['interface']:
                    ret_dict['vrfs'][vrf]['interface'][intf] = {}


                if 'group' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'] = {}
                if group and group not in ret_dict['vrfs'][vrf]['interface'][intf]['group']:
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group] = {}

                if source and source != '*':
                    if 'source' not in ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]:
                        ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source'] = {}
                    if source not in ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source']:
                        ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source'][source] = {}

                    sub_dict = ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source'][source]
                else:
                    sub_dict = ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]

                sub_dict['type'] = m.groupdict()['type'].lower()
                continue

            # Uptime/Expires: 00:26:28/never, Last Reporter: 2001:db1:1:1::1
            p4 = re.compile(r'^Uptime\/Expires *: +(?P<uptime>[\w\.\:]+)/(?P<expires>[\w\.\:]+), +'
                             'Last +Reporter *: +(?P<last_reporter>[\w\.\:]+)$')
            m = p4.match(line)
            if m:
                sub_dict['expire'] = m.groupdict()['expires']
                sub_dict['up_time'] = m.groupdict()['uptime']
                sub_dict['last_reporter'] = m.groupdict()['last_reporter']
                continue

        return ret_dict


# ===========================================
# Schema for 'show ipv6 mld local-groups'
# Schema for 'show ipv6 mld local-groups vrf all'
# Schema for 'show ipv6 mld local-groups vrf <vrf>'
# ===========================================
class ShowIpv6MldLocalGroupsSchema(MetaParser):
    """Schema for:
        show ipv6 mld local-groups
        show ipv6 mld local-groups vrf all
        show ipv6 mld local-groups vrf <vrf>"""

    schema = {'vrfs': {
                Any(): {
                    Optional('interface'): {
                        Any(): {
                            Optional('join_group'): {
                                Any(): {
                                    'group': str,
                                    'source': str
                                },
                            },
                            Optional('static_group'): {
                                Any(): {
                                    'group': str,
                                    'source': str
                                },
                            },
                            'group': {
                                Any(): {
                                    Optional('source'): {
                                        Any(): {
                                            'last_reported':str,
                                            'type': str,
                                        }
                                    },
                                    Optional('last_reported'): str,
                                    Optional('type'): str,
                                }
                            }
                        },
                    },
                },
            }
        }

class ShowIpv6MldLocalGroups(ShowIpv6MldLocalGroupsSchema):
    """Parser for:
        show ipv6 mld local-groups
        show ipv6 mld local-groups vrf all
        show ipv6 mld local-groups vrf <vrf>"""
    cli_command = ['show ipv6 mld local-groups vrf {vrf}','show ipv6 mld local-groups']

    def cli(self, vrf='', output=None):
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            cmd = self.cli_command[1]

        # excute command to get output
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables
        ret_dict = {}
        group = None
        source = None

        for line in out.splitlines():
            line = line.strip()

            # MLD Locally Joined Group Membership for VRF "default"
            p1 = re.compile(r'^MLD +Locally +Joined +Group +Membership +for +VRF +\"(?P<vrf>\S+)\"$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']

                if 'vrfs' not in ret_dict:
                    ret_dict['vrfs'] = {}
                if vrf not in ret_dict['vrfs']:
                    ret_dict['vrfs'][vrf] = {}
                continue

            # Group   Type     Interface   Last Reported 
            # (*, fffe::1)
            p2 = re.compile(r'^\((?P<source>[\w\.\:\*]+), *(?P<group>[\w\.\:]+)\)$')
            m = p2.match(line)
            if m:
                group = m.groupdict()['group']
                source = m.groupdict()['source']
                continue

            #         Local    Eth2/1      00:03:07  
            p2_1 = re.compile(r'^(?P<type>\w+) +(?P<intf>[\w\.\-\/]+) +'
                               '(?P<last_reported>[\w\.\:]+)$')
            m = p2_1.match(line)
            if m:
                intf = Common.convert_intf_name(m.groupdict()['intf'])
                if 'interface' not in ret_dict['vrfs'][vrf]:
                    ret_dict['vrfs'][vrf]['interface'] = {}
                if intf not in ret_dict['vrfs'][vrf]['interface']:
                    ret_dict['vrfs'][vrf]['interface'][intf] = {}

                if 'group' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'] = {}

                if group and group not in ret_dict['vrfs'][vrf]['interface'][intf]['group']:
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group] = {}

                group_type = m.groupdict()['type'].lower()

                if source and source != '*':
                    if 'source' not in ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]:
                        ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source'] = {}
                    if source not in ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source']:
                        ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source'][source] = {}

                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]\
                        ['source'][source]['type'] = group_type
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]\
                        ['source'][source]['last_reported'] = m.groupdict()['last_reported']
                else:
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['type'] = group_type                    
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['last_reported'] = \
                        m.groupdict()['last_reported']

                # build static_group and join_group info
                if group_type == 'static':
                    key = 'static_group'
                else:
                    key = 'join_group'
                if key not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf][key] = {}
                if group and source:
                    build_group = group + ' ' + source
                    if build_group not in ret_dict['vrfs'][vrf]['interface'][intf][key]:
                        ret_dict['vrfs'][vrf]['interface'][intf][key][build_group] = {}
                    ret_dict['vrfs'][vrf]['interface'][intf][key][build_group]['group'] = group
                    ret_dict['vrfs'][vrf]['interface'][intf][key][build_group]['source'] = source
                continue

        return ret_dict

