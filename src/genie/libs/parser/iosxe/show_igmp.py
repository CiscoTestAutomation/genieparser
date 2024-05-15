"""
show_igmp.py

IOSXE parsers for the following show commands:

    * show ip igmp interface 
    * show ip igmp vrf <WORD> interface 
    * show ip igmp groups detail
    * show ip igmp vrf <WORD> groups detail
    * show ip igmp ssm-mapping
    * show ip igmp ssm-mapping <WORD>
    * show ip igmp vrf <WORD> ssm-mapping <WORD>
    * show ip igmp snooping mrouter
    * show ip igmp snooping querier
    * show ip igmp snooping groups
    * show ip igmp vrf {vrf} snooping groups
    * show platform software fed switch active ip igmp snooping groups count
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
from genie.libs.parser.utils.common import Common
from genie.parsergen import oper_fill_tabular


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
# Parser for 'show ip igmp ssm-mapping'
# ========================================================

class ShowIpIgmpSsmSchema(MetaParser):
    """
    Schema for 'show ip igmp ssm-mapping'
    """
    schema = {'ssm_mapping': str
        }

class ShowIpIgmpSsm(ShowIpIgmpSsmSchema):
    """
    Parser for 'show ip igmp ssm-mapping'
    """
    cli_command = 'show ip igmp ssm-mapping'
    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}
        for line in out.splitlines():
            line = line.strip()
            # SSM Mapping : Disabled
            p1 = re.compile(r'^SSM +Mapping *: +(?P<ssm_mapping>\w+)$')
            m = p1.match(line)
            if m:
                ret_dict['ssm_mapping'] = m.groupdict()['ssm_mapping']
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
            #1         193.1.1.1                v2            Switch
            #10        192.1.1.1                v2            Fou1/0/31
            p1 = re.compile(r'^(?P<vlan>\d+) +(?P<ip_address>[\d.]+) +(?P<igmp_version>\w+) +(?P<port>\S+)$')

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

            # 801       225.6.1.1                igmp        v2          pw100155
            # 10        225.1.1.1                igmp        v2          Tw1/0/4, Tw1/0/25
            p1 = re.compile(r'^(?P<vlan_id>\d+) +(?P<group_ip>[\d\.]+) +(?P<type>\w+) +(?P<version>\w+) +(?P<port>[\S,\s]+)$')

            m = p1.match(line)
            if m:
                group = m.groupdict()
                igmp_dict.setdefault('igmp_groups', {}).setdefault(group.pop('group_ip'), group)

        return igmp_dict


# =====================================================================
# Schema for 'show ip igmp snooping groups vlan <vlan> <group> sources'
# ====================================================================
class ShowIpIgmpSnoopingGroupsVlanSourcesSchema(MetaParser):
    """ Schema for show ip igmp snooping groups vlan <vlan> <group> sources """
    schema = {
        'source_ip': {
            str: {
                'port_list': str,
            }
        },
    }


# =====================================================================
# Parser for 'show ip igmp snooping groups vlan <vlan> <group> sources'
# =====================================================================
class ShowIpIgmpSnoopingGroupsVlanSources(
        ShowIpIgmpSnoopingGroupsVlanSourcesSchema):
    """ Parser for show ip igmp snooping groups vlan <vlan> <group> sources """

    cli_command = ['show ip igmp snooping groups vlan {vlan} {group} sources']

    def cli(self, vlan=None, group=None, output=None):

        cmd = self.cli_command[0].format(vlan=vlan, group=group)

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        parsed_dict = {}

        if 'SourceIP' not in out:
            return parsed_dict

        out = out[out.index('SourceIP'):]

        # initial regexp pattern
        # 192.168.11.11 00:01:31 00:02:32 1/0 Et0/2
        p1 = re.compile(r'^(?P<source>[0-9a-fA-F\.:]+)\s+[\d:\w]+\s+[\d:\w]+'
                        r'\s+\d+\/\d+\s+(?P<port_list>[\w\/:]+)$')
        # 192.168.11.11 stopped 00:02:32 1/0
        p2 = re.compile(r'^(?P<source>[0-9a-fA-F\.:]+)\s+[\d:\w]+'
                        r'\s+[\d:\w]+\s+\d+\/\d+$')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # 192.168.11.11 00:01:31 00:02:32 1/0 Et0/2
            m = p1.match(line)
            if m:
                group_dict = m.groupdict()
                parsed_dict.setdefault('source_ip', {})
                parsed_dict['source_ip'].update({
                    group_dict['source']: {
                        'port_list': group_dict['port_list'],
                    }
                })
                continue

            # 192.168.11.11 stopped 00:02:32 1/0
            m = p2.match(line)
            if m:
                group_dict = m.groupdict()
                parsed_dict.setdefault('source_ip', {})
                parsed_dict['source_ip'].update({
                    group_dict['source']: {
                        'port_list': '',
                    }
                })
                continue

        return parsed_dict


# ===================================================================
# Schema for 'show ip igmp snooping groups vlan <vlan> <group> hosts'
# ===================================================================
class ShowIpIgmpSnoopingGroupsVlanHostsSchema(MetaParser):
    """ Schema for show ip igmp snooping groups vlan <vlan> <group> hosts"""
    schema = {
        Any(): {
            'host_addr': str,
            'filter': str,
            'expire': str,
            'uptime': str,
            'sources': str,
        },
    }


# ===================================================================
# Parser for 'show ip igmp snooping groups vlan <vlan> <group> hosts'
# ===================================================================
class ShowIpIgmpSnoopingGroupsVlanHosts(
        ShowIpIgmpSnoopingGroupsVlanHostsSchema):
    """ Parser for show ip igmp snooping groups vlan <vlan> <group> hosts """

    cli_command = ['show ip igmp snooping groups vlan {vlan} {group} hosts']

    def cli(self, vlan=None, group=None, output=None):
        cmd = self.cli_command[0].format(vlan=vlan, group=group)

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = oper_fill_tabular(
            header_fields=["Host \(MAC\/IP\)", "Filter mode",
                           "Expires", "Uptime", "# Sources"],
            label_fields=['host_addr', 'filter', 'expire', 'uptime', 'sources'],
            index=[0], device_output=out, device_os='iosxe'
        ).entries

        return parsed_dict


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


class ShowIpIgmpVrfSnoopingGroupsSchema(MetaParser):
    '''Schema for show ip igmp vrf {vrf} snooping groups'''
    schema = {
        Any(): {
            'vlan': int,
            'group': str,
            'type': str,
            'version': str,
            'port_list': list
        }
    }


class ShowIpIgmpVrfSnoopingGroups(ShowIpIgmpVrfSnoopingGroupsSchema):
    '''Parser for show ip igmp vrf {vrf} snooping groups'''

    cli_command = 'show ip igmp vrf {vrf} snooping groups'

    def cli(self, vrf="", output=None):

        if not output:
            output = self.device.execute(self.cli_command.format(vrf=vrf))

        # 10        232.1.1.1                igmp        v3          Te1/0/3
        p1 = re.compile(r'^(?P<vlan>\d+)\s+(?P<group>\S+)\s+(?P<type>\S+)\s+(?P<version>\S+)\s+(?P<port_list>[\w/\.\s]+)$')

        ret_dict = {}
        count = 1
        for line in output.splitlines():
            line = line.strip()

            # 10        232.1.1.1                igmp        v3          Te1/0/3
            m = p1.match(line)
            if m:
                output = m.groupdict()
                group_dict = ret_dict.setdefault(str(count), {})
                group_dict.setdefault('vlan', int(output['vlan']))
                group_dict.setdefault('group', output['group'])
                group_dict.setdefault('type', output['type'])
                group_dict.setdefault('version', output['version'])
                port_list = [Common.convert_intf_name(intf) for intf in re.findall(r'[\w/\.]+', output['port_list'])]
                group_dict.setdefault('port_list', port_list)
                count += 1
        return ret_dict

# ========================================================
# Parser for 'show ip igmp groups'
# ========================================================

class ShowIpIgmpGroupsSchema(MetaParser):
    """
    Schema for 'show ip igmp groups'
    """

    schema = {
        'igmp_groups': {
            Any(): {
                'intf': str,
                'uptime': str,
                'expires': str,
                'last_reporter': str,
            },
        }
    }


class ShowIpIgmpGroups(ShowIpIgmpGroupsSchema):
    """
    Parser for 'show ip igmp groups'
    """
    cli_command = 'show ip igmp groups'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial variables
        igmp_dict = {}
        
        # 228.0.8.204      Vlan10                   00:02:26  00:02:45  60.1.1.2
        p1=re.compile(r'^(?P<group>[\w\.\:]+) +(?P<intf>[\w\.\/\-]+) +(?P<uptime>[\w\.\:]+) +(?P<expires>[\w\.\:]+) +(?P<last_reporter>[\w\.\:]+)$')

        for line in output.splitlines():
            line = line.strip()
            # 228.0.8.204      Vlan10                   00:02:26  00:02:45  60.1.1.2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                igmp_dict.setdefault('igmp_groups', {}).setdefault(group.pop('group'), group)
        return igmp_dict

# ========================================================
# Parser for 'show ip igmp snooping mrouter vlan {vlan}'
# ========================================================
class ShowIpIgmpSnoopingMrouterVlanSchema(MetaParser):
    """
    Schema for 'show ip igmp snooping mrouter vlan {vlan}'
    """

    schema = {
        'vlan':
            {
                Any():
                {
                    'port': str
                },
            }
        }

class ShowIpIgmpSnoopingMrouterVlan(ShowIpIgmpSnoopingMrouterVlanSchema):
    """
    Parser for 'show ip igmp snooping mrouter vlan {vlan}'
    """
    cli_command = 'show ip igmp snooping mrouter vlan {vlan}'

    def cli(self, vlan=None, output=None):
        cmd = self.cli_command.format(vlan = vlan)
        if not output:
            out = self.device.execute(cmd)

        # initial variables
        vlan_dict = {}

        #  777    Po10(dynamic), Router
        p1 = re.compile(r'(?P<vlan_id>\d+)\s+(?P<port>.+)')

        for line in out.splitlines():
            line = line.strip()
        
            #  777    Po10(dynamic), Router
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict = vlan_dict.setdefault('vlan',{})
                vlan_id = group['vlan_id']
                port = group['port']
                ret_dict[vlan_id] = {}
                ret_dict[vlan_id]['port'] = port
        return vlan_dict

class ShowPlatformSoftwareIgmpSnoopingGroupsCountSchema(MetaParser):
    schema = {
             'ip_igmp_snooping_entries': int
             }

class ShowPlatformSoftwareIgmpSnoopingGroupsCount(ShowPlatformSoftwareIgmpSnoopingGroupsCountSchema):

    cli_command = [
                  'show platform software fed {switch} active ip igmp snooping groups count',
                  'show platform software fed active ip igmp snooping groups count'
                  ]

    def cli(self, output=None, switch=''):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)
        dict_count = {}
        # Total number of entries:8000
        p1 = re.compile(r'^Total\s+number\s+of\s+entries\:(?P<ip_igmp_snooping_entries>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Number of lines which match regexp = 240
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                count = int(groups['ip_igmp_snooping_entries'])
                dict_count['ip_igmp_snooping_entries'] = count

        return (dict_count)


# ===============================================================
# Parser for 'show ip igmp snooping querier vlan {vlan_id} detail '
# ===============================================================

class ShowIpIgmpSnoopingQuerierVlanDetailSchema(MetaParser):
    """Schema for show ip igmp snooping querier vlan {vlan_id} detail"""

    schema = {
        Optional('ip_address'): str,
        Optional('igmp_version'): str,
        Optional('port'): str,
        Optional('max_response_time'): str,
        'global_igmp': {
            'admin_state': str,           
            'admin_version': int,
            'source_ip_address': str,
            'query_interval': int,
            'max_response_time': int,
            'querier_timeout': int,
            'tcn_query_count': int,
            'tcn_query_interval': int,
        },
        'vlan': {     
            Any(): {       
                'admin_state': str,                             
                'admin_version': int,
                'source_ip_address': str,
                'query_interval': int,
                'max_response_time': int,
                'querier_timeout': int,
                'tcn_query_count': int,
                'tcn_query_interval': int,
                'operational_state': str,
                'operational_version': int,
                'tcn_query_pending_count': int,
            }
        }
    }

class ShowIpIgmpSnoopingQuerierVlanDetail(ShowIpIgmpSnoopingQuerierVlanDetailSchema):
    """Parser for show ip igmp snooping querier vlan {vlan_id} detail"""

    cli_command = 'show ip igmp snooping querier vlan {vlan_id} detail'

    def cli(self, vlan_id='', output=None):
        cmd = self.cli_command.format(vlan_id = vlan_id)
        if not output:
            output = self.device.execute(cmd)
        
        # IP address               : 1.1.1.1
        p1 = re.compile(r"^IP\s+address\s+:\s+(?P<ip_address>\S+)$")

        # IGMP version             : v2
        p2 = re.compile(r"^IGMP\s+version\s+:\s+(?P<igmp_version>\S+)$")

        # Port                     : Switch
        p3 = re.compile(r"^Port\s+:\s+(?P<port>\w+)$")

        # Max response time        : 10s
        p4 = re.compile(r"^Max\s+response\s+time\s+:\s+(?P<max_response_time>\S+)$")

        # Global IGMP switch querier status
        p5 = re.compile(r"^Global\s+IGMP\s+switch\s+querier\s+status$")

        # Vlan 100:   IGMP switch querier status
        p6 = re.compile(r"^Vlan\s+(?P<vlan>\d+):\s+IGMP\s+switch\s+querier\s+status$")

        # admin state                    : Enabled
        # admin state                    : Enabled (state inherited)
        p7 = re.compile(r"^admin\s+state\s+:\s+(?P<admin_state>\w+)(?:\s+\((?P<state>[\w\s]+)\))?")
       
        # admin version                  : 2
        p8 = re.compile(r"^admin\s+version\s+:\s+(?P<admin_version>\d+)$")

        # source IP address              : 1.1.1.1
        p9 = re.compile(r"^source\s+IP\s+address\s+:\s+(?P<source_ip_address>\S+)$")

        # query-interval (sec)           : 100
        p10 = re.compile(r"^query-interval\s+\(sec\)\s+:\s+(?P<query_interval>\d+)$")

        # max-response-time (sec)        : 10
        p11 = re.compile(r"^max-response-time\s+\(sec\)\s+:\s+(?P<max_response_time>\d+)$")

        # querier-timeout (sec)          : 120
        p12 = re.compile(r"^querier-timeout\s+\(sec\)\s+:\s+(?P<querier_timeout>\d+)$")

        # tcn query count                : 10
        p13 = re.compile(r"^tcn\s+query\s+count\s+:\s+(?P<tcn_query_count>\d+)$")

        # tcn query interval (sec)       : 10
        p14 = re.compile(r"^tcn\s+query\s+interval\s+\(sec\)\s+:\s+(?P<tcn_query_interval>\d+)$")

        # operational state              : Querier
        # operational state              : Non-Querier
        p15 = re.compile(r"^operational\s+state\s+:\s+(?P<operational_state>\S+)$")

        # operational version            : 2
        p16 = re.compile(r"^operational\s+version\s+:\s+(?P<operational_version>\d+)$")

        # tcn query pending count        : 0
        p17 = re.compile(r"^tcn\s+query\s+pending\s+count\s+:\s+(?P<tcn_query_pending_count>\d+)$")
        
        ret_dict = {}
        global_dict = {}       
       
        for line in output.splitlines():
            line = line.strip()           

            # IP address               : 1.1.1.1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['ip_address'] = group['ip_address']
                continue

            # IGMP version             : v2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['igmp_version'] = group['igmp_version']
                continue

            # Port                     : Switch
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'] = group['port']
                continue
                            
           # Max response time        : 10s
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict['max_response_time'] = group['max_response_time']
                continue

            # Vlan 100:   IGMP switch querier status
            m = p6.match(line)
            if m:                
                vlan_dict = ret_dict.setdefault("vlan", {}).setdefault(m.groupdict()["vlan"], {})
                continue
                
            # Global IGMP switch querier status
            m = p5.match(line)
            if m:                
                global_dict = ret_dict.setdefault("global_igmp", {}) 
                vlan_dict = global_dict               
                continue           
          
            # admin state                    : Enabled (state inherited)
            m = p7.match(line)        
            if m:         
                group = m.groupdict()                 
                vlan_dict["admin_state"] = group["admin_state"]
                continue
                 
            # admin version                  : 2
            m = p8.match(line)
            if m:
                group = m.groupdict()
                vlan_dict["admin_version"] = int(group["admin_version"])                
                continue

            # source IP address              : 1.1.1.1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                vlan_dict["source_ip_address"] = group["source_ip_address"]
                continue

            # query-interval (sec)           : 100
            m = p10.match(line)
            if m:
                group = m.groupdict()
                vlan_dict["query_interval"] = int(group["query_interval"])             
                continue

            # max-response-time (sec)        : 10
            m = p11.match(line)
            if m:
                group = m.groupdict()
                vlan_dict["max_response_time"] = int(group["max_response_time"])
                continue

            # querier-timeout (sec)          : 120
            m = p12.match(line)
            if m:
                group = m.groupdict()
                vlan_dict["querier_timeout"] = int(group["querier_timeout"])
                continue

            # tcn query count                : 10
            m = p13.match(line)
            if m:
                group = m.groupdict()
                vlan_dict["tcn_query_count"] = int(group["tcn_query_count"])                
                continue

            # tcn query interval (sec)       : 10
            m = p14.match(line)
            if m:
                group = m.groupdict()
                vlan_dict["tcn_query_interval"] = int(group["tcn_query_interval"])
                continue

            # operational state              : Querier
            m = p15.match(line)
            if m:
                group = m.groupdict()
                vlan_dict['operational_state'] = group['operational_state']
                continue

            # operational version            : 2
            m = p16.match(line)
            if m:
                group = m.groupdict()
                vlan_dict['operational_version'] = int(group['operational_version'])
                continue

            # tcn query pending count        : 0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                vlan_dict['tcn_query_pending_count'] = int(group['tcn_query_pending_count'])
                continue

        return ret_dict