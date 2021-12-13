"""
show_igmp.py

IOSXE parsers for the following show commands:

    * show ip igmp interface 
    * show ip igmp vrf <WORD> interface 
    * show ip igmp groups detail
    * show ip igmp vrf <WORD> groups detail
    * show ip igmp ssm-mapping <WORD>
    * show ip igmp vrf <WORD> ssm-mapping <WORD>
    * show ip igmp snooping mrouter
    * show ip igmp snooping querier
    * show ip igmp snooping groups
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ==============================================
# Parser for 'show ip igmp interface'
# Parser for 'show ip igmp vrf <WORD> interface'
# ==============================================

class ShowIpIgmpInterfaceSchema(MetaParser):
    """
    Schema for 'show ip igmp interface'
    Schema for 'show ip igmp vrf <WORD> interface'
    """

    schema = {'vrf':
                {Any(): {
                    Optional('global_max_groups'): int,
                    Optional('global_active_groups'): int,
                    'interface': {
                        Any(): {
                            Optional('oper_status'): str,
                            'interface_status': str,
                            Optional('internet_protocol_processing'): bool,
                            Optional('interface_address'): str,
                            Optional('enable'): bool,
                            Optional('host_version'): int,
                            Optional('router_version'): int,
                            Optional('query_interval'): int,
                            Optional('configured_query_interval'): int,
                            Optional('querier_timeout'): int,
                            Optional('configured_querier_timeout'): int,
                            Optional('query_max_response_time'): int,
                            Optional('last_member_query_interval'): int,
                            Optional('last_member_query_count'): int,
                            Optional('group_policy'): str,
                            Optional('max_groups'): int,
                            Optional('active_groups'): int,
                            Optional('counters'): {
                                'joins': int,
                                'leaves': int,
                            },
                            Optional('multicast'): {
                                Optional('routing_enable'): bool,
                                Optional('ttl_threshold'): int,
                                Optional('designated_router'): str,
                                Optional('routing_table'): str,
                                Optional('dr_this_system'): bool,
                            },
                            Optional('querier'): str,
                            Optional('query_this_system'): bool,
                            Optional('joined_group'): {
                                Any(): {
                                    'number_of_users': int,
                                },
                            }
                        },
                    }
                }
            },
        }

class ShowIpIgmpInterface(ShowIpIgmpInterfaceSchema):
    """
    Parser for 'show ip igmp interface'
    Parser for 'show ip igmp vrf <WORD> interface'
    """
    cli_command = ['show ip igmp vrf {vrf} interface','show ip igmp interface']
    exclude = ['joins', 'leaves']

    def cli(self, vrf='',output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]

            out = self.device.execute(cmd)
        else:
            out = output

        vrf = 'default' if not vrf else vrf

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Global IGMP State Limit : 1 active out of 20 max
            p1 = re.compile(r'^Global +IGMP +State +Limit *: +'
                             '(?P<active>\d+) +active +out +of +(?P<global_max_groups>\d+) +max$')
            m = p1.match(line)
            if m:
                max_groups = int(m.groupdict()['global_max_groups'])
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                ret_dict['vrf'][vrf]['global_max_groups'] = max_groups
                ret_dict['vrf'][vrf]['global_active_groups'] = \
                    int(m.groupdict()['active'])
                continue

            # GigabitEthernet1 is up, line protocol is up
            p2 = re.compile(r'^(?P<intf>[\w\-\.\/]+) +is +(?P<intf_status>[\w\s]+), +'
                             'line +protocol +is +(?P<oper_status>\w+)$')
            m = p2.match(line)
            if m:
                intf = m.groupdict()['intf']
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                if 'interface' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['interface'] = {}
                if intf not in ret_dict['vrf'][vrf]['interface']:
                    ret_dict['vrf'][vrf]['interface'][intf] = {}

                ret_dict['vrf'][vrf]['interface'][intf]['oper_status'] = \
                    m.groupdict()['oper_status'].lower()
                ret_dict['vrf'][vrf]['interface'][intf]['interface_status'] = \
                    m.groupdict()['intf_status'].lower()
                continue

            # Internet protocol processing disabled
            p2_2 = re.compile(r'^Internet protocol processing (?P<disabled>disabled)$')
            m = p2_2.match(line)
            if m:
                ret_dict['vrf'][vrf]['interface'][intf]['internet_protocol_processing'] = False
                continue

            # Internet address is 10.1.2.1/24
            p3 = re.compile(r'^Internet +address +is +(?P<ip>[\w\/\.\:]+)$')
            m = p3.match(line)
            if m:                
                ret_dict['vrf'][vrf]['interface'][intf]['interface_address'] = \
                    m.groupdict()['ip']
                continue

            # IGMP is enabled on interface
            p4 = re.compile(r'^IGMP +is +(?P<status>\w+) +on +interface$')
            m = p4.match(line)
            if m:      
                status = m.groupdict()['status'].lower()          
                ret_dict['vrf'][vrf]['interface'][intf]['enable'] = True if \
                    'enable' in status else False
                continue
            
            # Current IGMP host version is 3
            p5 = re.compile(r'^Current +IGMP +host +version +is +(?P<ver>\d+)$')
            m = p5.match(line)
            if m:                
                ret_dict['vrf'][vrf]['interface'][intf]['host_version'] = int(m.groupdict()['ver'])
                continue

            # Current IGMP router version is 3
            p6 = re.compile(r'^Current +IGMP +router +version +is +(?P<ver>\d+)$')
            m = p6.match(line)
            if m:                
                ret_dict['vrf'][vrf]['interface'][intf]['router_version'] = int(m.groupdict()['ver'])
                continue

            # IGMP query interval is 133 seconds
            p7 = re.compile(r'^IGMP +query +interval +is +(?P<query_interval>\d+) +seconds$')
            m = p7.match(line)
            if m:                
                ret_dict['vrf'][vrf]['interface'][intf]['query_interval'] = \
                    int(m.groupdict()['query_interval'])
                continue

            # IGMP configured query interval is 133 seconds
            p8 = re.compile(r'^IGMP +configured +query +interval +is +'
                             '(?P<query_interval>\d+) +seconds$')
            m = p8.match(line)
            if m:                
                ret_dict['vrf'][vrf]['interface'][intf]['configured_query_interval'] = \
                    int(m.groupdict()['query_interval'])
                continue

            # IGMP querier timeout is 266 seconds
            p9 = re.compile(r'^IGMP +querier +timeout +is +'
                             '(?P<timeout>\d+) +seconds$')
            m = p9.match(line)
            if m:                
                ret_dict['vrf'][vrf]['interface'][intf]['querier_timeout'] = \
                    int(m.groupdict()['timeout'])
                continue

            # IGMP configured querier timeout is 266 seconds
            p10 = re.compile(r'^IGMP +configured +querier +timeout +is +'
                             '(?P<timeout>\d+) +seconds$')
            m = p10.match(line)
            if m:                
                ret_dict['vrf'][vrf]['interface'][intf]['configured_querier_timeout'] = \
                    int(m.groupdict()['timeout'])
                continue

            # IGMP max query response time is 10 seconds
            p11 = re.compile(r'^IGMP +max +query +response +time +is +'
                             '(?P<time>\d+) +seconds$')
            m = p11.match(line)
            if m:                
                ret_dict['vrf'][vrf]['interface'][intf]['query_max_response_time'] = \
                    int(m.groupdict()['time'])
                continue

            # Last member query count is 2
            p12 = re.compile(r'^Last +member +query +count +is +(?P<count>\d+)$')
            m = p12.match(line)
            if m:                
                ret_dict['vrf'][vrf]['interface'][intf]['last_member_query_count'] = \
                    int(m.groupdict()['count'])
                continue

            # Last member query response interval is 100 ms
            p13 = re.compile(r'^Last +member +query +response +interval +is '
                              '+(?P<time>\d+) +ms$')
            m = p13.match(line)
            if m:                
                ret_dict['vrf'][vrf]['interface'][intf]['last_member_query_interval'] = \
                    int(m.groupdict()['time'])
                continue

            # Inbound IGMP access group is test2
            p14 = re.compile(r'^Inbound +IGMP +access +group +is +(?P<group_policy>\S+)$')
            m = p14.match(line)
            if m:                
                ret_dict['vrf'][vrf]['interface'][intf]['group_policy'] = \
                    m.groupdict()['group_policy']
                continue

            # IGMP activity: 13 joins, 3 leaves
            p15 = re.compile(r'^IGMP +activity: +(?P<joins>\d+) +joins, +(?P<leaves>\d+) +leaves$')
            m = p15.match(line)
            if m:
                if 'counters' not in ret_dict['vrf'][vrf]['interface'][intf]:
                    ret_dict['vrf'][vrf]['interface'][intf]['counters'] = {}
                ret_dict['vrf'][vrf]['interface'][intf]['counters']['joins'] = \
                    int(m.groupdict()['joins'])
                ret_dict['vrf'][vrf]['interface'][intf]['counters']['leaves'] = \
                    int(m.groupdict()['leaves'])
                continue

            # Interface IGMP State Limit : 1 active out of 10 max
            p16 = re.compile(r'^Interface +IGMP +State +Limit *: +'
                              '(?P<active>\d+) +active +out +of +(?P<max>\d+) +max$')
            m = p16.match(line)
            if m:                
                ret_dict['vrf'][vrf]['interface'][intf]['max_groups'] = int(m.groupdict()['max'])
                ret_dict['vrf'][vrf]['interface'][intf]['active_groups'] = int(m.groupdict()['active'])
                continue

            # Multicast routing is enabled on interface
            p17 = re.compile(r'^Multicast +routing +is +enabled +on +interface$')
            m = p17.match(line)
            if m:
                if 'multicast' not in ret_dict['vrf'][vrf]['interface'][intf]:
                    ret_dict['vrf'][vrf]['interface'][intf]['multicast'] = {}
                ret_dict['vrf'][vrf]['interface'][intf]['multicast']['routing_enable'] = True
                continue

            # Multicast TTL threshold is 0
            p18 = re.compile(r'^Multicast +TTL +threshold +is +(?P<ttl>\d+)$')
            m = p18.match(line)
            if m:
                if 'multicast' not in ret_dict['vrf'][vrf]['interface'][intf]:
                    ret_dict['vrf'][vrf]['interface'][intf]['multicast'] = {}
                ret_dict['vrf'][vrf]['interface'][intf]['multicast']['ttl_threshold'] = \
                    int(m.groupdict()['ttl'])
                continue

            # Multicast designated router (DR) is 10.1.2.1 (this system)
            p19 = re.compile(r'^Multicast +designated +router +\(DR\) +'
                              'is +(?P<ip>[\w\.\:]+)(?P<dummy> *\([\w\s]+\))?$')
            m = p19.match(line)
            if m:
                if 'multicast' not in ret_dict['vrf'][vrf]['interface'][intf]:
                    ret_dict['vrf'][vrf]['interface'][intf]['multicast'] = {}
                ret_dict['vrf'][vrf]['interface'][intf]['multicast']['designated_router'] = \
                    m.groupdict()['ip']

                if "this system" in str(m.groupdict()['dummy']):
                    ret_dict['vrf'][vrf]['interface'][intf]['multicast']['dr_this_system'] = True
                continue

            # IGMP querying router is 10.1.2.1 (this system)
            p20 = re.compile(r'^IGMP +querying +router +is +(?P<querier>[\w\.\:]+)'
                              '(?P<dummy> *\([\w\s]+\))?$')
            m = p20.match(line)
            if m:
                ret_dict['vrf'][vrf]['interface'][intf]['querier'] = \
                    m.groupdict()['querier']
                if "this system" in str(m.groupdict()['dummy']):
                    ret_dict['vrf'][vrf]['interface'][intf]['query_this_system'] = True
                continue

            # Multicast groups joined by this system (number of users):
            #   224.0.1.40(1)  239.4.4.4(1)  239.3.3.3(1)
            p21 = re.compile(r'([\w\.\:]+)\((\d+)\)')
            m = p21.findall(line)
            if m:
                if 'joined_group' not in ret_dict['vrf'][vrf]['interface'][intf]:
                    ret_dict['vrf'][vrf]['interface'][intf]['joined_group'] = {}
                for item in m:
                    if item[0] not in ret_dict['vrf'][vrf]['interface'][intf]['joined_group']:
                        ret_dict['vrf'][vrf]['interface'][intf]['joined_group'][item[0]] = {}
                    ret_dict['vrf'][vrf]['interface'][intf]['joined_group']\
                        [item[0]]['number_of_users'] = int(item[1])
                continue

            # Multicast Routing table VRF1
            p22 = re.compile(r'^Multicast +Routing +table +(?P<routing_table>\S+)$')
            m = p22.match(line)
            if m:
                if 'multicast' not in ret_dict['vrf'][vrf]['interface'][intf]:
                    ret_dict['vrf'][vrf]['interface'][intf]['multicast'] = {}
                ret_dict['vrf'][vrf]['interface'][intf]['multicast']['routing_table'] = \
                    m.groupdict()['routing_table']
                continue

        return ret_dict



# ==================================================
# Parser for 'show ip igmp groups detail'
# Parser for 'show ip igmp vrf <WORD> groups detail'
# ==================================================

class ShowIpIgmpGroupsDetailSchema(MetaParser):
    """
    Schema for 'show ip igmp groups detail'
    Schema for 'show ip igmp vrf <WORD> groups detail'
    """

    schema = {'vrf':
                {Any(): {
                    'interface': {
                        Any(): {
                            Optional('join_group'): {
                                Any(): {
                                    'group': str,
                                    'source': str,
                                    Optional('expire'): str,
                                    'up_time': str,
                                    'last_reporter': str,
                                    Optional('flags'): str,
                                    Optional('v3_exp'): str,
                                    Optional('csr_exp'):str,
                                    Optional('forward'): bool,
                                    Optional('source_flags'): str,
                                }
                            },
                            Optional('static_group'): {
                                Any(): {
                                    'group': str,
                                    'source': str,
                                    Optional('expire'): str,
                                    'up_time': str,
                                    'last_reporter': str,
                                    Optional('flags'): str,
                                    Optional('v3_exp'): str,
                                    Optional('csr_exp'):str,
                                    Optional('forward'): bool,
                                    Optional('source_flags'): str,
                                }
                            },
                            'group': {
                                Any(): {
                                    Optional('expire'): str,
                                    'up_time': str,
                                    'group_mode': str,
                                    'last_reporter': str,
                                    Optional('flags'): str,
                                    Optional('source'): {
                                        Any(): {
                                            'v3_exp': str,
                                            'csr_exp':str,
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

class ShowIpIgmpGroupsDetail(ShowIpIgmpGroupsDetailSchema):
    """
    Parser for 'show ip igmp groups detail'
    Parser for 'show ip igmp vrf <WORD> groups detail'
    """
    exclude = ['expire', 'up_time', 'ast_reporter']


    # internal function to do the key creation wehn the key is assign first
    def build_pre_define_key(self, key_value_dict):
        ret_dict = {}
        for key, value in key_value_dict.items():
            try:
                if value:
                    ret_dict[key] = value
            except Exception:
                pass
        return ret_dict

    cli_command = ['show ip igmp vrf {vrf} groups detail', 'show ip igmp groups detail']

    def cli(self, vrf='',output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                vrf = 'default'
                cmd = self.cli_command[1]

            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables
        ret_dict = {}
        keys = None
        expire = None
        up_time = None
        last_reporter = None
        flags = None

        for line in out.splitlines():
            line = line.strip()
            line = line.replace('\t', '    ')

            # Interface:        GigabitEthernet1
            # Interface:\tVlan211
            p1 = re.compile(r'^Interface: +(?P<intf>[\w\.\-\/]+)$')
            m = p1.match(line)
            if m:
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                intf = m.groupdict()['intf']
                if 'interface' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['interface'] = {}
                if intf not in ret_dict['vrf'][vrf]['interface']:
                    ret_dict['vrf'][vrf]['interface'][intf] = {}
                continue

            # Group:                239.1.1.1
            p2 = re.compile(r'^Group: +(?P<group>[\w\.\:]+)$')
            m = p2.match(line)
            if m:
                group = m.groupdict()['group']
                if 'group' not in ret_dict['vrf'][vrf]['interface'][intf]:
                    ret_dict['vrf'][vrf]['interface'][intf]['group'] = {}
                if group not in ret_dict['vrf'][vrf]['interface'][intf]['group']:
                    ret_dict['vrf'][vrf]['interface'][intf]['group'][group] = {}
                continue

            # Flags:                L U
            p3 = re.compile(r'^Flags:( *(?P<flags>[\w\s]+))?$')
            m = p3.match(line)
            if m:
                flags = m.groupdict()['flags']
                # flags
                if flags:
                    if 'SG' in flags:
                        keys = ['static_group']
                        if 'static_group' not in ret_dict['vrf'][vrf]['interface'][intf]:
                            ret_dict['vrf'][vrf]['interface'][intf]['static_group'] = {}
                        if flags.replace('SG', ''):
                            keys.append('join_group')
                            if 'join_group' not in ret_dict['vrf'][vrf]['interface'][intf]:
                                ret_dict['vrf'][vrf]['interface'][intf]['join_group'] = {}
                    else:
                        keys = ['join_group']
                        if 'join_group' not in ret_dict['vrf'][vrf]['interface'][intf]:
                            ret_dict['vrf'][vrf]['interface'][intf]['join_group'] = {}
                    ret_dict['vrf'][vrf]['interface'][intf]['group'][group]['flags'] = flags
                else:
                    keys = None
                continue

            # Uptime:                00:05:06
            p4 = re.compile(r'^Uptime: +(?P<up_time>[\w\:\.]+)$')
            m = p4.match(line)
            if m:
                up_time = m.groupdict()['up_time']
                ret_dict['vrf'][vrf]['interface'][intf]['group'][group]['up_time'] = up_time
                continue

            # Group mode:        INCLUDE
            # Group mode:        EXCLUDE (Expires: 00:06:06)
            p5 = re.compile(r'^Group +mode: +(?P<group_mode>\w+)'
                             '( *\(Expires: +(?P<expire>[\w\.\:]+)\))?$')
            m = p5.match(line)
            if m:
                group_mode = m.groupdict()['group_mode']
                expire = m.groupdict()['expire']
                ret_dict['vrf'][vrf]['interface'][intf]['group'][group]['group_mode'] = group_mode.lower()
                if expire:
                    ret_dict['vrf'][vrf]['interface'][intf]['group'][group]['expire'] = expire
                continue

            # Last reporter:        10.1.2.1
            p6 = re.compile(r'^Last +reporter: +(?P<last_reporter>[\w\.\:]+)$')
            m = p6.match(line)
            if m:
                last_reporter = m.groupdict()['last_reporter']
                ret_dict['vrf'][vrf]['interface'][intf]['group'][group]['last_reporter'] = last_reporter
                continue

            # Source Address   Uptime    v3 Exp   CSR Exp   Fwd  Flags
            # 10.4.1.1         00:05:06  stopped   stopped   Yes  L
            p7 = re.compile(r'^(?P<source>[\w\.\:]+) +'
                             '(?P<up_time>[\w\.\:]+) +'
                             '(?P<v3_exp>\w+) +'
                             '(?P<csr_exp>\w+) +'
                             '(?P<forward>\w+) +'
                             '(?P<source_flags>\w+)$')
            m = p7.match(line)
            if m:
                source = m.groupdict()['source']
                v3_exp = m.groupdict()['v3_exp']
                csr_exp = m.groupdict()['csr_exp']
                forward = True if m.groupdict()['forward'].lower() == 'yes' else False
                source_flags = m.groupdict()['source_flags']


                # group structure
                if 'source' not in ret_dict['vrf'][vrf]['interface'][intf]['group'][group]:
                    ret_dict['vrf'][vrf]['interface'][intf]['group'][group]['source'] = {}
                if source not in ret_dict['vrf'][vrf]['interface'][intf]['group'][group]['source']:
                    ret_dict['vrf'][vrf]['interface'][intf]['group'][group]['source'][source] = {}

                ret_dict['vrf'][vrf]['interface'][intf]['group'][group]\
                    ['source'][source]['up_time'] = m.groupdict()['up_time']

                ret_dict['vrf'][vrf]['interface'][intf]['group'][group]\
                    ['source'][source]['v3_exp'] = v3_exp

                ret_dict['vrf'][vrf]['interface'][intf]['group'][group]\
                    ['source'][source]['csr_exp'] = csr_exp

                ret_dict['vrf'][vrf]['interface'][intf]['group'][group]\
                    ['source'][source]['forward'] = forward

                ret_dict['vrf'][vrf]['interface'][intf]['group'][group]\
                    ['source'][source]['flags'] = source_flags

                # join_group or static_group structure
                if keys:
                    static_join_group = group + ' ' + source
                    for key in keys:
                        if static_join_group not in ret_dict['vrf'][vrf]['interface'][intf][key]:
                            ret_dict['vrf'][vrf]['interface'][intf][key][static_join_group] = {}

                        ret_dict['vrf'][vrf]['interface'][intf][key][static_join_group]['v3_exp'] = v3_exp
                        ret_dict['vrf'][vrf]['interface'][intf][key][static_join_group]['csr_exp'] = csr_exp
                        ret_dict['vrf'][vrf]['interface'][intf][key][static_join_group]['forward'] = forward
                        ret_dict['vrf'][vrf]['interface'][intf][key][static_join_group]['flags'] = flags
                        ret_dict['vrf'][vrf]['interface'][intf][key][static_join_group]['group'] = group
                        ret_dict['vrf'][vrf]['interface'][intf][key][static_join_group]['source'] = source

                        # create structure for pre define keys
                        key_value_dict = {'expire': expire,
                                          'up_time': up_time,
                                          'last_reporter': last_reporter,
                                          'flags': flags}

                        ret_dict['vrf'][vrf]['interface'][intf][key][static_join_group].update(
                            self.build_pre_define_key(key_value_dict=key_value_dict))

            # Source list is empty
            p7_1 = re.compile(r'^Source +list +is +empty$')
            m = p7_1.match(line)
            if m:
                source = '*'
                # join_group or static_group structure
                if keys:
                    static_join_group = group + ' ' + source
                    for key in keys:
                        if static_join_group not in ret_dict['vrf'][vrf]['interface'][intf][key]:
                            ret_dict['vrf'][vrf]['interface'][intf][key][static_join_group] = {}    
                        ret_dict['vrf'][vrf]['interface'][intf][key][static_join_group]['group'] = group
                        ret_dict['vrf'][vrf]['interface'][intf][key][static_join_group]['source'] = source                

                        # create structure for pre define keys
                        key_value_dict = {'expire': expire,
                                          'up_time': up_time,
                                          'last_reporter': last_reporter,
                                          'flags': flags}

                        ret_dict['vrf'][vrf]['interface'][intf][key][static_join_group].update(
                            self.build_pre_define_key(key_value_dict=key_value_dict))

                continue

        return ret_dict


# ========================================================
# Parser for 'show ip igmp ssm-mapping <WROD>'
# Parser for 'show ip igmp vrf <WORD> ssm-mapping <WORD>'
# ========================================================

class ShowIpIgmpSsmMappingSchema(MetaParser):
    """
    Schema for 'show ip igmp ssm-mapping <WROD>'
    Schema for 'show ip igmp vrf <WORD> ssm-mapping <WORD>'
    """

    schema = {'vrf':
                {Any(): {
                    'ssm_map': {
                        Any(): {
                            'source_addr': str,
                            'group_address': str,
                            'database': str,
                        }
                    }
                },
            }
        }

class ShowIpIgmpSsmMapping(ShowIpIgmpSsmMappingSchema):
    """
    Parser for 'show ip igmp ssm-mapping <WROD>'
    parser for 'show ip igmp vrf <WORD> ssm-mapping <WORD>'
    """
    cli_command = ['show ip igmp vrf {vrf} ssm-mapping {group}', 'show ip igmp ssm-mapping {group}']

    def cli(self, group, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf,group=group)
            else:
                vrf = 'default'
                cmd = self.cli_command[1].format(group=group)

            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables
        ret_dict = {}
        group_address = ''
        database = None

        for line in out.splitlines():
            line = line.strip()

            # Group address: 224.0.1.40
            p1 = re.compile(r'^Group +address *: +(?P<group_address>[\w\.\:]+)$')
            m = p1.match(line)
            if m:
                group_address = m.groupdict()['group_address']
                continue

            # Database     : Static
            p2 = re.compile(r'^Database *: +(?P<database>\w+)$')
            m = p2.match(line)
            if m:
                database = m.groupdict()['database']
                continue

            # Source list  : 10.4.1.1
            p3 = re.compile(r'^Source +list *: +(?P<source_addr>[\w\.\:]+)$')
            m = p3.match(line)
            if m:
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'ssm_map' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['ssm_map'] = {}

                source_addr = m.groupdict()['source_addr']
                ssm = source_addr + ' ' + group_address
                if ssm not in ret_dict['vrf'][vrf]['ssm_map']:
                    ret_dict['vrf'][vrf]['ssm_map'][ssm] = {}

                ret_dict['vrf'][vrf]['ssm_map'][ssm]['source_addr'] = source_addr

                if group_address:
                    ret_dict['vrf'][vrf]['ssm_map'][ssm]['group_address'] = group_address

                if database:
                    ret_dict['vrf'][vrf]['ssm_map'][ssm]['database'] = database.lower()
                continue

            # 10.4.1.2
            p3_1 = re.compile(r'^(?P<source_addr>[\w\.\:]+)$')
            m = p3_1.match(line)
            if m:
                source_addr = m.groupdict()['source_addr']
                ssm = source_addr + ' ' + group_address
                if ssm not in ret_dict['vrf'][vrf]['ssm_map']:
                    ret_dict['vrf'][vrf]['ssm_map'][ssm] = {}

                ret_dict['vrf'][vrf]['ssm_map'][ssm]['source_addr'] = source_addr

                if group_address:
                    ret_dict['vrf'][vrf]['ssm_map'][ssm]['group_address'] = group_address

                if database:
                    ret_dict['vrf'][vrf]['ssm_map'][ssm]['database'] = database.lower()
                continue

        return ret_dict

# ========================================================
# Parser for 'show ip igmp snooping mrouter'
# ========================================================

class ShowIpIgmpSnoopingMrouterSchema(MetaParser):
    """
    Schema for 'show ip igmp snooping mrouter'
    """

    schema = {
        'vlan':
            {Any():{
                'port': str
            },
        }
    }


class ShowIpIgmpSnoopingMrouter(ShowIpIgmpSnoopingMrouterSchema):
    """
    Parser for 'show ip igmp snooping mrouter'
    """
    cli_command = 'show ip igmp snooping mrouter'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        # initial variables
        vlan_dict = {}

        # 1    Po62(dynamic), Router
        p1 = re.compile(r'(?P<vlan_id>\d+)+\s+(?P<port>.+)')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict = vlan_dict.setdefault('vlan',{})
                vlan_id = group['vlan_id']
                port = group['port']
                ret_dict[vlan_id] = {}
                ret_dict[vlan_id]['port'] = port
        return vlan_dict



# ========================================================
# Parser for 'show ip igmp snooping querier'
# ========================================================

class ShowIpIgmpSnoopingQuerierSchema(MetaParser):
    """
    Schema for 'show ip igmp snooping querier'
    """

    schema = {
        'vlans': {
            Any(): {
                  'ip_address': str,
                  'igmp_version': str,
                  'port': str
            },
        }
    }



class ShowIpIgmpSnoopingQuerier(ShowIpIgmpSnoopingQuerierSchema):
    """
    Parser for 'show ip igmp snooping querier'
    """
    cli_command = 'show ip igmp snooping querier'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        # initial variables
        vlan_dict = {}

        for line in out.splitlines():
            line = line.strip()

            #327       27.1.1.2                 v2          Router
            p1 = re.compile(r'^(?P<vlan>\d+) +(?P<ip_address>[\d.]+) +(?P<igmp_version>\w+) +(?P<port>\w+)$')

            m = p1.match(line)
            if m:
                group = m.groupdict()

                ret_dict = vlan_dict.setdefault('vlans', {})

                ip_address = group['ip_address']
                vlan = group['vlan']
                port = group['port']
                igmp_version = group['igmp_version']

                ret_dict[vlan] = {}
                ret_dict[vlan]['ip_address'] = ip_address
                ret_dict[vlan]['igmp_version'] = igmp_version
                ret_dict[vlan]['port'] = port

        return vlan_dict


# ========================================================
# Parser for 'show ip igmp snooping groups'
# ========================================================

class ShowIpIgmpSnoopingGroupsSchema(MetaParser):
    """
    Schema for 'show ip igmp snooping groups'
    """

    schema = {
        'igmp_groups': {
            Any(): {
                'vlan_id': str,
                'type': str,
                'version': str,
                'port': str
            },
        }
    }


class ShowIpIgmpSnoopingGroups(ShowIpIgmpSnoopingGroupsSchema):
    """
    Parser for 'show ip igmp snooping groups'
    """
    cli_command = 'show ip igmp snooping groups'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        igmp_dict = {}

        for line in out.splitlines():
            line = line.strip()


            #801       225.6.1.1                igmp        v2          pw100155
            p1 = re.compile(r'^(?P<vlan_id>\d+) +(?P<group_ip>[\d.]+) +(?P<type>\w+) +(?P<version>\w+) +(?P<port>\w+)$')

            m = p1.match(line)
            if m:
                group = m.groupdict()

                ret_dict = igmp_dict.setdefault('igmp_groups', {})

                group_ip = group['group_ip']
                vlan_id = group['vlan_id']
                type = group['type']
                port = group['port']
                version = group['version']

                ret_dict[group_ip] = {}
                ret_dict[group_ip]['vlan_id'] = vlan_id
                ret_dict[group_ip]['type'] = type
                ret_dict[group_ip]['version'] = version
                ret_dict[group_ip]['port'] = port

        return igmp_dict

# ========================================================
# Parser for 'show ip igmp vrf vrf3001 groups'
# ========================================================

class ShowIpIgmpVrfGroupsSchema(MetaParser):
    """
    Schema for 'show ip igmp vrf {vrf} groups'
    """

    schema = {
        'igmp_group_address': {
            Any(): {
                'interface': str,
                'uptime': str,
                'expires': str,
                'last_reporter': str,
            },
        }
    }


class ShowIpIgmpVrfGroups(ShowIpIgmpVrfGroupsSchema):
    """
    Parser for 'show ip igmp vrf {vrf} groups'
    """
    cli_command = 'show ip igmp vrf {vrf} groups'

    def cli(self, vrf, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vrf=vrf))

        # initial variables
        igmp_dict = {}
        
        # 228.1.1.1        Vlan111                  00:03:07  00:02:59  151.1.1.2
        p1=re.compile("^(?P<groupip>[\d\.]+)\s+(?P<interface>\S+)\s+(?P<uptime>\S+)\s+(?P<expires>\S+)\s+(?P<last_reporter>\S+).*$")

        for line in output.splitlines():
            line = line.strip()

            m=p1.match(line)
            if m:
                r=m.groupdict()
                igmp_group_dict=igmp_dict.setdefault('igmp_group_address',{}).setdefault(r['groupip'],{})
                r.pop('groupip')
                for key,value in r.items():
                    igmp_group_dict[key]=value
                continue
        return igmp_dict
     
#==================================================
# Parser for show ip igmp snooping groups count
#==================================================

class ShowIpIgmpSnoopingGroupsCountSchema(MetaParser):
    schema = {
        'total_number_of_groups': {
            'igmp_groups_count': int
        }
    }

class ShowIpIgmpSnoopingGroupsCount(ShowIpIgmpSnoopingGroupsCountSchema):

    cli_command = 'show ip igmp snooping groups count'

    def cli(self, output=None):

        if not output:
            output = self.device.execute(self.cli_command)

        # Total number of groups:   831
        p1 = re.compile(r'^Total\s+number\s+of\s+groups\:\s+(?P<igmp_groups_count>\d+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Total number of groups:   831
            m = p1.match(line)
            if m:
                group = m.groupdict()
                igmp_groups_count_dict = ret_dict.setdefault('total_number_of_groups', {})
                igmp_groups_count_dict['igmp_groups_count'] = int(group['igmp_groups_count'])

        return ret_dict
