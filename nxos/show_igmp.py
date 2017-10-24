''' show_igmp.py

NXOS parsers for the following show commands:

    * show ip igmp interface
    * show ip igmp interface vrf all
    * show ip igmp interface vrf <WORD>
    * show ip igmp groups
    * show ip igmp groups vrf all
    * show ip igmp groups vrf <WORD>
    * show ip igmp local-groups
    * show ip igmp local-groups vrf all
    * show ip igmp local-groups vrf <WORD>

'''

# Python
import re

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional

# import parser utils
from parser.utils.common import Common

# ==============================================
# Parser for 'show ip igmp interface'
# Parser for 'show ip igmp interface vrf all'
# Parser for 'show ip igmp interface vrf <WORD>'
# ==============================================

class ShowIpIgmpInterfaceSchema(MetaParser):
    # Schema for 'show ip igmp interface'
    # Schema for 'show ip igmp interface vrf all'
    # Schema for 'show ip igmp interface vrf <WORD>'

    schema = {'vrfs': {
                Any(): {
                    'groups_count': int,
                    Optional('interface'): {
                        Any(): {
                            'enable': bool,
                            'link_status': str,
                            'oper_status': str,
                            Optional('address'): str,
                            Optional('subnet'): str,
                            Optional('querier'): str,
                            Optional('querier_version'): int,
                            Optional('next_query_sent_in'): str,
                            Optional('membership_count'): int,
                            Optional('old_membership_count'): int,
                            Optional('version'): int,
                            Optional('host_version'): int,
                            Optional('configured_query_interval'): int,
                            Optional('query_interval'): int,
                            Optional('configured_query_max_response_time'): int,
                            Optional('query_max_response_time'): int,
                            Optional('startup_query'): {
                                Optional('configured_interval'): int,
                                Optional('interval'): int,
                                Optional('count'): int,

                                },
                            Optional('last_member'): {                                
                                Optional('mrt'): int,
                                Optional('query_count'): int,
                            },
                            Optional('configured_group_timeout'): int,
                            Optional('group_timeout'): int,
                            Optional('configured_querier_timeout'): int,
                            Optional('querier_timeout'): int,
                            Optional('unsolicited_report_interval'): int,
                            Optional('configured_robustness_variable'): int,
                            Optional('robustness_variable'): int,
                            Optional('link_local_groups_reporting'): bool,
                            Optional('enable_refcount'): int,
                            Optional('immediate_leave'): bool,
                            Optional('vrf_name'): str,
                            Optional('vrf_id'): int,
                            Optional('group_policy'): str,
                            Optional('max_groups'): int,
                            Optional('available_groups'): int,
                            Optional('statistics'): {
                                Optional('general'): {
                                    'sent' :{
                                        Optional('v2_queries'): int,
                                        Optional('v2_reports'): int,
                                        Optional('v2_leaves'): int,
                                        Optional('v3_queries'): int,
                                        Optional('v3_reports'): int,
                                    },
                                    'received' :{
                                        Optional('v2_queries'): int,
                                        Optional('v2_reports'): int,
                                        Optional('v2_leaves'): int,
                                        Optional('v3_queries'): int,
                                        Optional('v3_reports'): int,
                                    }
                                },
                                Optional('errors'): {
                                    'reason': str,
                                    'router_alert_check': int,
                                }
                            },
                            Optional('pim_dr'): bool,
                            Optional('vpc_svi'): bool,
                        }
                    },
                },
            },
        }

