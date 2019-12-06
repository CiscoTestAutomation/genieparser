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
                    Optional('count'): int,
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
    exclude = [
        'next_query_sent_in',
        'address',
        'ipv6_address',
        'querier']

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

        # ICMPv6 MLD Interfaces for VRF "VRF1"
        p1 = re.compile(r'^ICMPv6 +MLD +Interfaces +for +VRF +\"(?P<vrf>\S+)\"$')

        # MLD Interfaces for VRF "VRF1", count: 4
        p1_1 = re.compile(r'^MLD +Interfaces +for +VRF +\"(?P<vrf>\S+)\", '
                           'count: +(?P<count>\d+)$')

        # Ethernet2/1, Interface status: protocol-up/link-up/admin-up
        p2 = re.compile(r'^(?P<intf>[\w\/\.\-]+), +'
                         'Interface +status: +protocol\-(?P<protocol_status>\w+)\/'
                         'link\-(?P<link_status>\w+)\/'
                         'admin\-(?P<admin_status>\w+)$')

        # 2001:db8:8404:751c::1/64 [VALID]
        p3 = re.compile(r'^(?P<address>(?P<ip>[a-z0-9\:]+)'
                         '\/(?P<prefix_length>[0-9]+))'
                         ' *\[(?P<status>[a-zA-Z]+)\]$')

        # Link Local Address : fe80::5054:ff:fed7:c01f(VALID)
        p3_1 = re.compile(r'^Link +Local +Address *: *'
                         '(?P<address>[\w\:]+)'
                         '\((?P<status>[a-zA-Z]+)\)$')

        # IPv6 Link-local Address: fe80::5054:ff:fed7:c01f
        p3_2 = re.compile(r'^IPv6 +Link\-local +Address *: *'
                         '(?P<address>[\w\:]+)$')

        # Active Querier: fe80::5054:ff:fed7:c01f
        p4 = re.compile(r'^Active +Querier: +(?P<querier>[\w\.\:]+)$')

        # Querier version: 2, next query sent in: 00:05:18
        p4_1 = re.compile(r'^Querier +version: +(?P<version>\d+), +'
                         'next +query +sent +in: +(?P<in>[\w\.\:]+)$')

        # MLD Membership count: 2
        p5 = re.compile(r'^MLD +Membership +count: +(?P<count>\d+)$')

        # MLD version: 2, host version: 2
        p7 = re.compile(r'^MLD +version: +(?P<ver>\d+), +'
                         'host +version: +(?P<host_ver>\d+)$')

        # MLD query interval: 366 secs, configured value: 366 secs
        p8 = re.compile(r'^MLD +query +interval: +(?P<intverval>\d+) +secs, +'
                         'configured +value: +(?P<conf_intvl>\d+) +secs$')

        # MLD max response time: 16 secs, configured value: 16 secs
        p9 = re.compile(r'^MLD +max +response +time: +(?P<time>\d+) +secs, +'
                         'configured +value: +(?P<conf_time>\d+) +secs$')

        # MLD startup query interval: 91 secs, configured value: 31 secs
        p10 = re.compile(r'^MLD +startup +query +interval: +(?P<intvl>\d+) +secs, +'
                         'configured +value: +(?P<conf_intvl>\d+) +secs$')

        # MLD startup query count: 7
        p11 = re.compile(r'^MLD +startup +query +count: +(?P<count>\d+)$')

        # MLD last member mrt: 1 secs
        p12 = re.compile(r'^MLD +last +member +mrt: +(?P<mrt>\d+) +secs$')

        # MLD last member query count: 7
        p13 = re.compile(r'^MLD +last +member +query +count: +(?P<count>\d+)$')

        # MLD group timeout: 2578 secs, configured value: 260 secs
        p14 = re.compile(r'^MLD +group +timeout: +(?P<timeout>\d+) +secs, +'
                         'configured +value: +(?P<conf_timeout>\d+) +secs$')

        # MLD querier timeout: 2570 secs, configured value: 255 secs
        p15 = re.compile(r'^MLD +querier +timeout: +(?P<timeout>\d+) +secs, +'
                         'configured +value: +(?P<conf_timeout>\d+) +secs$')

        # MLD unsolicited report interval: 1 secs
        p16 = re.compile(r'^MLD +unsolicited +report +interval: +(?P<val>\d+) +secs$')

        # MLD robustness variable: 7, configured value: 7
        p17 = re.compile(r'^MLD +robustness +variable: +(?P<val1>\d+), +'
                          'configured +value: +(?P<val2>\d+)$')

        # MLD reporting for link-local groups: disabled
        p18 = re.compile(r'^MLD +reporting +for +link\-local +groups: +(?P<status>\w+)$')

        # MLD interface enable refcount: 4
        p19 = re.compile(r'^MLD +interface +enable +refcount: +(?P<count>\d+)$')

        # MLD immediate leave: enabled
        p20 = re.compile(r'^MLD +immediate +leave: +(?P<status>\w+)$')

        # MLD Report Policy: test
        p22 = re.compile(r'^MLD +Report +Policy: +(?P<policy>\S+)$')

        # MLD State Limit: 6400,  Available States: 6400
        p23 = re.compile(r'^MLD +State +Limit: +(?P<max_groups>\d+), +'
                          'Available +States: +(?P<available_groups>\d+)$')

        # ICMPv6 MLD Statistics (sent/received):
        #   V1 Queries:          0/0
        #   V1 Leaves :          0/0
        p25 = re.compile(r'^(?P<title>[\w\s]+) *: +(?P<sent1>\d+)\/(?P<received1>\d+)$')

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # ICMPv6 MLD Interfaces for VRF "VRF1"
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                count = None
                continue

            # MLD Interfaces for VRF "VRF1", count: 4
            m = p1_1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                count = int(m.groupdict()['count'])
                continue

            # Ethernet2/1, Interface status: protocol-up/link-up/admin-up
            m = p2.match(line)
            if m:
                intf = m.groupdict()['intf']

                if 'vrfs' not in ret_dict:
                    ret_dict['vrfs'] = {}
                if vrf not in ret_dict['vrfs']:
                    ret_dict['vrfs'][vrf] = {}
                    if count:
                        ret_dict['vrfs'][vrf]['count'] = count

                if 'interface' not in ret_dict['vrfs'][vrf]:
                    ret_dict['vrfs'][vrf]['interface'] = {}

                if intf not in ret_dict['vrfs'][vrf]['interface']:
                    ret_dict['vrfs'][vrf]['interface'][intf] = {}

                ret_dict['vrfs'][vrf]['interface'][intf]['oper_status'] = m.groupdict()['protocol_status']
                ret_dict['vrfs'][vrf]['interface'][intf]['link_status'] = m.groupdict()['link_status']
                ret_dict['vrfs'][vrf]['interface'][intf]['enable'] = True if \
                    m.groupdict()['admin_status'].lower() == 'up' else False
                continue

            # 2001:db8:8404:751c::1/64 [VALID]
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
            m = p3_2.match(line)
            if m:
                if 'link_local' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['link_local'] = {}
                
                ret_dict['vrfs'][vrf]['interface'][intf]['link_local']['ipv6_address'] = \
                    m.groupdict()['address']
                continue

            # Active Querier: fe80::5054:ff:fed7:c01f
            m = p4.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['querier'] = m.groupdict()['querier']
                continue

            # Querier version: 2, next query sent in: 00:05:18
            m = p4_1.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['querier_version'] = int(m.groupdict()['version'])
                ret_dict['vrfs'][vrf]['interface'][intf]['next_query_sent_in'] = m.groupdict()['in']
                continue

            # MLD Membership count: 2
            m = p5.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['membership_count'] = \
                    int(m.groupdict()['count'])
                continue

            # MLD version: 2, host version: 2
            m = p7.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['version'] = \
                    int(m.groupdict()['ver'])
                ret_dict['vrfs'][vrf]['interface'][intf]['host_version'] = \
                    int(m.groupdict()['host_ver'])
                continue

            # MLD query interval: 366 secs, configured value: 366 secs
            m = p8.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['query_interval'] = \
                    int(m.groupdict()['intverval'])
                ret_dict['vrfs'][vrf]['interface'][intf]['configured_query_interval'] = \
                    int(m.groupdict()['conf_intvl'])
                continue

            # MLD max response time: 16 secs, configured value: 16 secs
            m = p9.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['query_max_response_time'] = \
                    int(m.groupdict()['time'])
                ret_dict['vrfs'][vrf]['interface'][intf]['configured_query_max_response_time'] = \
                    int(m.groupdict()['conf_time'])
                continue

            # MLD startup query interval: 91 secs, configured value: 31 secs
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
            m = p11.match(line)
            if m:
                if 'startup_query' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['startup_query'] = {}
                ret_dict['vrfs'][vrf]['interface'][intf]['startup_query']['count'] = \
                    int(m.groupdict()['count'])
                continue

            # MLD last member mrt: 1 secs
            m = p12.match(line)
            if m:
                if 'last_member' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['last_member'] = {}
                ret_dict['vrfs'][vrf]['interface'][intf]['last_member']['mrt'] = \
                    int(m.groupdict()['mrt'])
                continue

            # MLD last member query count: 7
            m = p13.match(line)
            if m:
                if 'last_member' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['last_member'] = {}
                ret_dict['vrfs'][vrf]['interface'][intf]['last_member']['query_count'] = \
                    int(m.groupdict()['count'])
                continue

            # MLD group timeout: 2578 secs, configured value: 260 secs
            m = p14.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['group_timeout'] = \
                    int(m.groupdict()['timeout'])
                ret_dict['vrfs'][vrf]['interface'][intf]['configured_group_timeout'] = \
                    int(m.groupdict()['conf_timeout'])
                continue

            # MLD querier timeout: 2570 secs, configured value: 255 secs
            m = p15.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['querier_timeout'] = \
                    int(m.groupdict()['timeout'])
                ret_dict['vrfs'][vrf]['interface'][intf]['configured_querier_timeout'] = \
                    int(m.groupdict()['conf_timeout'])
                continue

            # MLD unsolicited report interval: 1 secs
            m = p16.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['unsolicited_report_interval'] = \
                    int(m.groupdict()['val'])
                continue

            # MLD robustness variable: 7, configured value: 7
            m = p17.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['robustness_variable'] = \
                    int(m.groupdict()['val1'])
                ret_dict['vrfs'][vrf]['interface'][intf]['configured_robustness_variable'] = \
                    int(m.groupdict()['val2'])
                continue

            # MLD reporting for link-local groups: disabled
            m = p18.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['link_local_groups_reporting'] = True \
                    if 'enable' in m.groupdict()['status'].lower() else False
                continue

            # MLD interface enable refcount: 4
            m = p19.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['enable_refcount'] = \
                    int(m.groupdict()['count'])
                continue

            # MLD immediate leave: enabled
            m = p20.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['immediate_leave'] = True \
                    if 'enable' in m.groupdict()['status'].lower() else False
                continue

            # MLD Report Policy: test
            m = p22.match(line)
            if m:
                if m.groupdict()['policy'] != 'None':
                    ret_dict['vrfs'][vrf]['interface'][intf]['group_policy'] = \
                        m.groupdict()['policy']
                continue

            # MLD State Limit: 6400,  Available States: 6400
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
    exclude = [
        'expire',
        'up_time',
        'last_reporter']

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

        # show ipv6 mld groups
        p0 = re.compile(r'^show +ipv6 +mld +groups.*$')

        # MLD Connected Group Membership for VRF "default" - 2 total entries
        p1 = re.compile(r'^MLD +Connected +Group +Membership +for +VRF +\"(?P<vrf>\S+)\"'
                         ' +\- +(?P<entries>\d+) +total +entries$')

        # ff38::1
        p2 = re.compile(r'^(?P<group>[\w\.\:]+)$')

        # fffe::1            D   Ethernet1/2.10         00:13:56  00:03:31  fe80::200:7cff:fe06:af79
        p3 = re.compile(r'^(?P<group>\w+\:\:\w+) +(?P<type>\w+) +(?P<intf>[\w\.\/\-]+)'
            r' +(?P<uptime>[\w\.\:]+) +(?P<expires>[\w\.\:]+) +(?P<last_reporter>[\w\.\:]+)$')

        #   2001:20:1:1::254 D    Ethernet1/2.10         00:13:56  00:03:31  fe80::200:7cff:fe06:af79
        p4 = re.compile(r'^(?P<source>[\w\.\:]+) +(?P<type>\w+) +(?P<intf>[\w\.\/\-]+)'
            r' +(?P<uptime>[\w\.\:]+) +(?P<expires>[\w\.\:]+) +(?P<last_reporter>[\w\.\:]+)$')

        # (2001:db8:0:abcd::2, ff30::2)
        p5 = re.compile(r'^\((?P<source>[\w\.\:\*]+), *(?P<group>[\w\.\:]+)\)$')

        # Type: Static, Interface: Ethernet2/1
        p6 = re.compile(r'^Type: +(?P<type>\w+), Interface: +(?P<intf>[\w\.\/\-]+)$')

        # Uptime/Expires: 00:26:28/never, Last Reporter: 2001:db8:8404:907f::1
        p7 = re.compile(r'^Uptime\/Expires *: +(?P<uptime>[\w\.\:]+)/(?P<expires>[\w\.\:]+), +'
            r'Last +Reporter *: +(?P<last_reporter>[\w\.\:]+)$')

        # initial variables
        ret_dict = {}
        source = None
        group = None
        sub_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # show ipv6 mld groups
            m = p0.match(line)
            if m:
                continue

            # MLD Connected Group Membership for VRF "default" - 2 total entries
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                groups_count = int(m.groupdict()['entries'])

                ret_dict.setdefault('vrfs', {}).setdefault(vrf, {}).setdefault(
                    'groups_count', groups_count)

                continue

            # ff38::1
            m = p2.match(line)
            if m:
                group = m.groupdict()['group']
                continue

            # fffe::1            D   Ethernet1/2.10         00:13:56  00:03:31  fe80::200:7cff:fe06:af79
            m = p3.match(line)
            if m:
                group = m.groupdict()['group']
                intf = Common.convert_intf_name(m.groupdict()['intf'])

                sub_dict = ret_dict.setdefault('vrfs', {}).setdefault(vrf, {}).setdefault(
                    'interface', {}).setdefault(intf, {}).setdefault('group', {}).setdefault(group, {})

                sub_dict['type'] = m.groupdict()['type'].lower()
                sub_dict['expire'] = m.groupdict()['expires']
                sub_dict['up_time'] = m.groupdict()['uptime']
                sub_dict['last_reporter'] = m.groupdict()['last_reporter']
                continue

            #   2001:20:1:1::254 D    Ethernet1/2.10         00:13:56  00:03:31  fe80::200:7cff:fe06:af79
            m = p4.match(line)
            if m:
                intf = Common.convert_intf_name(m.groupdict()['intf'])
                source = m.groupdict()['source']

                sub_dict = ret_dict.setdefault('vrfs', {}).setdefault(vrf, {}).setdefault(
                    'interface', {}).setdefault(intf, {}).setdefault('group', {}).setdefault(
                    group, {}).setdefault('source', {}).setdefault(source, {})

                sub_dict['type'] = m.groupdict()['type'].lower()
                sub_dict['expire'] = m.groupdict()['expires']
                sub_dict['up_time'] = m.groupdict()['uptime']
                sub_dict['last_reporter'] = m.groupdict()['last_reporter']
                continue

            # (2001:db8:0:abcd::2, ff30::2)
            m = p5.match(line)
            if m:
                group = m.groupdict()['group']
                source = m.groupdict()['source']
                continue

            # Type: Static, Interface: Ethernet2/1
            m = p6.match(line)
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

            # Uptime/Expires: 00:26:28/never, Last Reporter: 2001:db8:8404:907f::1
            m = p7.match(line)
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
    exclude = [
        'last_reported',
        'uptime',
        'oil_uptime',
        'incoming_interface_list']

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

        # Group   Type     Interface   Last Reported
        p0 = re.compile(r'^Group +Type +Interface +Last +Reported$')

        # MLD Locally Joined Group Membership for VRF "default"
        p1 = re.compile(r'^MLD +Locally +Joined +Group +Membership +for +VRF +\"(?P<vrf>\S+)\"$')

        # Group   Type     Interface   Last Reported 
        # (*, fffe::1)
        p2 = re.compile(r'^\((?P<source>[\w\.\:\*]+), *(?P<group>[\w\.\:]+)\)$')

        #         Local    Eth2/1      00:03:07  
        p2_1 = re.compile(r'^(?P<type>\w+) +(?P<intf>[\w\.\-\/]+) +'
                           '(?P<last_reported>[\w\.\:]+)$')

        # Group Address    Source Address   Type     Interface   Last Reported 
        # fffe::2          *                Local    Eth1/2.12   00:27:31  
        p3 = re.compile(r'^(?P<group>[\w\.\:]+) +(?P<source>[\w\.\:\*]+) +'
                           '(?P<type>\w+) +(?P<intf>[\w\.\-\/]+) +(?P<last_reported>[\w\.\:]+)$')

        # initial variables
        ret_dict = {}
        group = None
        source = None

        for line in out.splitlines():
            line = line.strip()

            # Group   Type     Interface   Last Reported
            m = p0.match(line)
            if m:
                continue

            # MLD Locally Joined Group Membership for VRF "default"
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
            m = p2.match(line)
            if m:
                group = m.groupdict()['group']
                source = m.groupdict()['source']
                continue

            #         Local    Eth2/1      00:03:07  
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

            # Group Address    Source Address   Type     Interface   Last Reported 
            # fffe::2          *                Local    Eth1/2.12   00:27:31  
            m = p3.match(line)
            if m:
                group = m.groupdict()['group']
                source = m.groupdict()['source']
                intf = Common.convert_intf_name(m.groupdict()['intf'])
                grp_dict = ret_dict.setdefault('vrfs', {}).setdefault(vrf, {}).setdefault(
                    'interface', {}).setdefault(intf, {}).setdefault('group', {}).setdefault(
                    group, {})
                src_dict = grp_dict.setdefault('source', {}).setdefault(source, {})

                group_type = m.groupdict()['type'].lower()

                grp_dict['last_reported'] = m.groupdict()['last_reported']
                src_dict['last_reported'] = m.groupdict()['last_reported']
                grp_dict['type'] = group_type
                src_dict['type'] = group_type

                # build static_group and join_group info
                if group_type == 'static':
                    key = 'static_group'
                else:
                    key = 'join_group'

                build_group = group + ' ' + source
                build_dict = ret_dict.setdefault('vrfs', {}).setdefault(vrf, {}).setdefault(
                    'interface', {}).setdefault(intf, {}).setdefault(key, {}).setdefault(build_group, {})

                build_dict['group'] = group
                build_dict['source'] = source
                continue

        return ret_dict

