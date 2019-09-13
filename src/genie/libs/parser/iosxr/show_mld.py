'''
show_mld.py

IOSXR parsers for the following show commands:
    * show mld summary internal
    * show mld vrf {vrf} summary internal

    * show mld interface
    * show mld vrf {vrf} interface
    
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
# Schema for 
#    * 'show mld summary internal'
#    * 'show mld vrf {vrf} summary internal'
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
                Optional('robustness_value'): int,
                Optional('num_groups_x_intf'): int,
                Optional('max_num_groups_x_intfs'): int,
                Optional('supported_intf'): int,
                Optional('unsupported_intf'): int,
                Optional('enabled_intf'): int,
                Optional('disabled_intf'): int,
                Optional('mte_tuple_count'): int,
                Optional('interface'): {
                    Any(): {
                        'num_groups': int,
                        'max_groups': int,
                        'on': bool, 
                        'parent': str,
                        'last_query': str,
                        'last_report': str,
                        'igmp_r_uptime': str,
                    },
                },
            },
        },
    }



# ==============================================================================
# Parser for 
#    * 'show mld summary internal'
#    * 'show mld vrf {vrf} summary internal'
# ==============================================================================

class ShowMldSummaryInternal(ShowMldSummaryInternalSchema):
    '''
    Parser for:
    show mld summary internal
    show mld vrf {vrf} summary internal
    '''

    cli_command = ['show mld vrf {vrf} summary internal','show mld summary internal']
    exclude = ['last_query' ,'last_report', 'last_reporter', 'expire']

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

        # regex

        # Robustness Value 10
        p1 = re.compile(r'^Robustness +Value +(?P<robustness_value>\d+)$')
        
        # No. of Group x Interfaces 13
        p2 = re.compile(r'^No\. +of +Group +x +Interfaces +(?P<num_groups_x_intf>\d+)$')
        
        # Maximum number of Group x Interfaces 75000
        p3 = re.compile(r'^Maximum +number +of +Group +x +Interfaces +'
            			 '(?P<max_num_groups_x_intfs>\d+)$')
        
        # Supported Interfaces   : 1
        p4 = re.compile(r'^Supported +Interfaces +: +(?P<supported_intf>\d+)$')
        
        # Unsupported Interfaces : 0
        p5 = re.compile(r'^Unsupported +Interfaces +: +(?P<unsupported_intf>\d+)$')
        
        # Enabled Interfaces     : 1
        p6 = re.compile(r'^Enabled +Interfaces +: +(?P<enabled_intf>\d+)$')
        
        # Disabled Interfaces    : 0
        p7 = re.compile(r'^Disabled +Interfaces +: +(?P<disabled_intf>\d+)$')
        
        # MTE tuple count        : 0
        p8 = re.compile(r'^MTE +tuple +count +: +(?P<mte_tuple_count>\d+)$')
        
        # Interface                       Number  Max #   On Parent     Last     Last     IGMP R
        p9_1 = re.compile(r'^Interface +Number +Max +# +On +Parent +Last +Last +IGMP +R$')
        
        #                                 Groups  Groups                query    Report   Uptime
        p9_2 = re.compile(r'^\s|\sGroups +Groups +query +Report +Uptime$')
        
        # GigabitEthernet0/0/0/0          13      6400    Y  0x0        00:29:26 00:04:16    1d06h
        p9 = re.compile(r'^(?P<interface>[\w\-\.\/]+) +'
                         '(?P<num_groups>\d+) +'
                         '(?P<max_groups>\d+) +'
                         '(?P<on>\w+) +'
                         '(?P<parent>[\w]+) +'
                         '(?P<last_query>[\w\:]+) +'
                         '(?P<last_report>[\w\:]+) +'
                         '(?P<igmp_r_uptime>[\w\:]+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                if vrf:
                    vrf = vrf
                else:
                    vrf = 'default'
                vrf_dict = parsed_dict.setdefault('vrf', {}).\
                                       setdefault(vrf, {})
                vrf_dict['robustness_value'] = int(group['robustness_value'])
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['num_groups_x_intf'] = int(group['num_groups_x_intf'])
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['max_num_groups_x_intfs'] = int(group['max_num_groups_x_intfs'])
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['supported_intf'] = int(group['supported_intf'])
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['unsupported_intf'] = int(group['unsupported_intf'])
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['enabled_intf'] = int(group['enabled_intf'])
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['disabled_intf'] = int(group['disabled_intf'])
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['mte_tuple_count'] = int(group['mte_tuple_count'])
                continue

            m = p9_1.match(line)
            if m:
                continue

            m = p9_2.match(line)
            if m:
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                if vrf:
                    vrf = vrf
                else:
                    vrf = 'default'
                vrf_dict = parsed_dict.setdefault('vrf', {}).\
                                       setdefault(vrf, {})

                if 'interface' not in parsed_dict['vrf'][vrf]:
                    interface_dict = vrf_dict.setdefault('interface', {})
                if interface not in parsed_dict['vrf'][vrf]['interface']:
                    interface_dict = vrf_dict.setdefault('interface', {}).\
                                              setdefault(interface, {})

                interface_dict['num_groups'] = int(group['num_groups'])
                interface_dict['max_groups'] = int(group['max_groups'])
                interface_dict['on'] = True if group['on'].lower() == 'y' else False
                interface_dict['parent'] = group['parent']
                interface_dict['last_query'] = group['last_query']
                interface_dict['last_report'] = group['last_report']
                interface_dict['igmp_r_uptime'] = group['igmp_r_uptime']

        return parsed_dict


# ==============================================================================
# Schema for 
#    * 'show mld interface'
#    * 'show mld vrf {vrf} interface'
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
                        'oper_status': str,
                        'interface_status': str,
                        Optional('internet_address'): str,
                        'enable': bool,
                        Optional('version'): int,
                        Optional('query_interval'): int,
                        Optional('querier_timeout'): int,
                        Optional('query_max_response_time'): int,
                        Optional('last_member_query_interval'): int,
                        Optional('max_groups'): int,
                        Optional('active_groups'): int,
                        Optional('counters'): {
                            'joins': int,
                            'leaves': int,
                        },
                        Optional('querier'): str,
                        Optional('time_elapsed_since_last_query_sent'): str,
                        Optional('time_elapsed_since_igmp_router_enabled'): str,
                        Optional('time_elapsed_since_last_report_received'): str,
                    },
                }
            }
        },
    }

# ==============================================================================
# Parser for 
#    * 'show mld interface'
#    * 'show mld vrf {vrf} interface'
# ==============================================================================
class ShowMldInterface(ShowMldInterfaceSchema):
    '''
    Parser for:
    show mld interface
    show mld vrf {vrf} interface
    '''

    cli_command = ['show mld vrf {vrf} interface','show mld interface']
    exclude = ['time_elapsed_since_last_query_sent' , 'time_elapsed_since_last_report_received']

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

    	# regex

    	# GigabitEthernet0/0/0/0 is up, line protocol is up
        p1 = re.compile(r'^(?P<intf>[\w\-\.\/]+) +is +(?P<intf_status>[\w\s]+), +'
                         'line +protocol +is +(?P<oper_status>\w+)$')
        
        # Internet address is fe80::5054:ff:fefa:9ad7
        p2 = re.compile(r'^Internet +address +is +(?P<ip>[\w\/\.\:]+)$')

        # MLD is enabled on interface
        p3 = re.compile(r'^MLD +is +(?P<status>\w+) +on +interface$')

        # Current MLD version is 2
        p4 = re.compile(r'^Current +MLD +version +is +(?P<ver>\d+)$')

        # MLD query interval is 366 seconds
        p5 = re.compile(r'^MLD +query +interval +is +(?P<query_interval>\d+) +seconds$')

        # MLD querier timeout is 3666 seconds
        p6 = re.compile(r'^MLD +querier +timeout +is +'
                         '(?P<timeout>\d+) +seconds$')

        # MLD max query response time is 12 seconds
        p7 = re.compile(r'^MLD +max +query +response +time +is +'
                         '(?P<time>\d+) +seconds$')

        # Last member query response interval is 1 seconds
        p8 = re.compile(r'^Last +member +query +response +interval +is '
                         '+(?P<time>\d+) +(seconds|ms)$')

        # MLD activity: 18 joins, 5 leaves
        p9 = re.compile(r'^MLD +activity: +(?P<joins>\d+) +joins, +(?P<leaves>\d+) +leaves$')

        # MLD querying router is FE80::5054:FF:FE7C:DC70
        p10 = re.compile(r'^MLD +querying +router +is +(?P<querier>[\w\.\:]+)$')

        # Time elapsed since last query sent 00:30:16
        p11 = re.compile(r'^Time +elapsed +since +last +query +sent +'
              			  '(?P<time_elapsed_since_last_query_sent>[\w\:]+)$')

        # Time elapsed since IGMP router enabled 1d06h
        p12 = re.compile(r'^Time +elapsed +since +IGMP +router +enabled +'
                		  '(?P<time_elapsed_since_igmp_router_enabled>[\w\:]+)$')

        # Time elapsed since last report received 00:00:51
        p13 = re.compile(r'^Time +elapsed +since +last +report +received +'
                		  '(?P<time_elapsed_since_last_report_received>[\w\:]+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = group['intf']
                if vrf:
                    vrf = vrf
                else:
                    vrf = 'default'
                vrf_dict = parsed_dict.setdefault('vrf', {}).\
                                       setdefault(vrf, {})

                if 'interface' not in parsed_dict['vrf'][vrf]:
                    interface_dict = vrf_dict.setdefault('interface', {})
                if intf not in parsed_dict['vrf'][vrf]['interface']:
                    interface_dict = vrf_dict.setdefault('interface', {}).\
                                              setdefault(intf, {})

                interface_dict['oper_status'] = group['oper_status'].lower()
                interface_dict['interface_status'] = group['intf_status'].lower()
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface_dict['internet_address'] = group['ip']
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                status = group['status'].lower()
                interface_dict['enable'] = True if 'enable' in status else False
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                interface_dict['version'] = int(group['ver'])
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                interface_dict['query_interval'] = int(group['query_interval'])
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                interface_dict['querier_timeout'] = int(group['timeout'])
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                interface_dict['query_max_response_time'] = int(group['time'])
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                interface_dict['last_member_query_interval'] = int(group['time'])
                continue

            m = p9.match(line)
            if m:
                if 'counters' not in interface_dict:
                    counters_dict = interface_dict.setdefault('counters', {})

                group = m.groupdict()
                counters_dict['joins'] = int(group['joins'])
                counters_dict['leaves'] = int(group['leaves'])
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                interface_dict['querier'] = group['querier']
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                interface_dict['time_elapsed_since_last_query_sent'] = \
                    group['time_elapsed_since_last_query_sent']
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                interface_dict['time_elapsed_since_igmp_router_enabled'] = \
                    group['time_elapsed_since_igmp_router_enabled']
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                interface_dict['time_elapsed_since_last_report_received'] = \
                    group['time_elapsed_since_last_report_received']
                continue

        return parsed_dict




# ==============================================================================
# Schema for 
#    * 'show mld groups detail'
#    * 'show mld vrf {vrf} groups detail'
#    * 'show mld groups {group} detail'
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
                'interface': {
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
                        'group': {
                            Any(): {
                                'up_time': str,
                                'router_mode': str,
                                'host_mode': str,
                                'last_reporter': str,
                                Optional('suppress'): int,
                                Optional('expire'): str,
                                Optional('source'): {
                                    Any(): {
                                        Optional('expire'): str,
                                        'forward': bool,
                                        Optional('flags'): str,
                                        'up_time': str,
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
# Parser for 
#    * 'show mld groups detail'
#    * 'show mld vrf {vrf} groups detail'
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
            vrf = 'default'
            out = output

        # initial variables
        parsed_dict = {}

        # regex

        # Interface:      GigabitEthernet0/0/0/0
        p1 = re.compile(r'^Interface: +(?P<intf>[\w\.\-\/]+)$')

        # Group:          ff15:1::1
        p2 = re.compile(r'^Group: +(?P<group>[\w\.\:]+)$')

        # Host mode:      INCLUDE
        p3 = re.compile(r'^Host +mode: +(?P<host_mode>\w+)$')

		# Uptime:         08:06:00
        p4 = re.compile(r'^Uptime: +(?P<up_time>[\w\:\.]+)$')

        # Router mode:    INCLUDE
        # Router mode:    EXCLUDE (Expires: 00:29:15)
        p5 = re.compile(r'^Router +mode: +(?P<router_mode>\w+)'
                         '( *\(Expires: +(?P<expire>[\w\.\:]+)\))?$')

       	# Last reporter:  fe80::5054:ff:fefa:9ad7
        p6 = re.compile(r'^Last +reporter: +(?P<last_reporter>[\w\.\:]+)$')

        # Suppress:       0
        p7 = re.compile(r'^Suppress: +(?P<suppress>(\d+))$')

        # Source Address                          Uptime    Expires   Fwd  Flags
        p8_1 = re.compile(r'^Source +Address +Uptime +Expires +Fwd +Flags$')
        
        # 2001:db8:2:2::2                       08:06:00  01:00:00  Yes  Remote Local 2d
        p8 = re.compile(r'^(?P<source>(?!No)[\w\.\:]+) +'
                         '(?P<up_time>[\w\.\:]+) +'
                         '(?P<expire>[\w\.\:]+) +'
                         '(?P<forward>\w+) +'
                         '(?P<flags>[\w\s]+)$')


        for line in out.splitlines():
            line = line.strip()

            # Interface:\tGigabitEthernet0/0/0/0
            line = line.replace('\t', '    ')

            m = p1.match(line)
            if m:
                gd = m.groupdict()

                if vrf:
                    vrf = vrf
                else:
                    vrf = 'default'
                vrf_dict = parsed_dict.setdefault('vrf', {}).\
                                       setdefault(vrf, {})

                intf = gd['intf']
                if 'interface' not in parsed_dict['vrf'][vrf]:
                    interface_dict = vrf_dict.setdefault('interface', {})
                if intf not in parsed_dict['vrf'][vrf]['interface']:
                    interface_dict = vrf_dict.setdefault('interface', {}).\
                                              setdefault(intf, {})
                continue


            m = p2.match(line)
            if m:
                gd = m.groupdict()
                group = gd['group']
                if 'group' not in parsed_dict['vrf'][vrf]['interface'][intf]:
                    group_dict = interface_dict.setdefault('group', {})
                if group not in parsed_dict['vrf'][vrf]['interface'][intf]['group']:
                    group_dict = interface_dict.setdefault('group', {}).\
                                                setdefault(group, {})
                continue

            m = p3.match(line)
            if m:
                gd = m.groupdict()
                group_dict['host_mode'] = gd['host_mode'].lower()
                continue

            m = p4.match(line)
            if m:
                gd = m.groupdict()
                group_dict['up_time'] = gd['up_time']
                continue

            m = p5.match(line)
            if m:
                gd = m.groupdict()
                expire = gd['expire']
                group_dict['router_mode'] = gd['router_mode'].lower()
                if expire:
                    group_dict['expire'] = expire
                continue

            m = p6.match(line)
            if m:
                gd = m.groupdict()
                group_dict['last_reporter'] = gd['last_reporter']
                continue

            m = p7.match(line)
            if m:
                gd = m.groupdict()
                group_dict['suppress'] = int(gd['suppress'])
                continue

            m = p8_1.match(line)
            if m:
                continue

            m = p8.match(line)
            if m:
                gd = m.groupdict()
                source = gd['source']
                flags = gd['flags']

                # group structure
                if 'source' not in parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]:
                    source_dict = group_dict.setdefault('source', {})
                if source not in parsed_dict['vrf'][vrf]['interface'][intf]['group'][group]['source']:
                    source_dict = group_dict.setdefault('source', {}).\
                                             setdefault(source, {})
                source_dict['up_time'] = gd['up_time']
                source_dict['expire'] = gd['expire']
                source_dict['forward'] = True \
                    if gd['forward'].lower() == 'yes' else False
                source_dict['flags'] = flags

                flag_list = flags.lower().split()
                if (('4' in flag_list or '2d' in flag_list) and 'e' in flag_list) or '2b' in flag_list:
                    keys = ['join_group', 'static_group']
                elif '4' in flag_list or '2d' in flag_list or '29' in flag_list:
                    keys = ['join_group']
                elif 'e' in flag_list or 'a' in flag_list:
                    keys = ['static_group']
                else:
                    keys = []

                if keys:
                    static_join_group = group + ' ' + source
                    for key in keys:
                        if key not in parsed_dict['vrf'][vrf]['interface'][intf]:
                            key_dict = interface_dict.setdefault(key, {})

                        if static_join_group not in parsed_dict['vrf'][vrf]['interface'][intf][key]:
                            static_join_group_dict = key_dict.setdefault(static_join_group, {})

                        static_join_group_dict['group'] = group
                        static_join_group_dict['source'] = source

        return parsed_dict


# ==============================================================================
# Parser for 
#    * 'show mld groups {group} detail'
# ==============================================================================
class ShowMldGroupsGroupDetail(ShowMldGroupsDetail):
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