class ShowIpIgmpInterface(ShowIpIgmpInterfaceSchema):
    # Parser for 'show ip igmp interface'
    # Parser for 'show ip igmp interface vrf all'
    # Parser for 'show ip igmp interface vrf <WORD>'

    def cli(self, vrf=''):

        # excute command to get output
        out = self.device.execute('show ip igmp interface' if not vrf else
                                  'show ip igmp interface vrf {}'.format(vrf))

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # IGMP Interfaces for VRF "default", count: 2
            p1 = re.compile(r'^IGMP +Interfaces +for +VRF +\"(?P<vrf>\S+)\", +'
                             'count: +(?P<groups_count>\d+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']

                if 'vrfs' not in ret_dict:
                    ret_dict['vrfs'] = {}
                if vrf not in ret_dict['vrfs']:
                    ret_dict['vrfs'][vrf] = {}

                ret_dict['vrfs'][vrf]['groups_count'] = int(m.groupdict()['groups_count'])
                continue

            # Ethernet2/1, Interface status: protocol-up/link-up/admin-up
            p2 = re.compile(r'^(?P<intf>[\w\/\.\-]+), +'
                             'Interface +status: +protocol\-(?P<protocol_status>\w+)\/'
                             'link\-(?P<link_status>\w+)\/'
                             'admin\-(?P<admin_status>\w+)$')
            m = p2.match(line)
            if m:
                intf = m.groupdict()['intf']

                if 'interface' not in ret_dict['vrfs'][vrf]:
                    ret_dict['vrfs'][vrf]['interface'] = {}

                if intf not in ret_dict['vrfs'][vrf]['interface']:
                    ret_dict['vrfs'][vrf]['interface'][intf] = {}

                ret_dict['vrfs'][vrf]['interface'][intf]['oper_status'] = m.groupdict()['protocol_status']
                ret_dict['vrfs'][vrf]['interface'][intf]['link_status'] = m.groupdict()['link_status']
                ret_dict['vrfs'][vrf]['interface'][intf]['enable'] = True if \
                    m.groupdict()['admin_status'].lower() == 'up' else False
                continue

            # IP address: 10.1.2.1, IP subnet: 10.1.2.0/24
            p3 = re.compile(r'^IP +address: +(?P<ip>[\w\.\:]+), +'
                             'IP +subnet: +(?P<subnet>[\w\.\:\/]+)$')
            m = p3.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['address'] = m.groupdict()['ip']
                ret_dict['vrfs'][vrf]['interface'][intf]['subnet'] = m.groupdict()['subnet']
                continue

            # Active querier: 10.1.2.1, version: 3, next query sent in: 00:00:47
            p4 = re.compile(r'^Active +querier: +(?P<querier>[\w\.\:]+), +'
                             'version: +(?P<version>\d+), +'
                             'next +query +sent +in: +(?P<in>[\w\.\:]+)$')
            m = p4.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['querier'] = m.groupdict()['querier']
                ret_dict['vrfs'][vrf]['interface'][intf]['querier_version'] = int(m.groupdict()['version'])
                ret_dict['vrfs'][vrf]['interface'][intf]['next_query_sent_in'] = m.groupdict()['in']
                continue

            # Membership count: 4
            p5 = re.compile(r'^Membership +count: +(?P<count>\d+)$')
            m = p5.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['membership_count'] = \
                    int(m.groupdict()['count'])
                continue

            # Old Membership count 0
            p6 = re.compile(r'^Old +Membership +count +(?P<count>\d+)$')
            m = p6.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['old_membership_count'] = \
                    int(m.groupdict()['count'])
                continue

            # IGMP version: 3, host version: 3
            p7 = re.compile(r'^IGMP +version: +(?P<ver>\d+), +'
                             'host +version: +(?P<host_ver>\d+)$')
            m = p7.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['version'] = \
                    int(m.groupdict()['ver'])
                ret_dict['vrfs'][vrf]['interface'][intf]['host_version'] = \
                    int(m.groupdict()['host_ver'])
                continue

            # IGMP query interval: 133 secs, configured value: 133 secs
            p8 = re.compile(r'^IGMP +query +interval: +(?P<intverval>\d+) +secs, +'
                             'configured +value: +(?P<conf_intvl>\d+) +secs$')
            m = p8.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['query_interval'] = \
                    int(m.groupdict()['intverval'])
                ret_dict['vrfs'][vrf]['interface'][intf]['configured_query_interval'] = \
                    int(m.groupdict()['conf_intvl'])
                continue

            # IGMP max response time: 15 secs, configured value: 15 secs
            p9 = re.compile(r'^IGMP +max +response +time: +(?P<time>\d+) +secs, +'
                             'configured +value: +(?P<conf_time>\d+) +secs$')
            m = p9.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['query_max_response_time'] = \
                    int(m.groupdict()['time'])
                ret_dict['vrfs'][vrf]['interface'][intf]['configured_query_max_response_time'] = \
                    int(m.groupdict()['conf_time'])
                continue

            # IGMP startup query interval: 33 secs, configured value: 31 secs
            p10 = re.compile(r'^IGMP +startup +query +interval: +(?P<intvl>\d+) +secs, +'
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

            # IGMP startup query count: 5
            p11 = re.compile(r'^IGMP +startup +query +count: +(?P<count>\d+)$')
            m = p11.match(line)
            if m:
                if 'startup_query' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['startup_query'] = {}
                ret_dict['vrfs'][vrf]['interface'][intf]['startup_query']['count'] = \
                    int(m.groupdict()['count'])
                continue

            # IGMP last member mrt: 1 secs
            p12 = re.compile(r'^IGMP +last +member +mrt: +(?P<mrt>\d+) +secs$')
            m = p12.match(line)
            if m:
                if 'last_member' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['last_member'] = {}
                ret_dict['vrfs'][vrf]['interface'][intf]['last_member']['mrt'] = \
                    int(m.groupdict()['mrt'])
                continue

            # IGMP last member query count: 5
            p13 = re.compile(r'^IGMP +last +member +query +count: +(?P<count>\d+)$')
            m = p13.match(line)
            if m:
                if 'last_member' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['last_member'] = {}
                ret_dict['vrfs'][vrf]['interface'][intf]['last_member']['query_count'] = \
                    int(m.groupdict()['count'])
                continue

            # IGMP group timeout: 680 secs, configured value: 260 secs
            p14 = re.compile(r'^IGMP +group +timeout: +(?P<timeout>\d+) +secs, +'
                             'configured +value: +(?P<conf_timeout>\d+) +secs$')
            m = p14.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['group_timeout'] = \
                    int(m.groupdict()['timeout'])
                ret_dict['vrfs'][vrf]['interface'][intf]['configured_group_timeout'] = \
                    int(m.groupdict()['conf_timeout'])
                continue

            # IGMP querier timeout: 672 secs, configured value: 255 secs
            p15 = re.compile(r'^IGMP +querier +timeout: +(?P<timeout>\d+) +secs, +'
                             'configured +value: +(?P<conf_timeout>\d+) +secs$')
            m = p15.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['querier_timeout'] = \
                    int(m.groupdict()['timeout'])
                ret_dict['vrfs'][vrf]['interface'][intf]['configured_querier_timeout'] = \
                    int(m.groupdict()['conf_timeout'])
                continue

            # IGMP unsolicited report interval: 10 secs
            p16 = re.compile(r'^IGMP +unsolicited +report +interval: +(?P<val>\d+) +secs$')
            m = p16.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['unsolicited_report_interval'] = \
                    int(m.groupdict()['val'])
                continue

            # IGMP robustness variable: 5, configured value: 5
            p17 = re.compile(r'^IGMP +robustness +variable: +(?P<val1>\d+), +'
                             'configured +value: +(?P<val2>\d+)$')
            m = p17.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['robustness_variable'] = \
                    int(m.groupdict()['val1'])
                ret_dict['vrfs'][vrf]['interface'][intf]['configured_robustness_variable'] = \
                    int(m.groupdict()['val2'])
                continue

            # IGMP reporting for link-local groups: disabled
            p18 = re.compile(r'^IGMP +reporting +for +link\-local +groups: +(?P<status>\w+)$')
            m = p18.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['link_local_groups_reporting'] = True \
                    if 'enable' in m.groupdict()['status'].lower() else False
                continue

            # IGMP interface enable refcount: 9
            p19 = re.compile(r'^IGMP +interface +enable +refcount: +(?P<count>\d+)$')
            m = p19.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['enable_refcount'] = \
                    int(m.groupdict()['count'])
                continue

            # IGMP interface immediate leave: enabled
            p20 = re.compile(r'^IGMP +interface +immediate +leave: +(?P<status>\w+)$')
            m = p20.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['immediate_leave'] = True \
                    if 'enable' in m.groupdict()['status'].lower() else False
                continue

            # IGMP VRF name default (id 1)
            p21 = re.compile(r'^IGMP +VRF +name +(?P<vrf>\S+) +\(id +(?P<id>\d+)\)$')
            m = p21.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['vrf_name'] = m.groupdict()['vrf']
                ret_dict['vrfs'][vrf]['interface'][intf]['vrf_id'] = int(m.groupdict()['id'])
                continue

            # IGMP Report Policy: access-group-filter
            p22 = re.compile(r'^IGMP +Report +Policy: +(?P<policy>\S+)$')
            m = p22.match(line)
            if m:
                if m.groupdict()['policy'] != 'None':
                    ret_dict['vrfs'][vrf]['interface'][intf]['group_policy'] = \
                        m.groupdict()['policy']
                continue

            # IGMP State Limit: 10,  Available States: 10
            p23 = re.compile(r'^IGMP +State +Limit: +(?P<max_groups>\d+), +'
                              'Available +States: +(?P<available_groups>\d+)$')
            m = p23.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['max_groups'] = \
                    int(m.groupdict()['max_groups'])

                ret_dict['vrfs'][vrf]['interface'][intf]['available_groups'] = \
                    int(m.groupdict()['available_groups'])
                continue

            # IGMP interface statistics: (only non-zero values displayed)
            p24 = re.compile(r'^IGMP +interface +statistics: +(?P<dummy>[\w\-\s\(\)]+)$')
            m = p24.match(line)
            if m:
                if 'statistics' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['statistics'] = {}
                continue

            # General (sent/received):
            #   v2-queries: 5/5, v2-reports: 0/0, v2-leaves: 0/0
            p25 = re.compile(r'^v2\-queries: +(?P<sent1>\d+)\/(?P<received1>\d+), +'
                              'v2\-reports: +(?P<sent2>\d+)\/(?P<received2>\d+), +'
                              'v2\-leaves: +(?P<sent3>\d+)\/(?P<received3>\d+)$')
            m = p25.match(line)
            if m:
                if 'general' not in ret_dict['vrfs'][vrf]['interface'][intf]['statistics']:
                    ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general'] = {}
                if 'sent' not in ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']:
                    ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']['sent'] = {}
                if 'received' not in ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']:
                    ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']['received'] = {}

                ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']['sent']['v2_queries'] = \
                    int(m.groupdict()['sent1'])
                ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']['received']['v2_queries'] = \
                    int(m.groupdict()['received1'])

                ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']['sent']['v2_reports'] = \
                    int(m.groupdict()['sent2'])
                ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']['received']['v2_reports'] = \
                    int(m.groupdict()['received2'])

                ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']['sent']['v2_leaves'] = \
                    int(m.groupdict()['sent3'])
                ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']['received']['v2_leaves'] = \
                    int(m.groupdict()['received3'])
                continue

            #   v3-queries: 11/11, v3-reports: 56/56
            p25_1 = re.compile(r'^v3\-queries: +(?P<sent1>\d+)\/(?P<received1>\d+), +'
                                'v3\-reports: +(?P<sent2>\d+)\/(?P<received2>\d+)$')
            m = p25_1.match(line)
            if m:
                if 'general' not in ret_dict['vrfs'][vrf]['interface'][intf]['statistics']:
                    ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general'] = {}
                if 'sent' not in ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']:
                    ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']['sent'] = {}
                if 'received' not in ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']:
                    ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']['received'] = {}

                ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']['sent']['v3_queries'] = \
                    int(m.groupdict()['sent1'])
                ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']['received']['v3_queries'] = \
                    int(m.groupdict()['received1'])

                ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']['sent']['v3_reports'] = \
                    int(m.groupdict()['sent2'])
                ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['general']['received']['v3_reports'] = \
                    int(m.groupdict()['received2'])
                continue

            # Errors:
            #   Packets dropped due to router-alert check: 19
            p26 = re.compile(r'^Packets +dropped +due +to +(?P<reason>\S+) +check: +(?P<count>\d+)$')
            m = p26.match(line)
            if m:
                if 'errors' not in ret_dict['vrfs'][vrf]['interface'][intf]['statistics']:
                    ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['errors'] = {}

                ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['errors']['reason'] = \
                    m.groupdict()['reason']
                ret_dict['vrfs'][vrf]['interface'][intf]['statistics']['errors']['router_alert_check'] = \
                    int(m.groupdict()['count'])
                continue

            # Interface PIM DR: Yes
            p27 = re.compile(r'^Interface +PIM +DR: +(?P<status>\w+)$')
            m = p27.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['pim_dr'] = True \
                    if 'yes' in m.groupdict()['status'].lower() else False
                continue
                
            # Interface vPC SVI: No
            p28 = re.compile(r'^Interface +vPC +SVI: +(?P<status>\w+)$')
            m = p28.match(line)
            if m:
                ret_dict['vrfs'][vrf]['interface'][intf]['vpc_svi'] = True \
                    if 'no' not in m.groupdict()['status'].lower() else False
                continue
                
            # Interface vPC CFS statistics:

        return ret_dict


# ===========================================
# Parser for 'show ip igmp groups'
# Parser for 'show ip igmp groups vrf all'
# Parser for 'show ip igmp groups vrf <WORD>'
# ===========================================
class ShowIpIgmpGroupsSchema(MetaParser):
    # Schema for 'show ip igmp groups'
    # Schema for 'show ip igmp groups vrf all'
    # Schema for 'show ip igmp groups vrf <WORD>'

    schema = {'vrfs': {
                Any(): {
                    'total_entries': int,
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

class ShowIpIgmpGroups(ShowIpIgmpGroupsSchema):
    # Parser for 'show ip igmp groups'
    # Parser for 'show ip igmp groups vrf all'
    # Parser for 'show ip igmp groups vrf <WORD>'

    def cli(self, vrf=''):

        # excute command to get output
        out = self.device.execute('show ip igmp groups' if not vrf else
                                  'show ip igmp groups vrf {}'.format(vrf))

        # initial variables
        ret_dict = {}
        source_flag = False

        for line in out.splitlines():
            line = line.strip()

            # IGMP Connected Group Membership for VRF "default" - 4 total entries
            p1 = re.compile(r'^IGMP +Connected +Group +Membership +for +VRF +\"(?P<vrf>\S+)\"'
                             ' +\- +(?P<entries>\d+) +total +entries$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']

                if 'vrfs' not in ret_dict:
                    ret_dict['vrfs'] = {}
                if vrf not in ret_dict['vrfs']:
                    ret_dict['vrfs'][vrf] = {}

                ret_dict['vrfs'][vrf]['total_entries'] = int(m.groupdict()['entries'])
                continue

            # 239.7.7.7
            p2 = re.compile(r'^(?P<group>[\w\.\:]+)$')
            m = p2.match(line)
            if m:
                group = m.groupdict()['group']
                source_flag = True
                continue

            # 239.5.5.5          S    Ethernet2/1         00:21:00  never     10.1.2.1
            p3 = re.compile(r'^(?P<group>[\w\.\:]+) +(?P<type>[SDLT]+) +(?P<intf>[\w\.\/\-]+)'
                             ' +(?P<uptime>[\w\.\:]+) +(?P<expires>[\w\.\:]+)'
                             ' +(?P<last_reporter>[\w\.\:]+)$')
            m = p3.match(line)
            if m:
                intf = m.groupdict()['intf']
                if 'interface' not in ret_dict['vrfs'][vrf]:
                    ret_dict['vrfs'][vrf]['interface'] = {}
                if intf not in ret_dict['vrfs'][vrf]['interface']:
                    ret_dict['vrfs'][vrf]['interface'][intf] = {}

                if source_flag:
                    source = m.groupdict()['group']
                else:
                    group = m.groupdict()['group']

                if 'group' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'] = {}
                if group not in ret_dict['vrfs'][vrf]['interface'][intf]['group']:
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group] = {}

                if source_flag:
                    if 'source' not in ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]:
                        ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source'] = {}
                    if source not in ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source']:
                        ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source'][source] = {}

                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source'][source]['expire'] = \
                        m.groupdict()['expires']
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source'][source]['type'] = \
                        m.groupdict()['type']
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source'][source]['up_time'] = \
                        m.groupdict()['uptime']
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source'][source]['last_reporter'] = \
                        m.groupdict()['last_reporter']
                else:
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['expire'] = \
                        m.groupdict()['expires']
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['type'] = \
                        m.groupdict()['type']
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['up_time'] = \
                        m.groupdict()['uptime']
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['last_reporter'] = \
                        m.groupdict()['last_reporter']

                source_flag = False

                continue

        return ret_dict


# ===========================================
# Parser for 'show ip igmp local-groups'
# Parser for 'show ip igmp local-groups vrf all'
# Parser for 'show ip igmp local-groups vrf <WORD>'
# ===========================================
class ShowIpIgmpLocalGroupsSchema(MetaParser):
    # Schema for 'show ip igmp local-groups'
    # Schema for 'show ip igmp local-groups vrf all'
    # Schema for 'show ip igmp local-groups vrf <WORD>'

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
                                            'last_reporter':str,
                                            'type': str,
                                        }
                                    },
                                    Optional('last_reporter'): str,
                                    Optional('type'): str,
                                }
                            }
                        },
                    },
                },
            }
        }

