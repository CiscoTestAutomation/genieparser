'''
show_mld.py

IOSXR parsers for the following show commands:
    * show mld summary internal
    * show mld vrf {vrf} summary internal

    * show mld interface
    * show mld vrf {vrf} interface
    
    * show mld ssm map detail
    * show mld vrf {vrf} ssm map detail
    
    * show mld groups detail
    * show mld vrf {vrf} groups detail
    * show mld groups {group} detail
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# ==============================================================================
# Schema for 'show mld summary internal', 'show mld vrf {vrf} summary internal' (1 and 2)
# ==============================================================================

class ShowMldSummaryInternalSchema(MetaParser):
    '''
    Schema for:
    show mld summary internal
    show mld vrf {vrf} summary internal
    '''

    schema = {
        'vrf': {
            Any(): {
                Optional('robustness_value'): int, # Robustness Value 10
                Optional('num_groups_x_intf'): int, # No. of Group x Interfaces 13
                Optional('max_num_groups_x_intfs'): int, 
                # Maximum number of Group x Interfaces 75000
                Optional('supported_intf'): int, # Supported Interfaces   : 1
                Optional('unsupported_intf'): int, # Unsupported Interfaces : 0
                Optional('enabled_intf'): int, # Enabled Interfaces     : 1
                Optional('disabled_intf'): int, # Disabled Interfaces    : 0
                Optional('mte_tuple_count'): int, # MTE tuple count        : 0
                Optional('interface'): {
                    # Interface: GigabitEthernet0/0/0/0
                    Any(): {
                        'num_groups': int, # Number Groups: 13
                        'max_groups': int, # Max # Groups: 6400
                        'on': bool, # On: Y 
                        'parent': str, # Parent: 0x0
                        'last_query': str, # Last query: 00:29:26
                        'last_report': str, # Last Report: 00:04:16
                        'igmp_r_uptime': str, # IGMP R Uptime: 1d06h
                    },
                },
            },
        },
    }



# ==============================================================================
# Parser for 'show mld summary internal', 'show mld vrf {vrf} summary internal' (1 and 2)
# ==============================================================================

class ShowMldSummaryInternal(ShowMldSummaryInternalSchema):
    '''
    Parser for:
    show mld summary internal
    show mld vrf {vrf} summary internal
    '''

    cli_command = ['show mld vrf {vrf} summary internal','show mld summary internal']

    def cli(self, vrf = '', output = None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf = vrf)
            else:
                vrf = 'default'
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables
        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Robustness Value 10
            p1 = re.compile(r'^Robustness +Value +(?P<robustness_value>\d+)$')
            m = p1.match(line)
            if m:
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf] = {}

                parsed_dict['vrf'][vrf]['robustness_value'] = \
                    int(m.groupdict()['robustness_value'])
                continue

            # No. of Group x Interfaces 13
            p2 = re.compile(r'^No\. +of +Group +x +Interfaces +(?P<num_groups_x_intf>\d+)$')
            m = p2.match(line)
            if m:
                parsed_dict['vrf'][vrf]['num_groups_x_intf'] = \
                int(m.groupdict()['num_groups_x_intf'])
                continue

            # Maximum number of Group x Interfaces 75000
            p3 = re.compile(r'^Maximum +number +of +Group +x +Interfaces +'
                '(?P<max_num_groups_x_intfs>\d+)$')
            m = p3.match(line)
            if m:
                parsed_dict['vrf'][vrf]['max_num_groups_x_intfs'] = \
                int(m.groupdict()['max_num_groups_x_intfs'])
                continue

            # Supported Interfaces   : 1
            p4 = re.compile(r'^Supported +Interfaces +: +(?P<supported_intf>\d+)$')
            m = p4.match(line)
            if m:
                parsed_dict['vrf'][vrf]['supported_intf'] = \
                int(m.groupdict()['supported_intf'])
                continue

            # Unsupported Interfaces : 0
            p5 = re.compile(r'^Unsupported +Interfaces +: +(?P<unsupported_intf>\d+)$')
            m = p5.match(line)
            if m:
                parsed_dict['vrf'][vrf]['unsupported_intf'] = \
                int(m.groupdict()['unsupported_intf'])
                continue

            # Enabled Interfaces     : 1
            p6 = re.compile(r'^Enabled +Interfaces +: +(?P<enabled_intf>\d+)$')
            m = p6.match(line)
            if m:
                parsed_dict['vrf'][vrf]['enabled_intf'] = \
                int(m.groupdict()['enabled_intf'])
                continue

            # Disabled Interfaces    : 0
            p7 = re.compile(r'^Disabled +Interfaces +: +(?P<disabled_intf>\d+)$')
            m = p7.match(line)
            if m:
                parsed_dict['vrf'][vrf]['disabled_intf'] = \
                int(m.groupdict()['disabled_intf'])
                continue

            # MTE tuple count        : 0
            p8 = re.compile(r'^MTE +tuple +count +: +(?P<mte_tuple_count>\d+)$')
            m = p8.match(line)
            if m:
                parsed_dict['vrf'][vrf]['mte_tuple_count'] = \
                int(m.groupdict()['mte_tuple_count'])
                continue

            # Interface                       Number  Max #   On Parent     Last     Last     IGMP R
            p9_1 = re.compile(r'^Interface +Number +Max +# +On +Parent +Last +Last +IGMP +R$')
            m = p9_1.match(line)
            if m:
                continue
            #                                 Groups  Groups                query    Report   Uptime
            p9_2 = re.compile(r'^\s|\sGroups +Groups +query +Report +Uptime$')
            m = p9_2.match(line)
            if m:
                continue

            # GigabitEthernet0/0/0/0          13      6400    Y  0x0        00:29:26 00:04:16    1d06h
            p9 = re.compile(r'^(?P<interface>[\w\-\.\/]+) +'
                             '(?P<num_groups>\d+) +'
                             '(?P<max_groups>\d+) +'
                             '(?P<on>\w+) +'
                             '(?P<parent>[\w]+) +'
                             '(?P<last_query>[\w\:]+) +'
                             '(?P<last_report>[\w\:]+) +'
                             '(?P<igmp_r_uptime>[\w\:]+)$')
            m = p9.match(line)
            if m:
                interface = m.groupdict()['interface']

                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf] = {}
                
                if 'interface' not in parsed_dict['vrf'][vrf]:
                    parsed_dict['vrf'][vrf]['interface'] = {}
                if interface not in parsed_dict['vrf'][vrf]['interface']:
                    parsed_dict['vrf'][vrf]['interface'][interface] = {}
                
                parsed_dict['vrf'][vrf]['interface'][interface]['num_groups'] = \
                    int(m.groupdict()['num_groups'])

                parsed_dict['vrf'][vrf]['interface'][interface]['max_groups'] = \
                    int(m.groupdict()['max_groups'])

                parsed_dict['vrf'][vrf]['interface'][interface]['on'] = True \
                    if m.groupdict()['on'].lower() == 'y' else False

                parsed_dict['vrf'][vrf]['interface'][interface]['parent'] = \
                    m.groupdict()['parent']

                parsed_dict['vrf'][vrf]['interface'][interface]['last_query'] = \
                    m.groupdict()['last_query']

                parsed_dict['vrf'][vrf]['interface'][interface]['last_report'] = \
                    m.groupdict()['last_report']

                parsed_dict['vrf'][vrf]['interface'][interface]['igmp_r_uptime'] = \
                    m.groupdict()['igmp_r_uptime']

        return parsed_dict


# ==============================================================================
# Schema for 'show mld interface', 'show mld vrf {vrf} interface' (3 and 4)
# ==============================================================================
class ShowMldInterfaceSchema(MetaParser):
    '''
    Schema for:
    show mld interface
    show mld vrf {vrf} interface
    '''
    schema = {
        'vrf': {
            Any(): {
                Optional('max_groups'): int,
                Optional('active_groups'): int,
                'interface': {
                    Any(): {
                        'oper_status': str, # line protocol is up
                        'interface_status': str, # GigabitEthernet0/0/0/0 is up
                        Optional('internet_address'): str,  
                        # Internet address is fe80::5054:ff:fefa:9ad7
                        'enable': bool, # MLD is enabled on interface
                        Optional('version'): int, # Current MLD version is 2
                        Optional('query_interval'): int, 
                        # MLD query interval is 366 seconds
                        Optional('querier_timeout'): int, 
                        # MLD querier timeout is 3666 seconds
                        Optional('query_max_response_time'): int, 
                        # MLD max query response time is 12 seconds
                        Optional('last_member_query_interval'): int, 
                        # Last member query response interval is 1 seconds
                        Optional('max_groups'): int,
                        Optional('active_groups'): int,
                        Optional('counters'): {
                            'joins': int, # MLD activity: 18 joins, 5 leaves
                            'leaves': int,
                        },
                        Optional('querier'): str, 
                        # MLD querying router is fe80::5054:ff:fed7:c01f
                        Optional('time_elapsed_since_last_query_sent'): str, 
                        # Time elapsed since last query sent 00:30:16
                        Optional('time_elapsed_since_igmp_router_enabled'): str,
                        # Time elapsed since IGMP router enabled 1d06h
                        Optional('time_elapsed_since_last_report_received'): str,
                        # Time elapsed since last report received 00:05:05
                    },
                }
            }
        },
    }

# ==============================================================================
# Parser for 'show mld interface', 'show mld vrf {vrf} interface' (3 and 4)
# ==============================================================================
class ShowMldInterface(ShowMldInterfaceSchema):
    '''
    Parser for:
    show mld interface
    show mld vrf {vrf} interface
    '''

    cli_command = ['show mld vrf {vrf} interface','show mld interface']

    def cli(self, vrf = '', output = None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf = vrf)
            else:
                vrf = 'default'
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables
        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet0/0/0/0 is up, line protocol is up
            p1 = re.compile(r'^(?P<intf>[\w\-\.\/]+) +is +(?P<intf_status>[\w\s]+), +'
                             'line +protocol +is +(?P<oper_status>\w+)$')
            m = p1.match(line)
            if m:
                intf = m.groupdict()['intf']
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf] = {}

                if 'interface' not in parsed_dict['vrf'][vrf]:
                    parsed_dict['vrf'][vrf]['interface'] = {}
                if intf not in parsed_dict['vrf'][vrf]['interface']:
                    parsed_dict['vrf'][vrf]['interface'][intf] = {}

                parsed_dict['vrf'][vrf]['interface'][intf]['oper_status'] = \
                    m.groupdict()['oper_status'].lower()
                parsed_dict['vrf'][vrf]['interface'][intf]['interface_status'] = \
                    m.groupdict()['intf_status'].lower()
                continue

            # Internet address is fe80::5054:ff:fefa:9ad7
            p2 = re.compile(r'^Internet +address +is +(?P<ip>[\w\/\.\:]+)$')
            m = p2.match(line)
            if m:                
                parsed_dict['vrf'][vrf]['interface'][intf]['internet_address'] = \
                    m.groupdict()['ip']
                continue

            # MLD is enabled on interface
            p3 = re.compile(r'^MLD +is +(?P<status>\w+) +on +interface$')
            m = p3.match(line)
            if m:
                status = m.groupdict()['status'].lower()
                parsed_dict['vrf'][vrf]['interface'][intf]['enable'] = True if \
                    'enable' in status else False
                continue

            # Current MLD version is 2
            p4 = re.compile(r'^Current +MLD +version +is +(?P<ver>\d+)$')
            m = p4.match(line)
            if m:                
                parsed_dict['vrf'][vrf]['interface'][intf]['version'] = \
                    int(m.groupdict()['ver'])
                continue

            # MLD query interval is 366 seconds
            p5 = re.compile(r'^MLD +query +interval +is +(?P<query_interval>\d+) +seconds$')
            m = p5.match(line)
            if m:                
                parsed_dict['vrf'][vrf]['interface'][intf]['query_interval'] = \
                    int(m.groupdict()['query_interval'])
                continue

            # MLD querier timeout is 3666 seconds
            p6 = re.compile(r'^MLD +querier +timeout +is +'
                             '(?P<timeout>\d+) +seconds$')
            m = p6.match(line)
            if m:                
                parsed_dict['vrf'][vrf]['interface'][intf]['querier_timeout'] = \
                    int(m.groupdict()['timeout'])
                continue

            # MLD max query response time is 12 seconds
            p7 = re.compile(r'^MLD +max +query +response +time +is +'
                             '(?P<time>\d+) +seconds$')
            m = p7.match(line)
            if m:                
                parsed_dict['vrf'][vrf]['interface'][intf]['query_max_response_time'] = \
                    int(m.groupdict()['time'])
                continue

            # Last member query response interval is 1 seconds
            p8 = re.compile(r'^Last +member +query +response +interval +is '
                              '+(?P<time>\d+) +(seconds|ms)$')
            m = p8.match(line)
            if m:                
                parsed_dict['vrf'][vrf]['interface'][intf]['last_member_query_interval'] = \
                    int(m.groupdict()['time'])
                continue

            # MLD activity: 18 joins, 5 leaves
            p9 = re.compile(r'^MLD +activity: +(?P<joins>\d+) +joins, +(?P<leaves>\d+) +leaves$')
            m = p9.match(line)
            if m:
                if 'counters' not in parsed_dict['vrf'][vrf]['interface'][intf]:
                    parsed_dict['vrf'][vrf]['interface'][intf]['counters'] = {}
                parsed_dict['vrf'][vrf]['interface'][intf]['counters']['joins'] = \
                    int(m.groupdict()['joins'])
                parsed_dict['vrf'][vrf]['interface'][intf]['counters']['leaves'] = \
                    int(m.groupdict()['leaves'])
                continue

            # MLD querying router is FE80::5054:FF:FE7C:DC70
            p10 = re.compile(r'^MLD +querying +router +is +(?P<querier>[\w\.\:]+)$')
            m = p10.match(line)
            if m:
                parsed_dict['vrf'][vrf]['interface'][intf]['querier'] = \
                    m.groupdict()['querier']
                continue

            # Time elapsed since last query sent 00:30:16
            p11 = re.compile(r'^Time +elapsed +since +last +query +sent +'
                '(?P<time_elapsed_since_last_query_sent>[\w\:]+)$')
            m = p11.match(line)
            if m:
                parsed_dict['vrf'][vrf]['interface'][intf]['time_elapsed_since_last_query_sent'] = \
                    m.groupdict()['time_elapsed_since_last_query_sent']
                continue

            # Time elapsed since IGMP router enabled 1d06h
            p12 = re.compile(r'^Time +elapsed +since +IGMP +router +enabled +'
                '(?P<time_elapsed_since_igmp_router_enabled>[\w\:]+)$')
            m = p12.match(line)
            if m:
                parsed_dict['vrf'][vrf]['interface'][intf]['time_elapsed_since_igmp_router_enabled'] = \
                    m.groupdict()['time_elapsed_since_igmp_router_enabled']
                continue

            # Time elapsed since last report received 00:00:51
            p13 = re.compile(r'^Time +elapsed +since +last +report +received +'
                '(?P<time_elapsed_since_last_report_received>[\w\:]+)$')
            m = p13.match(line)
            if m:
                parsed_dict['vrf'][vrf]['interface'][intf]['time_elapsed_since_last_report_received'] = \
                    m.groupdict()['time_elapsed_since_last_report_received']
                continue

        return parsed_dict

"""
# ==============================================================================
# Schema for 'show mld ssm map detail', 'show mld vrf {vrf} ssm map detail' (5 and 6)
# ==============================================================================

class ShowMldSsmMapDetailSchema(MetaParser):
    '''
    Schema for:
    show mld ssm map detail
    show mld vrf {vrf} ssm map detail
    '''

    # TODO






# ==============================================================================
# Parser for 'show mld ssm map detail', 'show mld vrf {vrf} ssm map detail' (5 and 6)
# ==============================================================================

class ShowMldSsmMapDetail(ShowMldSsmMapDetailSchema):
    '''
    Parser for:
    show mld ssm map detail
    show mld vrf {vrf} ssm map detail
    '''

    # TODO
"""







# ==============================================================================
# Schema for 'show mld groups detail', 'show mld vrf {vrf} groups detail', 
#            'show mld groups {group} detail' (7, 8, 9)
# ==============================================================================

class ShowMldGroupsDetailSchema(MetaParser):
    '''
    Schema for:
    show mld groups detail
    show mld vrf {vrf} groups detail
    show mld groups {group} detail
    '''

    schema = {
        'vrf': {
            Any(): {
                'interface': { # Interface: GigabitEthernet0/0/0/0
                    Any(): {
                        Optional('join_group'): {
                            Any(): {
                                'group': str,
                                'source': str,
                            }
                        },
                        Optional('static_group'): {
                            Any(): {
                                'group': str,
                                'source': str,
                            }
                        },
                        'group': { # Group: ff15:1::1
                            Any(): {
                                'up_time': str, # Uptime: 08:06:00
                                'router_mode': str, 
                                # Router mode: INCLUDE,or
                                # Router mode: EXCLUDE (Expires: 00:29:15)
                                'host_mode': str, # Host mode: INCLUDE
                                'last_reporter': str, 
                                # Last reporter: fe80::5054:ff:fefa:9ad7
                                Optional('suppress'): int, # Suppress:       0
                                Optional('expire'): str,
                                Optional('source'): {
                                    # Source Address: 2001:db8:2:2::2
                                    Any(): {
                                        Optional('expire'): str, 
                                        # Expires: 01:00:00
                                        'forward': bool, # Fwd: Yes
                                        Optional('flags'): str, 
                                        # Flags: Remote Local 2d
                                        'up_time': str, # Uptime: 08:06:00
                                    },
                                },
                            }
                        },
                    }
                }
            },
        }
    }

# ==============================================================================
# Parser for 'show mld groups detail', 'show mld vrf {vrf} groups detail' (7 and 8)
# ==============================================================================
class ShowMldGroupsDetail(ShowMldGroupsDetailSchema):
    '''
    Parser for:
    show mld groups detail
    show mld vrf {vrf} groups detail
    '''

    cli_command = ['show mld vrf {vrf} groups detail', 'show mld groups detail']

    def cli(self, vrf = '', output = None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf = vrf)
            else:
                vrf = 'default'
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            vrf = 'default' ###### not completely sure
            out = output

        # initial variables
        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Interface:\tGigabitEthernet0/0/0/0
            line = line.replace('\t', '    ')

            # Interface:      GigabitEthernet0/0/0/0
            p1 = re.compile(r'^Interface: +(?P<intf>[\w\.\-\/]+)$')
            m = p1.match(line)
            if m:
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf] = {}

                intf = m.groupdict()['intf']
                if 'interface' not in parsed_dict['vrf'][vrf]:
                    parsed_dict['vrf'][vrf]['interface'] = {}
                if intf not in parsed_dict['vrf'][vrf]['interface']:
                    parsed_dict['vrf'][vrf]['interface'][intf] = {}
                continue

            # Group:          ff15:1::1
            p2 = re.compile(r'^Group: +(?P<group>[\w\.\:]+)$')
            m = p2.match(line)
            if m:
                group = m.groupdict()['group']
                if 'group' not in parsed_dict['vrf'][vrf]['interface'][intf]:
                    parsed_dict['vrf'][vrf]['interface'][intf]['group'] = {}
                if group not in parsed_dict['vrf'][vrf]['interface'][intf]['group']:
                    parsed_dict['vrf'][vrf]['interface'][intf]['group'][group] = {}
                continue

            # Host mode:      INCLUDE
            p3 = re.compile(r'^Host +mode: +(?P<host_mode>\w+)$')
            m = p3.match(line)
            if m:
                host_mode = m.groupdict()['host_mode']
                parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]['host_mode'] = host_mode.lower()
                continue

            # Uptime:         08:06:00
            p4 = re.compile(r'^Uptime: +(?P<up_time>[\w\:\.]+)$')
            m = p4.match(line)
            if m:
                up_time = m.groupdict()['up_time']
                parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]['up_time'] = up_time
                continue

            # Router mode:    INCLUDE
            # Router mode:    EXCLUDE (Expires: 00:29:15)
            p5 = re.compile(r'^Router +mode: +(?P<router_mode>\w+)'
                             '( *\(Expires: +(?P<expire>[\w\.\:]+)\))?$')
            m = p5.match(line)
            if m:
                router_mode = m.groupdict()['router_mode']
                expire = m.groupdict()['expire']
                parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]['router_mode'] = router_mode.lower()
                if expire:
                    parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]['expire'] = expire
                continue

            # Last reporter:  fe80::5054:ff:fefa:9ad7
            p6 = re.compile(r'^Last +reporter: +(?P<last_reporter>[\w\.\:]+)$')
            m = p6.match(line)
            if m:
                last_reporter = m.groupdict()['last_reporter']
                parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]['last_reporter'] = last_reporter
                continue

            # Suppress:       0
            p7 = re.compile(r'^Suppress: +(?P<suppress>(\d+))$')
            m = p7.match(line)
            if m:
                suppress = int(m.groupdict()['suppress'])
                parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]['suppress'] = suppress
                continue

            # Source Address                          Uptime    Expires   Fwd  Flags
            p8_1 = re.compile(r'^Source +Address +Uptime +Expires +Fwd +Flags$')
            m = p8_1.match(line)
            if m:
                continue

            # 2001:db8:2:2::2                       08:06:00  01:00:00  Yes  Remote Local 2d
            p8 = re.compile(r'^(?P<source>[\w\.\:]+) +'
                             '(?P<up_time>[\w\.\:]+) +'
                             '(?P<expire>[\w\.\:]+) +'
                             '(?P<forward>\w+) +'
                             '(?P<flags>[\w\s]+)$')
            m = p8.match(line)
            if m:
                source = m.groupdict()['source']
                flags = m.groupdict()['flags']


                # group structure
                if 'source' not in parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]:
                    parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]['source'] = {}
                if source not in parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]['source']:
                    parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]['source'][source] = {}

                parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]\
                    ['source'][source]['up_time'] = m.groupdict()['up_time']

                parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]\
                    ['source'][source]['expire'] = m.groupdict()['expire']

                parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]\
                    ['source'][source]['forward'] = True \
                        if m.groupdict()['forward'].lower() == 'yes' else False

                parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]\
                    ['source'][source]['flags'] = flags

                flag_list = flags.lower().split()
                if ('4' in flag_list or '2d' in flag_list) and 'e' in flag_list:
                    keys = ['join_group', 'static_group']
                elif '4' in flag_list or '2d' in flag_list or '29' in flag_list:
                    keys = ['join_group']
                elif 'e' in flag_list or 'a' in flag_list:
                    keys = ['static_group']
                else:
                    keys = []

                # join_group or static_group structure
                if keys:
                    static_join_group = group + ' ' + source
                    for key in keys:
                        if key not in parsed_dict['vrf'][vrf]['interface'][intf]:
                            parsed_dict['vrf'][vrf]['interface'][intf][key] = {}

                        if static_join_group not in parsed_dict['vrf'][vrf]['interface'][intf][key]:
                            parsed_dict['vrf'][vrf]['interface'][intf][key][static_join_group] = {}

                        parsed_dict['vrf'][vrf]['interface'][intf][key][static_join_group]['group'] = group
                        parsed_dict['vrf'][vrf]['interface'][intf][key][static_join_group]['source'] = source

        return parsed_dict


# ==============================================================================
# Parser for 'show mld groups {group} detail' (9)
# ==============================================================================
class ShowMldGroupsVrfDetail(ShowMldGroupsDetail):
    ''' 
    Parser for:
    show mld groups {group} detail
    '''
    cli_command = 'show mld groups {group} detail'

    def cli(self, group = '', output = None):
        if output is None:
            if group:
                out = self.device.execute(self.cli_command.format(group = group))
            else:
                out = self.device.execute(self.cli_command.format(group = 'default'))
        else:
            out = output
    
        return super().cli(output = out)