class ShowIpIgmpLocalGroups(ShowIpIgmpLocalGroupsSchema):
    # Parser for 'show ip igmp local-groups'
    # Parser for 'show ip igmp local-groups vrf all'
    # Parser for 'show ip igmp local-groups vrf <WORD>'

    def cli(self, vrf=''):

        # excute command to get output
        out = self.device.execute('show ip igmp local-groups' if not vrf else
                                  'show ip igmp local-groups vrf {}'.format(vrf))

        # initial variables
        ret_dict = {}
        source_flag = False

        for line in out.splitlines():
            line = line.strip()

            # IGMP Locally Joined Group Membership for VRF "default"
            p1 = re.compile(r'^IGMP +Locally +Joined +Group +Membership +for +VRF +\"(?P<vrf>\S+)\"$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']

                if 'vrfs' not in ret_dict:
                    ret_dict['vrfs'] = {}
                if vrf not in ret_dict['vrfs']:
                    ret_dict['vrfs'][vrf] = {}
                continue

            # 239.1.1.1        *                Local    Eth2/4      00:00:50
            # 239.7.7.7        2.2.2.1          Static   Eth2/4      01:06:47
            p2 = re.compile(r'^(?P<group>[\w\.\:]+) +(?P<source>[\w\.\:\*]+) +'
                             '(?P<type>\w+) +(?P<intf>[\w\.\/\-]+)'
                             ' +(?P<last_reporter>[\w\.\:]+)$')
            m = p2.match(line)
            if m:
                intf = Common.convert_intf_name(m.groupdict()['intf'])
                if 'interface' not in ret_dict['vrfs'][vrf]:
                    ret_dict['vrfs'][vrf]['interface'] = {}
                if intf not in ret_dict['vrfs'][vrf]['interface']:
                    ret_dict['vrfs'][vrf]['interface'][intf] = {}

                group = m.groupdict()['group']
                if 'group' not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'] = {}
                if group not in ret_dict['vrfs'][vrf]['interface'][intf]['group']:
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group] = {}

                group_type = m.groupdict()['type'].lower()


                source = m.groupdict()['source']
                if source != '*':
                    if 'source' not in ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]:
                        ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source'] = {}
                    if source not in ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source']:
                        ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['source'][source] = {}

                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]\
                        ['source'][source]['type'] = group_type
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]\
                        ['source'][source]['last_reporter'] = m.groupdict()['last_reporter']
                else:
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['type'] = group_type                    
                    ret_dict['vrfs'][vrf]['interface'][intf]['group'][group]['last_reporter'] = \
                        m.groupdict()['last_reporter']

                # build static_group and join_group info
                if group_type == 'static':
                    key = 'static_group'
                else:
                    key = 'join_group'
                if key not in ret_dict['vrfs'][vrf]['interface'][intf]:
                    ret_dict['vrfs'][vrf]['interface'][intf][key] = {}
                build_group = group + ' ' + source
                if build_group not in ret_dict['vrfs'][vrf]['interface'][intf][key]:
                    ret_dict['vrfs'][vrf]['interface'][intf][key][build_group] = {}
                ret_dict['vrfs'][vrf]['interface'][intf][key][build_group]['group'] = group
                ret_dict['vrfs'][vrf]['interface'][intf][key][build_group]['source'] = source
                continue

        return ret_dict

